# Security Policy

## Reporting

Report suspected vulnerabilities through the private contact route at:

https://grabbitapp.com/contact

Do not open a public GitHub issue for a security vulnerability.

Never include access tokens, authorization codes, refresh tokens, cookies, API keys, reviewer credentials, or personal saved-item data. Provide reproduction steps with synthetic or redacted identifiers.

## Public trust boundary

- Canonical MCP resource: `https://mcp.grabbitapp.com/api/mcp`
- OAuth issuer: `https://grabbitapp.com`
- Authentication: OAuth 2.0 Authorization Code with PKCE
- Registered scopes: `grabblist:read` and `grabblist:write`

Send Grabblist credentials only to the canonical service and issuer. Do not paste a shared Bearer token into a public directory, issue, configuration example, screenshot, or log.

## User-data isolation

The authenticated account identity is established by the verified connection and is not accepted from MCP tool input. Item, collection, relationship, and history operations are scoped to that account. Nonexistent and cross-account identifiers return the same sanitized not-found behavior.

## External processing

Most tools only access the connected account's Grabblist records. Two explicit, user-initiated exceptions are:

1. `add_item` may request metadata from a public HTTP(S) page when an image is omitted.
2. `ask_agent` sends the request and relevant context to the AI provider configured by that user.

Grabblist does not continuously monitor saved pages in the background.

## Repository scope

This repository contains public integration metadata and documentation, not the hosted service implementation or production configuration. Security reports should target the live service behavior rather than assuming this repository is a deployable backend.
