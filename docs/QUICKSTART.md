# Quickstart

## 1. Connect the remote MCP

Use the canonical Streamable HTTP endpoint:

```text
https://mcp.grabbitapp.com/api/mcp
```

Generic configuration:

```json
{
  "mcpServers": {
    "grabblist": {
      "type": "http",
      "url": "https://mcp.grabbitapp.com/api/mcp"
    }
  }
}
```

Your client should discover OAuth automatically, open the Grabblist consent page, and request one or both scopes:

- `grabblist:read`
- `grabblist:write`

Do not paste a shared API key or Bearer token into the configuration.

## 2. Verify the connection

Ask the client:

> Use Grabblist `ping` and tell me the connected server version.

A connected client should report Grabblist 2.1.0. Tool discovery should return 23 tools.

## 3. Try a read-only request

> List up to five of my most recently saved items. Do not change anything.

The agent should use `get_wishlist` with a small limit.

## 4. Save one item

Give the agent a public product or listing URL and ask:

> Save this as a static snapshot. Extract only details actually present on the page, tell me which fields are missing, and do not invent a current or original price.

`add_item` requires an explicit title, numeric price, currency, URL, and platform. The agent should inspect the source first and ask for clarification if a required value cannot be established.

## 5. Organize it

> Create a collection named “Desk Upgrade”, add the saved item, and show the resulting collection total.

The agent should use `create_collection`, `add_to_collection`, and `list_collections`.

## Troubleshooting

### Authentication required

Reconnect the MCP through your client's OAuth flow. Do not copy tokens from browser storage or logs.

### Read works but writes fail

Reconnect and grant `grabblist:write`. `ask_agent` requires both read and write scopes.

### `ask_agent` is unavailable

The connected Grabblist account must have a supported AI provider configured in Grabblist Settings.

### A saved price is stale

Grabblist stores snapshots; it does not monitor pages continuously. Recheck the public source, then call `update_price` only with the newly observed price and its provenance.
