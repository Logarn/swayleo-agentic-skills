# What this library actually contains

Audit date: October 29, 2026.

## Correction to the first version

The first nine files were newly written starter workflows from an operations agenda. They were not an inventory or export of the existing Codex skills. They were too brief to represent the available capability. The current version replaces those short files and broadens the library.

## Coverage

- **166 existing skill entrypoints** were found in the local plugin cache, primary runtime packages and system skill directory.
- **117 were classified as relevant** to lifecycle, creative, operations, analytics, deliverables or building. Specialist/optional and out-of-core skills remain visible in the catalogue, with their classification.
- **43 existing vendor skills** are bundled with their package resources. Their package manifests declare MIT or Apache-2.0 licences. The archive retains references, scripts and assets rather than extracting only the main Markdown.
- **23 Swayleo workflows** now include input requirements, a process, deliverable schema, example, completion checks and a supporting output worksheet. These include expanded starters, workflows recovered from past work and clearly identified new gap-fillers.

The authoritative inventory is [inventory.json](inventory.json). [CATALOG.md](CATALOG.md) is its readable version. Counts describe this dated local snapshot, not all skills ever published or every tool available to every teammate.

## Historical practices recovered

The audit checked local strategy instructions, template-update notes and QA-review notes, plus selected recent turns from operations, strategy, project-management and brand chats. Reusable practices included:

- Email / Job / Lead / Support / Proof / Close strategy maps.
- Detailed briefs immediately above matching copy sections.
- Native copy tables, template fidelity and blank writing-cell preservation.
- Current client overrides taking precedence within their own scope.
- Claim/footnote, offer, product-image and destination QA.
- Comment identity, anchors and in-place edits.
- Internal/client version reconciliation and concurrent-edit protection.
- Approval gates, active revisions versus held work and original deadline preservation.
- Tracker batch consolidation with retained source history.
- Actual board schemas, recurrence rules and automation test evidence.
- Complete design review coverage, including plain-text variants.

These are generalized procedures. No client files, quotes, private document links, account IDs, contact details, prices, offers, transcripts or chat dumps are included.

## Distribution and dependency limits

Proprietary and undeclared-licence plugins are catalogued for installation from their official source; their instruction files are not redistributed. This includes capabilities such as Data Analytics, Figma and Customer.io where applicable to this snapshot. A catalogue entry is not a working installation.

The archive's vendor snapshots preserve package layout and source versions. They are reference/source packages, not a claim that copying them installs connectors, hosted services, credentials or a compatible runtime. Prefer the official plugin installation for vendor capabilities.

The installer defaults to the 23 Swayleo workflow folders and preserves their worksheets. External skills require an explicit --external selection. It previews changes by default and never overwrites an existing skill. Root Markdown files are readable previews; the archive contains the proper SKILL.md folder layout.

## What is not verified

- Not every past cloud chat or cloud filesystem was inspected. The historical review was selected, not an exhaustive recovery of all previous turns.
- Files present in the local cache are not necessarily active or callable in this chat.
- No dedicated Klaviyo skill file was found in the scanned directories. Prior Klaviyo work informs workflow guidance, not an assertion of a portable connector.
- Some earlier work referenced external copywriting skills without installing them. They are not counted as installed skills here.
- Swayleo workflows have structural and packaging validation. They have not all been behavior-tested against live accounts. No campaign, flow or automation was activated for this audit.

## Maintaining completeness

Re-run the source inventory when Codex plugins change. Compare skill IDs, versions and hashes, review newly found capabilities for relevance, and preserve licence/dependency boundaries. Keep source exports distinct from original Swayleo instructions. New detail should encode a real decision, useful schema or verified procedure rather than padding the files.

## External expansion

After the local audit, 48 external skills were added from seven public source repositories. These are not counted among the 166 local entries. They cover direct-response copy, email/SMS and lifecycle strategy, marketing/sales, Klaviyo analysis and development, Figma email design, Klaviyo personalization, and project/program management. See EXTERNAL-SKILLS.md and external-manifest.json for pinned source commits, authors, licences and prerequisites.

The archive now includes 23 Swayleo + 43 local vendor + 48 external skill entrypoints. Original external SKILL.md files are hash-checked against downloaded source. References/templates are retained. The installer was exercised in a task-local scratch directory; external workflow scripts were not run and no service account was connected.

The system's quick_validate.py could not run because PyYAML is absent. The Swayleo files instead passed checks of their deliberately simple frontmatter subset, names, descriptions, required resources and packaging. Do not interpret those checks, static source inspection or upstream test claims as certification of live workflow behavior.
