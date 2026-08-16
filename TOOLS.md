# Grabblist MCP tools

Grabblist 2.1.0 exposes 23 authenticated tools. MCP `tools/list` remains the machine-readable authority for exact input schemas.

## Read scope

These tools require `grabblist:read`.

| Tool | Purpose |
|---|---|
| `ping` | Confirm connectivity and return the service version |
| `get_wishlist` | List the user's non-deleted saved items |
| `get_item` | Return one saved item snapshot |
| `search_saved` | Search saved items by keyword |
| `list_collections` | List collections or return one collection and its items |
| `get_item_graph` | Return an item and its linked alternatives, complements, upgrades, duplicates, and same-seller records |
| `get_item_history` | Return item change history |
| `get_collection_activity` | Return collection additions, removals, and edits |

## Write scope

These tools require `grabblist:write`.

| Tool | Purpose |
|---|---|
| `add_item` | Save a static item snapshot |
| `update_item` | Update one item or apply the same supplied fields to a bounded batch |
| `update_price` | Manually update an item's price and record the change |
| `delete_item` | Soft-delete one item or a bounded batch |
| `restore_item` | Restore one soft-deleted item or a bounded batch |
| `create_collection` | Create a collection with optional presentation and budget fields |
| `update_collection` | Update collection metadata, budget, or sharing state |
| `delete_collection` | Delete a collection without deleting its items |
| `add_to_collection` | Add an existing item to a collection |
| `remove_from_collection` | Remove items from a collection without deleting them |
| `set_pinned_items` | Set up to three ordered top picks for a collection |
| `link_items` | Create alternative, complement, upgrade, duplicate, or same-seller relationships |
| `unlink_items` | Remove one typed item relationship |
| `send_feedback` | Submit a bug, parsing failure, feature request, or general feedback report |

## Both scopes

| Tool | Purpose |
|---|---|
| `ask_agent` | Ask the AI assistant configured in the user's Grabblist account to analyze saved items |

`ask_agent` additionally requires the user to configure a supported AI provider in Grabblist Settings.

## Behavior notes

- Saved items are static snapshots and do not auto-update.
- Delete operations are explicitly identified as destructive to MCP clients.
- Public-page metadata fetch and configured AI-provider calls are identified as open-world operations.
- Cross-account and nonexistent identifiers return the same not-found behavior.
- Clients should confirm destructive actions with the user.
