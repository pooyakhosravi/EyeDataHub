# AGENTS.md

Pointer file for cross-tool AI coding agents (Cursor, Aider, Cline,
Continue, OpenAI Codex CLI, etc.).

**Canonical agent guide for this repository is `CLAUDE.md`.** Read it first.
It covers intent, layout, conventions, platform notes, common workflows, and
things to avoid.

## Structured access for agents

| Interface | Purpose |
|---|---|
| `llms.txt` | Repo entry points for LLM tools (follows llmstxt.org). |
| `llms-full.txt` | Token-efficient full catalog of all 251 records. |
| `eyehub search --json` | Machine-readable filtered catalog. |
| `eyehub cite <name> --type {dataset,article,software}` | Typed citation output. |
| `eyehub preflight <name> --json` | Read-only terms, access, and loader preflight. |
| `eyehub show <name> --json` | Machine-readable single-dataset detail. |
| `eyehub show <name> --copy {cli,python,bibtex,apa,url}` | One snippet, pipe-friendly. |
| `eyehub search --modality <name> --json` | Read-only catalog search over contained modalities. |
| `eyehub cite <name> --type dataset --format bibtex` | Typed dataset citation export. |
| `eyehub download <name> --dry-run --json` | Side-effect-free terms and access preflight. |
| `python -m eyedatahub.agent.mcp_server` | Stdio MCP JSON-RPC server. |
| `from eyedatahub.datasets.registry import REGISTRY` | Direct Python access to 251 auto-registered records; `REGISTRY` is an internal compatibility name. |

Use `eyedatahub` for Python imports and `eyehub` for CLI commands.

## Cross-tool config

- `.cursorrules` - Cursor rules pointing to CLAUDE.md plus license discipline.
- `.aider.conf.yml` - Aider read-list including CLAUDE.md and llms.txt.
- Add for Claude Desktop MCP: see `eyedatahub/agent/mcp_server.py` docstring.

Modular skills for common tasks live under `.claude/skills/`:

- `add-dataset/` - walks through adding a new dataset end-to-end.
- `license-filter/` - recommends datasets given a use case.
- `build-hf-subset/` - assembles a custom Hugging Face mirror.
- `benchmark-model/` - archived planning skill; model benchmarking is outside the dataset-access CLI surface.

The human contributor workflow is in `CONTRIBUTING.md`. Use it as the source
of truth when generating PRs.
