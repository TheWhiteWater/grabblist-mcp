---
name: grabblist-research
description: Use Grabblist MCP as durable, user-controlled memory for web finds. Save evidence-backed snapshots, organize collections, compare alternatives, record decisions, and handle destructive or public-sharing actions safely.
---

# Grabblist research

## Use this skill when

- the user wants to save a product, service, rental, course, event, listing, or other web find;
- research should persist across conversations;
- saved candidates need comparison, grouping, budgets, relationships, or decision status;
- stored prices need an explicit manual recheck;
- the user wants to review history, recover an item, or share a collection.

## Core model

Grabblist stores **static snapshots**. It does not continuously monitor pages. External search, browsing, and current-price verification are separate agent responsibilities; save the resulting evidence only when the source supports it.

## Operating rules

1. Search before saving to reduce accidental duplicates.
2. Never invent required `add_item` fields; ask or research when title, price, currency, URL, or platform is unknown.
3. Omit unsupported optional fields instead of guessing.
4. Distinguish stored snapshot facts from current external evidence.
5. Compare exact variants, currency, condition, quantity, seller, shipping, and tax treatment.
6. Use relationships deliberately: `alternative`, `complement`, `upgrade`, `duplicate`, or `same_seller`.
7. Change decision status only from user intent.
8. Confirm destructive operations and public collection sharing when intent is ambiguous.
9. Use short, factual `reason` fields where supported.
10. Do not put credentials or unnecessary personal data into notes, tags, attributes, feedback, or reasons.

## Preferred sequence

### Save

1. Inspect the source.
2. Call `search_saved` for likely existing matches.
3. Call `add_item` with evidence-backed fields.
4. Report omitted fields and snapshot limitations.

### Compare

1. Call `search_saved` and `get_item`.
2. Call `get_item_graph` for existing relationships.
3. Gather current evidence externally when requested.
4. Store concise notes with `update_item`.
5. Link alternatives with `link_items` after identity is clear.
6. Use the comparison template in `assets/templates/comparison.md`.

### Organize

1. Clarify goal, budget, currency, and constraints.
2. Call `create_collection`.
3. Add owned items with `add_to_collection`.
4. Re-read with `list_collections` and report totals and gaps.
5. Pin only user-approved top picks.

### Decide

Use `update_item` to move through:

```text
considering → shortlisted → decided → bought
                               └──────→ rejected
```

Do not infer purchase from checkout activity. Use `assets/templates/decision-record.md`.

## Safety-critical tools

- `delete_item`: soft-deletes items; verify exact IDs and count.
- `delete_collection`: deletes the collection but not its items.
- `unlink_items`: removes only a relationship.
- `update_collection(is_public=true)`: creates public access; require explicit confirmation.
- batch `update_item`: applies the same supplied fields to every selected item.
- `ask_agent`: requires both scopes and uses the AI provider configured by the user.

## References

- Start with [`references/START_HERE.md`](references/START_HERE.md).
- Full workflows: [`../../docs/WORKFLOWS.md`](../../docs/WORKFLOWS.md).
- Safety guidance: [`../../docs/SAFETY.md`](../../docs/SAFETY.md).
- Tool inventory: [`../../TOOLS.md`](../../TOOLS.md).
