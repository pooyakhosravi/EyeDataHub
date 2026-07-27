"""
Helpers for loading HuggingFace models with quantization and graceful fallback.

When GPU VRAM is insufficient to hold a quantized model entirely on-device,
``device_map="auto"`` offloads some layers to CPU or disk — which bitsandbytes
does not support unless explicitly configured.

``load_hf_model`` handles three tiers automatically:

1. Quantized (4-bit or 8-bit) on GPU — preferred, lowest VRAM usage
2. Quantized + CPU-offload enabled — for models that partially spill to CPU
3. fp16/bf16 without quantization — safest fallback, higher VRAM usage

Usage in an example file::

    from eyedatahub.utils.hf_loading import build_bnb_config, load_hf_model

    bnb_cfg = build_bnb_config(load_in_4bit=True)
    model = load_hf_model(
        AutoModelForImageTextToText,
        model_id,
        device_map="auto",
        torch_dtype="auto",
        quantization_config=bnb_cfg,
    )
"""
from __future__ import annotations

from typing import Any, Optional, Type


def build_bnb_config(
    load_in_4bit: bool = False,
    load_in_8bit: bool = False,
    compute_dtype: Optional[Any] = None,
    enable_cpu_offload: bool = True,
):
    """
    Build a ``BitsAndBytesConfig`` with sensible defaults.

    Args:
        load_in_4bit:        Use NF4 4-bit quantisation (recommended).
        load_in_8bit:        Use LLM.int8() quantisation.
        compute_dtype:       Dtype for 4-bit compute (default: torch.bfloat16).
        enable_cpu_offload:  Allow 8-bit layers to offload to CPU in fp32
                             when VRAM is tight (``llm_int8_enable_fp32_cpu_offload``).

    Returns:
        BitsAndBytesConfig instance, or None if neither flag is set.
    """
    if not load_in_4bit and not load_in_8bit:
        return None

    try:
        import torch
        from transformers import BitsAndBytesConfig

        if compute_dtype is None:
            compute_dtype = torch.bfloat16

        return BitsAndBytesConfig(
            load_in_4bit=load_in_4bit,
            load_in_8bit=load_in_8bit and not load_in_4bit,
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_use_double_quant=True,
            llm_int8_enable_fp32_cpu_offload=enable_cpu_offload,
        )
    except ImportError:
        print(
            "  [warning] bitsandbytes not installed — "
            "quantisation disabled. Run: pip install bitsandbytes"
        )
        return None


def load_hf_model(
    model_class: Type,
    model_id: str,
    **kwargs: Any,
):
    """
    Load a HuggingFace model with automatic fallback on quantisation errors.

    Tries three strategies in order:
    1. Load with the provided kwargs (typically quantised).
    2. If the quantised load fails because of CPU/disk offloading conflicts,
       retry with ``llm_int8_enable_fp32_cpu_offload=True`` patched in.
    3. If that also fails, drop the quantisation config entirely and load in
       fp16, printing a warning.

    Args:
        model_class:  HF model class (e.g. ``AutoModelForImageTextToText``).
        model_id:     HuggingFace model ID or local path.
        **kwargs:     Passed verbatim to ``model_class.from_pretrained``.

    Returns:
        Loaded model.
    """
    import torch

    def _normalise_kwargs(kw: dict) -> dict:
        """Rename torch_dtype → dtype if transformers expects the newer key."""
        import transformers
        ver = tuple(int(x) for x in transformers.__version__.split(".")[:2])
        if ver >= (4, 52) and "torch_dtype" in kw and "dtype" not in kw:
            kw = {**kw, "dtype": kw.pop("torch_dtype")}
        return kw

    def _is_recoverable(e: Exception) -> bool:
        err = str(e)
        return (
            "quantized" in err.lower()
            or "llm_int8_enable_fp32_cpu_offload" in err
            or "dispatch" in err.lower()
            # bitsandbytes version mismatch with transformers
            or "_is_hf_initialized" in err
            or "Params4bit" in err
            or "Linear4bit" in err
            or "unexpected keyword argument" in err and "bit" in err.lower()
        )

    kwargs = _normalise_kwargs(dict(kwargs))

    # ── Attempt 1: load as requested ─────────────────────────────────────────
    try:
        return model_class.from_pretrained(model_id, **kwargs)

    except (RuntimeError, TypeError) as e:
        if not _is_recoverable(e):
            raise
        print(f"  [warning] Quantised load failed ({type(e).__name__}: {e})")

    # ── Attempt 2: patch in CPU-offload flag ──────────────────────────────────
    print("  Retrying with CPU-offload enabled …")
    bnb_cfg = kwargs.get("quantization_config")
    if bnb_cfg is not None:
        try:
            from transformers import BitsAndBytesConfig

            patched = BitsAndBytesConfig(
                load_in_4bit=getattr(bnb_cfg, "load_in_4bit", False),
                load_in_8bit=getattr(bnb_cfg, "load_in_8bit", False),
                bnb_4bit_compute_dtype=getattr(bnb_cfg, "bnb_4bit_compute_dtype", torch.bfloat16),
                bnb_4bit_use_double_quant=getattr(bnb_cfg, "bnb_4bit_use_double_quant", True),
                llm_int8_enable_fp32_cpu_offload=True,
            )
            return model_class.from_pretrained(
                model_id, **{**kwargs, "quantization_config": patched}
            )
        except (RuntimeError, TypeError):
            pass  # fall through to attempt 3

    # ── Attempt 3: no quantisation, bfloat16 ─────────────────────────────────
    print(
        "  [warning] Quantisation fallback also failed — "
        "loading without quantisation (bfloat16). Higher VRAM usage."
    )
    safe_kwargs = {k: v for k, v in kwargs.items() if k not in ("quantization_config", "dtype")}
    safe_kwargs["torch_dtype"] = torch.bfloat16
    safe_kwargs = _normalise_kwargs(safe_kwargs)
    return model_class.from_pretrained(model_id, **safe_kwargs)
