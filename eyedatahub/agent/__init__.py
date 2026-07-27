"""Agent-facing entry points for EyeDataHub.

Modules:
  - mcp_server: stdio JSON-RPC MCP server exposing registry query tools.
  - planner: side-effect-free workflow plans for dataset selection and handoff.
"""

from eyedatahub.agent.planner import build_fundus_foundation_plan

__all__ = ["build_fundus_foundation_plan"]
