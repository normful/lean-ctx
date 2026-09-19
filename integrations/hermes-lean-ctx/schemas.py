"""Engine tool schemas injected into the Hermes agent tool list.

Each schema is ``{"name", "description", "parameters"}`` per the Context Engine
plugin guide. Parameters mirror the daemon's real ``/v1`` tool argument schemas
so calls dispatched through :mod:`tools` are accepted as-is. These are
lean-ctx's recall / code-intelligence surface — the agent pulls exactly the
context it needs instead of holding it in the window.
"""

from __future__ import annotations

from typing import Any, Dict, List

CTX_READ: Dict[str, Any] = {
    "name": "ctx_read",
    "description": (
        "Read a file (cached + compressed). Prefer over loading whole files into "
        "context; use mode/line ranges to read only what is needed."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Absolute file path"},
            "mode": {
                "type": "string",
                "description": "auto (default)|full|map|signatures|lines:N-M|...",
            },
            "start_line": {"type": "integer", "description": "First line, 1-based"},
            "limit": {"type": "integer", "description": "Max lines to read"},
        },
        "required": ["path"],
    },
}

# Order is stable for deterministic tool-list injection.
ALL_SCHEMAS: List[Dict[str, Any]] = [
    CTX_READ,
]

TOOL_NAMES: List[str] = [s["name"] for s in ALL_SCHEMAS]


def recall_hint() -> str:
    """One-line hint appended to compaction summaries listing recovery tools."""
    return "Recover detail with: " + ", ".join(f"{n}()" for n in TOOL_NAMES) + "."
