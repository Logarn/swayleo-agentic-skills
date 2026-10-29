---
name: swayleo-flow-build-qa
description: Verify lifecycle flow settings and content against a strategy before activation.
---

# Flow Build Qa

## Purpose and provenance

Recovered from flow-settings verification work; no historical live settings are treated as verified defaults.

This workflow applies across brands by substituting the current brand's sources, account, scope and approval rules. It is a reusable instruction set, not evidence that a live system is configured.

## Inputs

Approved map; correct ESP account; actual event/property schema; flow revision; test profiles/events; consent and suppression requirements.

If an input is unavailable, identify its effect and continue work that does not depend on it. Do not fill factual gaps with another brand's assumptions.

## Workflow

1. Verify the active brand/account and flow identity before reading settings. Absence from recent accounts does not prove lack of access.
2. Read the actual trigger, trigger filters, profile filters, conditional splits, delays, re-entry and exit rules. Record literal settings and any evaluation-time semantics.
3. Check whether purchase-type routing uses an event property that exists. Distinguish subscription status from the selected purchase type.
4. Compare branch order, time delays and message counts with the approved map. Check purchasers, unconsented profiles and other excluded people exit as intended.
5. Test representative cases including missing properties, both purchase types, a purchase after entry, repeat entry and suppressed recipients. Use the platform's test/preview tools without contacting real recipients unless authorized.
6. Validate dynamic products, checkout return links, alternative-product destinations, personalization fallbacks and plain-text versions.
7. Record observed behavior and unresolved technical checks. A browser failure is not proof of an account-permission rejection or a failed flow rule.
8. Do not activate or change live settings merely because QA is requested. Report release blockers and approval status distinctly.

## Deliverable

Settings comparison; test matrix with expected/observed behavior; evidence links; blockers; activation state.

Use the output worksheet inside the downloadable library ZIP to structure a working draft. Adapt it to the requested deliverable; do not create extra files unless useful.

## Example

A profile subscribed last month may start a one-time checkout today. Test the checkout property rather than branching solely on subscriber status.

## Verification and completion

Correct account; settings read directly; negative cases covered; consent/exit logic checked; uncertain checks remain unverified; no accidental activation.

Report what was completed, the source or saved record that proves it, and any unresolved blocker. Distinguish a draft, a saved change and a live action. Publishing, posting, scheduling or changing live systems requires the corresponding user request and available tools.
