#!/usr/bin/env python3
"""Validate the public Grabblist MCP integration repository."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ENDPOINT = "https://mcp.grabbitapp.com/api/mcp"
REGISTRY_NAME = "com.grabbitapp/grabblist"
EXPECTED_TOOLS = {
    "ping",
    "get_wishlist",
    "get_item",
    "add_item",
    "delete_item",
    "restore_item",
    "search_saved",
    "update_price",
    "update_item",
    "list_collections",
    "create_collection",
    "add_to_collection",
    "remove_from_collection",
    "delete_collection",
    "update_collection",
    "link_items",
    "get_item_graph",
    "unlink_items",
    "get_item_history",
    "get_collection_activity",
    "set_pinned_items",
    "send_feedback",
    "ask_agent",
}


def fail(message: str) -> None:
    raise SystemExit(message)


def load_json(relative_path: str) -> dict:
    path = ROOT / relative_path
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid {relative_path}: {exc}")


def validate_metadata() -> None:
    server = load_json("server.json")
    if server.get("name") != REGISTRY_NAME:
        fail("server.json has the wrong Registry name")
    if server.get("version") != "2.1.0":
        fail("server.json must describe the currently deployed service version")
    remotes = server.get("remotes")
    if remotes != [{"type": "streamable-http", "url": CANONICAL_ENDPOINT}]:
        fail("server.json must expose only the canonical Streamable HTTP endpoint")
    if "packages" in server or "repository" in server:
        fail("server.json must not imply a package or source repository")

    client = load_json("mcp.json")
    expected = {
        "mcpServers": {
            "grabblist": {"type": "http", "url": CANONICAL_ENDPOINT}
        }
    }
    if client != expected:
        fail("mcp.json does not match the canonical client configuration")


def validate_tool_inventory() -> None:
    tools_doc = (ROOT / "TOOLS.md").read_text(encoding="utf-8")
    documented = set(re.findall(r"\| `([a-z_]+)` \|", tools_doc))
    if documented != EXPECTED_TOOLS:
        missing = sorted(EXPECTED_TOOLS - documented)
        extra = sorted(documented - EXPECTED_TOOLS)
        fail(f"tool inventory mismatch: missing={missing}, extra={extra}")


def validate_boundary() -> None:
    required = {
        "README.md",
        "SECURITY.md",
        "TOOLS.md",
        "CONTRIBUTING.md",
        "NOTICE.md",
        "server.json",
        "mcp.json",
    }
    missing = sorted(name for name in required if not (ROOT / name).is_file())
    if missing:
        fail(f"missing public files: {missing}")

    forbidden_paths = {
        "grabbit-web",
        "browse-service",
        "extension",
        "extension-v2",
        "operator",
    }
    present = sorted(name for name in forbidden_paths if (ROOT / name).exists())
    if present:
        fail(f"private product paths entered the public repository: {present}")

    secret_patterns = {
        "JWT": re.compile(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
        "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
        "cloud access key": re.compile(r"AKIA[0-9A-Z]{16}"),
        "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        "credential assignment": re.compile(
            r"(?i)(?:secret|password|token|api[_-]?key)\s*[:=]\s*[\"']?"
            r"[A-Za-z0-9_./+~-]{24,}"
        ),
    }
    internal_markers = (
        "/home/ali/",
        ".env.production",
        "service_role",
        "sb_secret_",
        "sbp_",
        "up.railway.app",
    )

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path == Path(__file__):
            continue
        if path.suffix.lower() not in {".md", ".json", ".yml", ".yaml", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in secret_patterns.items():
            if pattern.search(text):
                fail(f"possible {label} in {path.relative_to(ROOT)}")
        lowered = text.lower()
        for marker in internal_markers:
            if marker.lower() in lowered:
                fail(f"private infrastructure marker in {path.relative_to(ROOT)}")


def main() -> None:
    validate_metadata()
    validate_tool_inventory()
    validate_boundary()
    print("public Grabblist MCP repository validation passed")


if __name__ == "__main__":
    main()
