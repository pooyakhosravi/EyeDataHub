---
id: agentic
title: "Optional machine interfaces"
sidebar_label: Machine interfaces
description: "Use the shared EyeDataHub metadata through Python, JSON, or the optional read-only MCP server."
---

# Optional machine interfaces

The command-line workflow is EyeDataHub's primary interface. Python, JSON,
JSON-LD, and Model Context Protocol (MCP) provide secondary views of the same
metadata implementation. Agreement among them is a software-conformance check,
not independent validation of source records.

## Deterministic JSON

```bash
eyehub search --modality oct --json
eyehub show airogs --json
eyehub cite airogs --type dataset --format json
eyehub preflight airogs --json
```

These operations are read-only. Dataset transfer begins only through an
explicit non-dry-run `eyehub download` command.

## Python

```python
from eyedatahub.datasets.registry import REGISTRY

dataset = REGISTRY.get_dataset("airogs")
print(dataset.info.access_friction)
print(dataset.info.source_terms)
print(dataset.info.terms_scope)
```

`REGISTRY` is retained as an internal compatibility name; the public product is
a command-line access tool backed by a versioned catalog snapshot.

## Read-only MCP server

```bash
python -m eyedatahub.agent.mcp_server
```

Example client configuration:

```json
{
  "mcpServers": {
    "eyedatahub": {
      "command": "python",
      "args": ["-m", "eyedatahub.agent.mcp_server"],
      "cwd": "/path/to/EyeDataHub"
    }
  }
}
```

The MCP server supports metadata retrieval and reviewable planning. It cannot
transfer data, accept source terms, approve a route, bypass access controls,
choose or train a model, or determine legal, ethical, clinical, or scientific
suitability. Any software client must preserve unknown values and show the
official evidence and dated verification state.

## Reproducible interface checks

The test suite covers Python, command-line, and MCP interface conformance,
along with manually specified expected-query fixtures. Run it with:

```bash
python -m pytest -q
```
