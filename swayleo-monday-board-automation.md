---
name: swayleo-monday-board-automation
description: Audit or implement board workflows using the real Monday.com schema and testable rules.
---

# Monday Board Automation

## Purpose and provenance

Recovered from project-management build out, review assignment and recurrence work.

This workflow applies across brands by substituting the current brand's sources, account, scope and approval rules. It is a reusable instruction set, not evidence that a live system is configured.

## Inputs

Workspace/board, column IDs and labels, owner directory, existing automations, workflow requirements, test records and permitted changes.

If an input is unavailable, identify its effect and continue work that does not depend on it. Do not fill factual gaps with another brand's assumptions.

## Workflow

1. Read the board schema, groups, status labels, people/date fields, dependencies and views. Resolve IDs directly; do not hardcode another board's label indexes.
2. Map the production stages and who acts at each transition. Keep waiting for review, revision, ready for design and completion distinguishable.
3. Inspect existing automations before adding another. Identify overlapping triggers and assignment/notification loops.
4. Specify each rule as trigger → conditions → action, with field ownership, recurrence behavior, timezone and exception handling.
5. For due-date cascades, use the current upstream date and documented offsets. Record whether offsets mean working or calendar days. Handle reopened tasks and missing dates without silently shifting history.
6. For review assignment, distinguish artifact owner from reviewer. Confirm person/team IDs and whether assignment should replace or append.
7. Test native automation on a small authorized fixture: normal transition, repeat event, date change, missing owner and reopened task. Record actual run history.
8. Item descriptions, Updates and Workdocs are distinct surfaces. Verify the current API and supported location before using a workaround; an API error does not prove an undocumented initialization requirement.
9. Report configured, tested, activated and unverified states separately. A mocked fixture or source file is not a live automation.

## Deliverable

Board map; automation register; rule specifications; test matrix/run evidence; known limits and proposed next steps.

Use the output worksheet inside the downloadable library ZIP to structure a working draft. Adapt it to the requested deliverable; do not create extra files unless useful.

## Example

Changing the Copy Due date should update dependent deadlines only under the agreed cascade rule, without reassigning the reviewer or erasing the original commitment.

## Verification and completion

Actual schema; no overlapping rules; reviewer mapping correct; recurrence/replay checked; date semantics explicit; activation claims supported.

Report what was completed, the source or saved record that proves it, and any unresolved blocker. Distinguish a draft, a saved change and a live action. Publishing, posting, scheduling or changing live systems requires the corresponding user request and available tools.
