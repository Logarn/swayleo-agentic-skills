---
name: swayleo-monday-slack-sync
description: Specify a reliable Monday.com and Slack tracker synchronization with clear ownership.
---

# Monday Slack Sync

## Purpose and provenance

Expanded from the proposed dual-system operations process.

This workflow applies across brands by substituting the current brand's sources, account, scope and approval rules. It is a reusable instruction set, not evidence that a live system is configured.

## Inputs

Real board schema, Slack tracking type, current records, tool capabilities, source-of-truth decision, owner mapping and required update frequency.

If an input is unavailable, identify its effect and continue work that does not depend on it. Do not fill factual gaps with another brand's assumptions.

## Workflow

1. Identify whether Slack tracking uses Lists, messages, a canvas or an integration. Read/write capabilities differ; inspect the available API rather than assuming Slack Lists can be edited.
2. Map canonical task identity and each field: title, client, owner, status, due date and document links. Define field ownership and allowed direction before claiming two-way sync.
3. Use immutable cross-system IDs. Matching only by campaign title or date is insufficient for variants, renamed tasks and replacement batches.
4. Specify triggers, event payloads, idempotency keys, change provenance and loop prevention. Store last successful version/checkpoint so replay does not create duplicates.
5. Define conflicts: newer explicit instructions may change a task's current state, while historical dates and previous decisions remain auditable. Do not let a stale Start ASAP row override a later hold.
6. Define handling of missing owners, unmapped statuses, timezones, partial failures, retries and deletion/archive. A failed Slack update must not be reported as a successful two-system sync.
7. Pilot an authorized small set across create, rename, due-date change, completion, hold and replay. Verify both records after the round trip.
8. If a system is read-only with current tools, provide the exact pending manual change and record the limitation. Do not maintain an invisible third record pretending the systems agree.

## Deliverable

Field mapping; authority/conflict matrix; event flow; exception queue; pilot cases; live versus proposed components; sync status with IDs and failed fields.

Use the output worksheet inside the downloadable library ZIP to structure a working draft. Adapt it to the requested deliverable; do not create extra files unless useful.

## Example

Monday has a later approved hold while Slack says Start ASAP. Preserve the latest authoritative decision and surface the Slack correction rather than auto-releasing the task.

## Verification and completion

IDs prevent duplicates; field ownership is explicit; loops/retries are tested; status/date semantics match; unsupported writes remain visible.

Report what was completed, the source or saved record that proves it, and any unresolved blocker. Distinguish a draft, a saved change and a live action. Publishing, posting, scheduling or changing live systems requires the corresponding user request and available tools.
