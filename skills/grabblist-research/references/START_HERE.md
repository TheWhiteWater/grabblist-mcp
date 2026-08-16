# Start here

## Connection check

1. Confirm the MCP endpoint is `https://mcp.grabbitapp.com/api/mcp`.
2. Call `ping`.
3. Confirm tool discovery returns 23 tools.
4. Determine whether the connection has read, write, or both scopes before planning mutations.

## Before every save

- Is the source URL public HTTP(S)?
- Is the title exact?
- Is the numeric price actually visible?
- Is the currency explicit?
- Is the platform correctly identified?
- Are optional details evidence-backed?
- Does a matching item already exist?

## Before every comparison

- Are variants, condition, quantity, currency, shipping, and seller comparable?
- Which facts are stored snapshots?
- Which facts were checked now?
- What evidence is missing?
- Does the user want notes/status changed, or only a report?

## Before every destructive or public action

- Restate the target and number of affected records.
- Explain whether deletion is recoverable.
- Explain what public sharing exposes.
- Obtain confirmation when intent is not explicit.
- Record a concise reason.

## Response discipline

Return:

1. what was read;
2. what was changed;
3. what was not changed;
4. snapshot/current-data caveats;
5. unresolved evidence gaps;
6. the next user decision, if one is required.
