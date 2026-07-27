"""Credential loading for EyeDataHub.

Called once at package import time. Loads a local ``.env`` file into
``os.environ`` and authenticates Hugging Face Hub if ``HF_TOKEN`` is present.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional


def load_credentials(
    env_file: str | os.PathLike[str] | None = None,
    *,
    override: bool = False,
    login_huggingface: bool = True,
) -> Optional[Path]:
    """Load credentials from environment variables and an optional dotenv file.

    The default behavior is intentionally conservative:

    1. Load ``.env`` from the current working directory or one of its parents.
       Existing environment variables are not overridden.
    2. If ``EYEDATAHUB_ENV_FILE`` is set, load that file instead.
    3. If ``HF_TOKEN`` or ``HUGGING_FACE_HUB_TOKEN`` is set, call
       ``huggingface_hub.login()`` so later gated Hub downloads are
       authenticated.

    Args:
        env_file: Explicit dotenv file path. Takes precedence over
            ``EYEDATAHUB_ENV_FILE``.
        override: Whether values in the dotenv file should replace existing
            environment variables.
        login_huggingface: Disable in tests or scripts that only need to parse
            variables without touching Hugging Face credentials.

    Returns:
        The dotenv file that was loaded, or ``None`` when no file was found or
        ``python-dotenv`` is unavailable.
    """
    loaded = _load_dotenv(env_file=env_file, override=override)
    if login_huggingface:
        _login_huggingface()
    return loaded


def _load_dotenv(
    env_file: str | os.PathLike[str] | None = None,
    *,
    override: bool = False,
) -> Optional[Path]:
    try:
        from dotenv import find_dotenv, load_dotenv
    except ImportError:
        return None  # python-dotenv not installed; rely on real env vars

    path_value = (
        env_file
        or os.environ.get("EYEDATAHUB_ENV_FILE")
    )
    if path_value:
        path = Path(path_value).expanduser()
        if not path.is_file():
            return None
        load_dotenv(path, override=override)
        return path

    found = find_dotenv(usecwd=True)
    if not found:
        return None
    path = Path(found)
    load_dotenv(path, override=override)
    return path


def _login_huggingface() -> None:
    # Support both the new (HF_TOKEN) and old (HUGGING_FACE_HUB_TOKEN) names.
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    if not token:
        return
    try:
        from huggingface_hub import HfFolder, login

        # Skip if already logged in with the same token to avoid redundant I/O.
        if HfFolder.get_token() == token:
            return
        login(token=token, add_to_git_credential=False)
    except ImportError:
        # huggingface_hub is optional; newer Hub clients still read HF_TOKEN.
        pass
    except Exception:
        # Never crash import on a bad token; the downstream call will surface
        # the platform-specific authentication error.
        pass
