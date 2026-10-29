---
name: swayleo-campaign-build-qa
description: Verify a built campaign against its approved copy, design, audience and send plan.
---

# Campaign Build Qa

## Purpose and provenance

New execution workflow derived from recurring copy/design/destination review gaps.

This workflow applies across brands by substituting the current brand's sources, account, scope and approval rules. It is a reusable instruction set, not evidence that a live system is configured.

## Inputs

Approved campaign ID/version, correct ESP account, build preview, segment definitions, suppressions, send date/timezone, offer terms and QA recipients.

If an input is unavailable, identify its effect and continue work that does not depend on it. Do not fill factual gaps with another brand's assumptions.

## Workflow

1. Confirm account, campaign identity, audience variant and revision. A copied campaign may retain old sender details, lists, links or tracking.
2. Compare subject, preview, from/reply-to, body, offer, images, disclaimers and plain-text content with the approved artifacts.
3. Inspect actual audience filters, suppressions and estimated counts; compare against the segment definition and frequency plan. Flag count shifts for investigation.
4. Test every CTA/product destination, visible label, offer code and purchase route. Distinguish member/prospect and one-time/subscription destinations.
5. Preview personalization and dynamic blocks with representative profiles and missing values. Check empty recommendations, cart behavior, alt text and unsubscribe/footer requirements.
6. Render desktop/mobile and required email clients with available tooling. A design screenshot does not prove the ESP build renders correctly.
7. Verify send date, timezone, daylight-saving conversion, smart-send settings and any resend exclusion. Check last-minute offer changes.
8. Use authorized test recipients only. QA does not authorize scheduling or sending to the audience. Record all blockers and the current release decision.

## Deliverable

Preflight checklist with evidence; audience and schedule readback; link/dynamic-content tests; unresolved blockers; ready-for-approval versus scheduled/sent state.

Use the output worksheet inside the downloadable library ZIP to structure a working draft. Adapt it to the requested deliverable; do not create extra files unless useful.

## Example

The button says Shop the Kit but its hyperlink points to last month's single-product landing page. Fixing the design label alone does not fix the build.

## Verification and completion

Correct revision/account; audience/exclusions verified; actual links tested; dynamic fallbacks checked; render/schedule verified; send approval separate.

Report what was completed, the source or saved record that proves it, and any unresolved blocker. Distinguish a draft, a saved change and a live action. Publishing, posting, scheduling or changing live systems requires the corresponding user request and available tools.
