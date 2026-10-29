---
name: swayleo-call-to-tasks
description: Convert call transcripts and after-call notes into sourced, deduplicated tasks.
---

# Call To Tasks

## Purpose and provenance

Expanded from the operations agenda; proposed process, not a deployed integration.

This workflow applies across brands by substituting the current brand's sources, account, scope and approval rules. It is a reusable instruction set, not evidence that a live system is configured.

## Inputs

Call date and timezone; transcript and after-call notes; client/project; existing task records; owner directory; destination board/list if task creation is requested.

If an input is unavailable, identify its effect and continue work that does not depend on it. Do not fill factual gaps with another brand's assumptions.

## Workflow

1. Read transcript and notes together. Distinguish a decision, an explicit commitment, an idea and an unresolved question. Only commitments become tasks automatically in the draft.
2. Capture the action as a verb plus deliverable. Preserve a short source quote or timestamp and a link. Split unrelated deliverables; keep one deliverable with its acceptance criteria together.
3. Resolve the responsible person from the actual commitment. A speaker, attendee or reviewer is not automatically the owner. Flag missing or conflicting ownership.
4. Explicit client or team deadlines override the default call date +2 days. Record original deadline wording. Resolve relative dates against the call date and timezone, not the processing date. Calendar versus working days is still a team decision; present a provisional date with that assumption visible if needed.
5. Compare client, deliverable, source and existing task IDs to identify matches. Update an existing record only within the user's authorized scope; do not duplicate it because wording differs.
6. Prepare the list on the call day. For late processing, keep the original call date and overdue state. Never backdate completion.
7. If asked to create tasks and tools exist, map fields to the actual schema, create a small clear batch, read back IDs and dates, then report any failed rows. An ambiguous owner or deadline remains an unresolved draft.
8. For automation, define transcript-ready and notes-ready triggers, source revision IDs, duplicate keys, retry behavior and a review queue. A proposed automation is not an activated one.

## Deliverable

Task | Client | Owner | Due date + timezone | Deadline basis | Acceptance criteria | Source | Existing task ID | Action/status. Follow with decisions and questions that did not become tasks.

Use the output worksheet inside the downloadable library ZIP to structure a working draft. Adapt it to the requested deliverable; do not create extra files unless useful.

## Example

“Send the revised brief by Friday” becomes a revised-brief task with Friday's resolved date. “Maybe test SMS” stays an idea unless someone committed to a deliverable.

## Verification and completion

Verify every task against its source; explicit dates beat defaults; unresolved fields are visible; existing-task matches are checked; created records are read back.

Report what was completed, the source or saved record that proves it, and any unresolved blocker. Distinguish a draft, a saved change and a live action. Publishing, posting, scheduling or changing live systems requires the corresponding user request and available tools.
