"""EyeDataHub MCP (Model Context Protocol) server - stdio JSON-RPC.

Exposes the EyeDataHub catalog as a set of read-only tools that MCP-aware clients
(Claude Desktop, mcp-cli, custom agents) can call:

  - eyedatahub.list_datasets(modality=, task=, license_type=, access_friction=)
  - eyedatahub.get_dataset(name=)
  - eyedatahub.filter_by_license(use_case=)
  - eyedatahub.plan_fundus_foundation_model(...)
  - eyedatahub.stats()

Design notes:
  - Speaks a minimal MCP-2024 stdio protocol so it works without any
    third-party MCP SDK. Clients that expect a stricter MCP handshake
    should still get the tool list + tool call semantics.
   - Everything is read-only. This server never triggers downloads or accepts
     source terms. Transfer requires a separate explicit CLI or Python call.
  - Run:
        python -m eyedatahub.agent.mcp_server
    then connect an MCP client to the stdio pipes.

Register with Claude Desktop by adding to
`~/.config/claude/claude_desktop_config.json`:

    {
      "mcpServers": {
        "eyedatahub": {
          "command": "python",
          "args": ["-m", "eyedatahub.agent.mcp_server"]
        }
      }
    }
"""
from __future__ import annotations

import json
import sys
from typing import Any


TOOLS: list[dict] = [
    {
        "name": "eyedatahub.list_datasets",
        "description": (
            "List EyeDataHub datasets. Filter by modality (for example fundus, "
            "oct, octa, adaptive_optics, cell_microscopy, or omics), task, "
            "normalized source-term category, access friction, or acquisition "
            "support. This operation never starts a transfer."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "modality": {"type": "string"},
                "task": {"type": "string"},
                "license_type": {"type": "string"},
                "access_friction": {"type": "string"},
                "acquisition_support": {"type": "string"},
            },
        },
    },
    {
        "name": "eyedatahub.get_dataset",
        "description": (
            "Return full metadata, typed citations, and explicit preflight/acquisition snippets "
            "for a single catalog record."
        ),
        "inputSchema": {
            "type": "object",
            "required": ["name"],
            "properties": {"name": {"type": "string"}},
        },
    },
    {
        "name": "eyedatahub.filter_by_license",
        "description": (
            "Return a descriptive normalized source-term filter for a use case. "
            "This is not a legal or permission recommendation."
        ),
        "inputSchema": {
            "type": "object",
            "required": ["use_case"],
            "properties": {
                "use_case": {
                    "type": "string",
                    "enum": [
                        "academic_research",
                        "internal_rnd",
                        "commercial_product",
                        "opensource_release",
                        "foundation_pretraining",
                    ],
                }
            },
        },
    },
    {
        "name": "eyedatahub.stats",
        "description": (
            "Aggregate catalog statistics across independent access, acquisition, "
            "source-term, category, and backend dimensions."
        ),
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "eyedatahub.plan_fundus_foundation_model",
        "description": (
            "Build a side-effect-free fundus foundation-model data plan. "
            "Selects a license-filtered pretraining pool, proposes held-out "
            "datasets for disease gaps, and returns exact inspection and "
            "download commands. It never downloads data or starts training."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "license_type": {
                    "type": "string",
                    "enum": [
                        "standard-no-nc",
                        "non-commercial",
                        "research-only",
                        "any",
                    ],
                    "default": "standard-no-nc",
                },
                "max_pretraining_datasets": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 50,
                    "default": 8,
                },
                "gaps": {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": [
                        "diabetic_retinopathy",
                        "glaucoma",
                        "amd",
                    ],
                },
                "max_validation_per_gap": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 10,
                    "default": 3,
                },
                "include_manual": {"type": "boolean", "default": False},
            },
        },
    },
]


def _dataset_payload(ds) -> dict:
    from eyedatahub.catalog import dataset_to_record

    return dataset_to_record(ds)


def call_tool(name: str, args: dict) -> dict:
    """Dispatch a tool call. Returns a dict with `content` and optional `error`."""
    from eyedatahub.catalog import citation_payload
    from eyedatahub.core.dataset import license_matches_filter
    from eyedatahub.datasets.registry import REGISTRY

    if name == "eyedatahub.list_datasets":
        results = REGISTRY.list_datasets(
            modality=args.get("modality"),
            task=args.get("task"),
        )
        lic = args.get("license_type")
        if lic:
            results = [d for d in results if license_matches_filter(d.info.license, lic)]
        if args.get("access_friction"):
            results = [
                d for d in results
                if d.info.access_friction == args["access_friction"]
            ]
        if args.get("acquisition_support"):
            results = [
                d for d in results
                if d.info.acquisition_support == args["acquisition_support"]
            ]
        results = sorted(results, key=lambda item: item.info.name)
        return {"content": [_dataset_payload(d) for d in results]}

    if name == "eyedatahub.get_dataset":
        try:
            ds = REGISTRY.get_dataset(args["name"])
        except KeyError as e:
            return {"error": str(e)}
        info = ds.info
        return {
            "content": {
                **_dataset_payload(ds),
                "description": info.description,
                "classes": info.classes,
                "num_classes": info.num_classes,
                "splits": info.splits,
                "citation": info.citation,
                "tags": info.tags,
                "notes": info.notes,
                "snippets": {
                    "cli": (
                        f"eyehub download {info.name} --dry-run\n"
                        f"eyehub download {info.name}"
                    ),
                    "python": (
                        "from pathlib import Path\n"
                        "from eyedatahub.acquisition import acquire_dataset, preflight_dataset\n"
                        "from eyedatahub.datasets.registry import REGISTRY\n"
                        f"ds = REGISTRY.get_dataset('{info.name}')\n"
                        "data_dir = Path('~/.eyedatahub/data').expanduser()\n"
                        "plan = preflight_dataset(ds, data_dir)  # read-only\n"
                        "result = acquire_dataset(ds, data_dir)  # explicit request"
                    ),
                    "url": info.download_url,
                },
                "citations": citation_payload(info),
            }
        }

    if name == "eyedatahub.filter_by_license":
        use_case = args["use_case"]
        recommendation = {
            "academic_research": (
                "any",
                "Inspect every source record; research-only and unknown terms remain separate categories.",
            ),
            "internal_rnd": (
                "any",
                "Inspect every source record and its component-specific terms before use.",
            ),
            "commercial_product": (
                "standard-no-nc",
                "Descriptive screen for normalized labels without an explicit noncommercial clause.",
            ),
            "opensource_release": (
                "standard-no-nc",
                "Descriptive screen only; attribution, share-alike, component scope, and model-release questions remain for the user.",
            ),
            "foundation_pretraining": (
                "standard-no-nc",
                "Descriptive screen only; it does not establish permission to train or release a model.",
            ),
        }
        flag, note = recommendation[use_case]
        matching = REGISTRY.list_datasets() if flag == "any" else [
            d for d in REGISTRY.list_datasets()
            if license_matches_filter(d.info.license, flag)
        ]
        return {
            "content": {
                "filter": flag,
                "note": note,
                "matching_dataset_count": len(matching),
                "matching_datasets": [d.info.name for d in matching],
                "disclaimer": (
                    "EyeDataHub reports source-stated terms and normalized labels. "
                    "This output is not legal advice and does not determine permission."
                ),
            }
        }

    if name == "eyedatahub.stats":
        from collections import Counter

        all_ds = REGISTRY.list_datasets()
        return {
            "content": {
                "total": len(all_ds),
                "reported_item_counts_are_not_summed": True,
                "by_primary_category": dict(Counter(d.info.primary_category for d in all_ds)),
                "by_contained_modality": dict(
                    Counter(modality for d in all_ds for modality in d.info.modalities)
                ),
                "by_license_family": dict(Counter(d.info.license_family for d in all_ds)),
                "by_access_friction": dict(Counter(d.info.access_friction for d in all_ds)),
                "by_acquisition_support": dict(Counter(d.info.acquisition_support for d in all_ds)),
                "by_backend": dict(Counter(d.info.download_type for d in all_ds)),
            }
        }

    if name == "eyedatahub.plan_fundus_foundation_model":
        from eyedatahub.agent.planner import build_fundus_foundation_plan

        return {
            "content": build_fundus_foundation_plan(
                license_type=args.get("license_type", "standard-no-nc"),
                max_pretraining_datasets=args.get(
                    "max_pretraining_datasets", 8
                ),
                gaps=args.get("gaps"),
                max_validation_per_gap=args.get(
                    "max_validation_per_gap", 3
                ),
                include_manual=args.get("include_manual", False),
            )
        }

    return {"error": f"Unknown tool: {name}"}


def rpc_response(request_id: Any, result: dict | None = None, error: dict | None = None) -> str:
    resp = {"jsonrpc": "2.0", "id": request_id}
    if error is not None:
        resp["error"] = error
    else:
        resp["result"] = result
    return json.dumps(resp)


def handle_request(req: dict) -> str | None:
    method = req.get("method")
    req_id = req.get("id")

    if method == "initialize":
        from eyedatahub import __version__

        return rpc_response(
            req_id,
            result={
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "eyedatahub", "version": __version__},
            },
        )
    if method == "notifications/initialized":
        return None  # notification — no response
    if method == "tools/list":
        return rpc_response(req_id, result={"tools": TOOLS})
    if method == "tools/call":
        params = req.get("params", {})
        name = params.get("name")
        args = params.get("arguments", {})
        try:
            r = call_tool(name, args)
        except Exception as e:
            return rpc_response(req_id, error={"code": -32000, "message": str(e)})
        if "error" in r:
            return rpc_response(req_id, error={"code": -32602, "message": r["error"]})
        return rpc_response(
            req_id,
            result={
                "content": [
                    {"type": "text", "text": json.dumps(r["content"], indent=2)}
                ]
            },
        )
    return rpc_response(req_id, error={"code": -32601, "message": f"Unknown method: {method}"})


def serve() -> int:
    """Read newline-delimited JSON-RPC on stdin, write responses on stdout."""
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        try:
            req = json.loads(raw)
        except json.JSONDecodeError:
            continue
        resp = handle_request(req)
        if resp is not None:
            sys.stdout.write(resp + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(serve())
