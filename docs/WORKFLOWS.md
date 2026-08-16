# Agent workflows

These workflows separate external research from durable Grabblist storage. The agent or another connected research tool obtains current public evidence; Grabblist stores user-approved snapshots, notes, relationships, and decisions.

## 1. Save without fabricating fields

1. Inspect the public source.
2. Extract title, numeric price, currency, URL, and platform.
3. Include optional fields only when the source supports them.
4. Call `add_item`.
5. Report omitted or uncertain fields to the user.

Never infer a discount, seller rating, condition, or original price without evidence.

## 2. Compare alternatives

1. Use `search_saved` to find existing candidates before creating duplicates.
2. Use `get_item` for full stored snapshots.
3. If needed, collect current external evidence separately.
4. Store concise provenance-aware notes with `update_item`.
5. Link candidates with `link_items(relation="alternative")`.
6. Use `get_item_graph` to present the final comparison set.
7. Update decision status only when the user states a preference.

Use [the comparison template](../skills/grabblist-research/assets/templates/comparison.md) for the response.

## 3. Build a collection under budget

1. Clarify the goal, budget, currency, required categories, and exclusions.
2. Call `create_collection` with the budget.
3. Research and save candidates as static snapshots.
4. Add owned items with `add_to_collection`.
5. Call `list_collections(id=...)` after each meaningful batch.
6. Report total value, remaining budget, missing components, and incompatible assumptions.
7. Pin one to three user-approved top picks with `set_pinned_items`.

Use [the collection brief](../skills/grabblist-research/assets/templates/collection-brief.md).

## 4. Record a price recheck

1. Find the item with `search_saved` and read it with `get_item`.
2. Obtain a current public price outside Grabblist.
3. Check currency, seller, condition, quantity, shipping treatment, and variant before comparing.
4. Call `update_price` with `source="ai_check"` and a short reason.
5. Explain that this is a manual correction, not continuous tracking.

Do not overwrite a stored price merely because a search snippet shows a different variant.

## 5. Move through a decision

Use the status progression only when supported by the user's intent:

```text
considering → shortlisted → decided → bought
                               └──────→ rejected
```

- `considering`: saved for evaluation.
- `shortlisted`: user has narrowed the field.
- `decided`: user chose an option but has not confirmed purchase.
- `bought`: user confirms acquisition.
- `rejected`: user explicitly removes it from consideration.

Use `update_item` and include a short reason. Do not mark an item bought based on browsing or checkout activity alone.

## 6. Recover or remove data safely

- `delete_item` is a soft delete; use `restore_item` to recover it.
- `delete_collection` removes the collection but leaves its items in Grabblist.
- `unlink_items` removes a relationship, not either item.
- Tools belonging to other MCP servers are outside Grabblist and must not be used as substitutes.

Confirm destructive intent and restate the exact target before calling a destructive tool.

## 7. Share a collection

1. Find the collection with `list_collections`.
2. Explain that `is_public=true` creates public access to the collection.
3. Obtain explicit user confirmation.
4. Call `update_collection` with only the intended fields.
5. Return the resulting public URL.

Never enable sharing merely because the user asks to “send” or “show” a collection; clarify whether they want a summary in chat or a public link.
