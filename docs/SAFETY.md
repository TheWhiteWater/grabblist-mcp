# Agent safety guidance

## Snapshot truth

Grabblist records are static snapshots. Agents must not describe stored prices, availability, ratings, or listing status as current unless they have just checked an authoritative public source.

When presenting stored data, use wording such as:

> Saved at NZD 249 when this snapshot was created; current price not checked.

## Required evidence

Do not fabricate required `add_item` values. If title, price, currency, URL, or platform cannot be established, ask the user or gather better evidence before saving.

Optional fields should be omitted rather than guessed.

## Mutations

Before destructive or externally visible changes:

- identify the exact item or collection;
- explain what will change;
- obtain confirmation when intent is ambiguous;
- include a concise `reason` where the tool supports it.

Pay particular attention to:

- `delete_item` and `delete_collection`;
- `unlink_items`;
- `update_collection(is_public=true)`;
- bulk updates that apply the same fields to multiple items.

## External processing

`add_item` can request public metadata when an image is omitted. `ask_agent` can send the request and relevant account context to the AI provider configured by the user. Use these only when relevant to the user's request.

## Personal data

Avoid placing secrets, payment credentials, account tokens, private addresses, or unnecessary personal information in item notes, attributes, tags, feedback, or reasons.

## Price comparisons

Compare like with like:

- same product variant and quantity;
- same currency;
- same condition;
- shipping and tax treatment made explicit;
- seller identity and marketplace differences disclosed.

A lower sticker price is not necessarily a lower total cost.

## Public sharing

Public collection links can expose item titles, prices, notes intended for sharing, and selection context. Inspect the collection and obtain explicit consent before enabling public sharing.
