# Grabblist MCP

**Persistent, user-controlled memory for things you find online.**

Grabblist is a hosted remote MCP server for saving, searching, organizing, comparing, and revisiting products, services, courses, rentals, events, listings, and other web finds across AI conversations.

[![Official MCP Registry](https://img.shields.io/badge/Official_MCP_Registry-active-12b981)](https://registry.modelcontextprotocol.io/v0/servers/com.grabbitapp%2Fgrabblist/versions/latest)
[![Glama Connector](https://img.shields.io/badge/Glama_Connector-healthy-12b981)](https://glama.ai/mcp/connectors/com.grabbitapp/grabblist)
[![MCP](https://img.shields.io/badge/MCP-Streamable_HTTP-6f42c1)](https://modelcontextprotocol.io/)

- **23 tools** for saved items, collections, relationships, history, feedback, and shopping research.
- **OAuth 2.0 + PKCE** with Dynamic Client Registration; no shared API key to paste into a client.
- **User-controlled snapshots:** Grabblist does not continuously scrape pages or promise live prices.
- **Multi-user isolation:** every authenticated account sees only its own data.

## Connect

Use the canonical remote MCP endpoint in any client that supports Streamable HTTP and OAuth discovery:

```text
https://mcp.grabbitapp.com/api/mcp
```

Generic MCP configuration:

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

The client discovers Grabblist's OAuth metadata, opens the consent screen, and connects the user's account. Users should not paste a shared Bearer token into third-party directory forms.

## What agents can do

### Save and decide

- save a static snapshot of a product, service, rental, course, listing, or event;
- add notes, tags, decision status, quantity, target price, condition, and seller details;
- manually record price changes;
- soft-delete and restore items.

### Organize research

- search saved items across conversations;
- create collections with budgets and pinned top picks;
- link alternatives, complements, upgrades, duplicates, and same-seller items;
- inspect item history and collection activity.

### Collaborate safely

- share a collection when the user explicitly enables public sharing;
- submit bugs, parsing failures, feedback, and feature requests;
- optionally ask the AI provider configured by that user to analyze saved items.

See [TOOLS.md](TOOLS.md) for the complete inventory and scope map.

## Agent resources

The repository includes reusable, credential-free material for humans and agent hosts:

- [Quickstart](docs/QUICKSTART.md) — connect, authorize, verify, and save the first item;
- [Agent workflows](docs/WORKFLOWS.md) — save, compare, budget, recheck, decide, recover, and share;
- [Safety guidance](docs/SAFETY.md) — snapshot truth, mutations, personal data, and public sharing;
- [Ready-to-use prompts](examples/PROMPTS.md) — copy-paste requests for common tasks;
- [`grabblist-research` skill](skills/grabblist-research/SKILL.md) — portable agent operating guidance;
- [comparison](skills/grabblist-research/assets/templates/comparison.md), [collection](skills/grabblist-research/assets/templates/collection-brief.md), and [decision](skills/grabblist-research/assets/templates/decision-record.md) templates.

The skill is a Markdown playbook, not an executable plugin. Connect the hosted MCP separately; no credentials are bundled.

## Authentication

Grabblist supports OAuth 2.0 Authorization Code with PKCE and Dynamic Client Registration.

| Scope | Access |
|---|---|
| `grabblist:read` | Connectivity and read-only item, collection, graph, and history tools |
| `grabblist:write` | Item and collection mutations, links, sharing controls, and feedback |
| Both scopes | `ask_agent` |

Authentication is required for tool calls. The authenticated user identity comes from the verified connection, not from tool input.

## Data behavior

Most tools only read or write records in the connected user's Grabblist account. Two user-initiated operations can contact another service:

1. `add_item` may request public page metadata when an image is omitted.
2. `ask_agent` sends the request and relevant account context to the AI provider configured by that user.

There is no continuous background page monitoring. Saved prices and metadata are snapshots unless the user or agent explicitly updates them.

## Public service links

- **Website:** https://grabbitapp.com
- **Documentation:** https://grabbitapp.com/docs/mcp
- **Privacy:** https://grabbitapp.com/privacy
- **Terms:** https://grabbitapp.com/terms
- **Support:** https://grabbitapp.com/contact
- **Official Registry name:** `com.grabbitapp/grabblist`
- **Glama Connector:** https://glama.ai/mcp/connectors/com.grabbitapp/grabblist

## Repository boundary

This is the public integration repository for the hosted Grabblist MCP service. It contains:

- public connection metadata;
- the human-readable tool and authorization contract;
- client configuration examples;
- public security and disclosure guidance.

It intentionally does **not** contain the Grabblist web application, service implementation, database code, deployment configuration, production credentials, or user data. Those are not required to connect an MCP client to the hosted service.

## Security

Read [SECURITY.md](SECURITY.md) before reporting a vulnerability. Never include access tokens, authorization codes, cookies, API keys, or personal saved-item data in a report.

## Status

The live service and official MCP Registry currently identify the server as **Grabblist 2.1.0**.
