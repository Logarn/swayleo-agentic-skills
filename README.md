<div align="center">

# SWAYLEO
### Agentic Skills

**A shared toolkit for better work across every brand.**

Retention · Lifecycle · Copy · Design · Automation · Operations

[Install](#get-started) · [Find a workflow](#swayleo-workflows) · [External skills](EXTERNAL-SKILLS.md) · [Plugin catalogue](CATALOG.md)

---
</div>

Swayleo Agentic Skills is the team's shared library of instructions, workflows and resources for working with AI agents. Use it to plan campaigns, write and review copy, design emails, manage projects, build automations and document how we work.

Whether you're joining Swayleo or taking on a new responsibility, start with the skills that fit your role. Bring the current brand brief, approved sources and relevant account access to each task.

## Get started

### Ask your agent to help you install

Copy this into your agent:

```text
Review https://github.com/Logarn/swayleo-agentic-skills.
Download and inspect swayleo-skill-library.zip, then read its README.md.
Help me choose skills for my role and install them in the supported skill
directory, preserving their references, resources and licence notices.
Preview changes before copying files and do not overwrite existing skills.
Use EXTERNAL-SKILLS.md for external skill choices and prerequisites.
Tell me which plugins or account connections my chosen workflows need.
```

### Install with Python

1. [Download the library](https://github.com/Logarn/swayleo-agentic-skills/raw/refs/heads/main/swayleo-skill-library.zip) and extract it.
2. Open a terminal in the extracted folder.
3. Preview the installation, then apply it:

```bash
python install.py
python install.py --apply
```

By default, this installs the Swayleo workflow folders, including their worksheets, into `~/.codex/skills/`. Existing skills are skipped. Python is required; the installer has no additional package dependencies.

To choose one workflow:

```bash
python install.py --skill swayleo-flow-strategy --apply
```

To choose an external skill:

```bash
python install.py --external rob-palmer/direct-response-copy
python install.py --external rebecca/klaviyo-analyst --apply
```

Use `--external all` to preview the full external collection. Add `--destination /your/skills/path` to use another supported skill directory. The [external guide](EXTERNAL-SKILLS.md) lists the available source/skill IDs.

The installer copies instructions and resources. Connect services such as Klaviyo, Figma, Google Drive, Monday.com and Slack separately, using the access your role requires. Other agents may use a different skill location or installation method.

## Choose a starting point

| Your work | Start with |
| :-- | :-- |
| Account management & client onboarding | Brand Context, Client Onboarding, Client Folder, Approval Handoffs |
| Retention & lifecycle strategy | Segmentation Strategy, Flow Strategy, Campaign Calendar, Retention Reporting |
| Copywriting | Lifecycle Copy, Copy Document Structure, Copy Claims QA; external direct-response and copy-review skills |
| Email design | Email Design QA, Campaign Design QA; external Figma design and Email Love workflows |
| Building & implementation | Campaign Build QA, Flow Build QA; external Klaviyo development and personalization skills |
| Operations & project management | Call to Tasks, Operations Call, Task Batch Consolidation, Monday Board Automation |
| Marketing & sales | External customer research, offers, marketing planning, RevOps and sales enablement |

## How to use a skill

Tell your agent which skill to use, what you're trying to produce and which sources it should follow. Include the brand, scope, relevant links or files, and any deadline or approval requirements.

For example:

> Use Campaign Calendar to plan next month's emails from this intake. Give each campaign a clear audience, objective and angle. Flag anything that needs confirmation.

> Use Lifecycle Copy to draft this welcome email. Follow the brand voice, approved offer and product evidence in the brief.

> Use Call to Tasks on this transcript and my notes. Check existing tasks first and flag missing owners or unclear deadlines.

Start with the workflow that fits the job. Add specialist skills when needed, and review the result against the current brand sources before handing it over.

## What's in the library

| Collection | What it contains | Where to look |
| :-- | :-- | :-- |
| Swayleo workflows | Agency processes for strategy, production, QA, operations and team knowledge | Workflow links below; `skills/` in the download |
| External skills | Specialist copywriting, marketing, lifecycle, Klaviyo, Figma and project-management guidance | [External guide](EXTERNAL-SKILLS.md); `external/` in the download |
| Vendor source packages | Document, spreadsheet, presentation, PDF, Drive and development resources | `vendor/` in the download |
| Plugin catalogue | Additional capabilities and their installation requirements | [Catalogue](CATALOG.md) |

Each Swayleo workflow includes inputs, steps, an output format, an example, verification checks and a worksheet. Files linked on GitHub are reading previews; the download preserves the full skill-folder structure and supporting resources.

Vendor packages may depend on official plugins and runtimes. Use their supported installation route to enable tools. Source files alone do not provide a working service connection.

## Swayleo workflows



### Retention & lifecycle

| Skill | What it helps you do |
| :-- | :-- |
| [Brand Context](swayleo-brand-context.md) | Build a sourced brand context pack before strategy, copy or operations work. |
| [Segmentation Strategy](swayleo-segmentation-strategy.md) | Audit existing audiences and define a measurable lifecycle segmentation plan. |
| [Flow Strategy](swayleo-flow-strategy.md) | Build flow maps and email strategy using the established Swayleo review structure. |
| [Lifecycle Copy](swayleo-lifecycle-copy.md) | Write and revise email/SMS copy from brand evidence and an approved strategy. |
| [Flow Build QA](swayleo-flow-build-qa.md) | Verify lifecycle flow settings and content against a strategy before activation. |
| [Retention Reporting](swayleo-retention-reporting.md) | Produce a sourced lifecycle performance readout with clear metric definitions. |

### Campaign production

| Skill | What it helps you do |
| :-- | :-- |
| [Campaign Calendar](swayleo-campaign-calendar.md) | Create campaign calendars with sourced offers, defined audiences and matching briefs. |
| [Copy Document Structure](swayleo-copy-document-structure.md) | Prepare native copy-document sections and preserve approved writing-table formats. |
| [Copy Claims QA](swayleo-copy-claims-qa.md) | Review lifecycle copy for product accuracy, offer mechanics, claims and policy limits. |
| [Email Design QA](swayleo-email-design-qa.md) | Prepare design direction and review rendered lifecycle emails against approved copy. |
| [Campaign Design QA](swayleo-campaign-design-qa.md) | Run complete campaign design QA and draft comments tied to exact frames. |
| [Campaign Build QA](swayleo-campaign-build-qa.md) | Verify a built campaign against its approved copy, design, audience and send plan. |

### Operations & automation

| Skill | What it helps you do |
| :-- | :-- |
| [Client Onboarding](swayleo-client-onboarding.md) | Turn a new client brief into a verified operations and lifecycle readiness plan. |
| [Client Folder](swayleo-client-folder.md) | Set up or audit the core client document set without carrying old-brand residue. |
| [Call to Tasks](swayleo-call-to-tasks.md) | Convert call transcripts and after-call notes into sourced, deduplicated tasks. |
| [Operations Call](swayleo-operations-call.md) | Build a concise recurring operations agenda with urgent leadership decisions first. |
| [Approval Handoffs](swayleo-approval-handoffs.md) | Keep strategy, copy, design and build handoffs aligned with actual approvals. |
| [Monday Slack Sync](swayleo-monday-slack-sync.md) | Specify a reliable Monday.com and Slack tracker synchronization with clear ownership. |
| [Monday Board Automation](swayleo-monday-board-automation.md) | Audit or implement board workflows using the real Monday.com schema and testable rules. |
| [Task Batch Consolidation](swayleo-task-batch-consolidation.md) | Consolidate campaign tasks into batches while retaining original history and references. |

### Review & team knowledge

| Skill | What it helps you do |
| :-- | :-- |
| [Document Reconciliation](swayleo-document-reconciliation.md) | Reconcile internal and client documents while preserving comments and source authority. |
| [Qa Comments](swayleo-qa-comments.md) | Write, revise and verify short actionable QA comments without duplicating threads. |
| [Academy Resource](swayleo-academy-resource.md) | Curate external learning and turn verified internal workflows into reusable training. |


## Specialist skills

The [external collection](EXTERNAL-SKILLS.md) includes:

- **Copywriting:** direct-response copy, ads, landing pages, editing and copy review.
- **Lifecycle & marketing:** email sequences, SMS, customer research, offers, retention and experimentation.
- **Klaviyo:** account auditing, segmentation, development and Django personalization.
- **Email design:** brand-component workflows, Figma building, template repair, migration and design QA.
- **Marketing & sales:** positioning, marketing plans, prospecting, RevOps and sales enablement.
- **Project management:** delivery planning, program coordination, Kanban and meetings.

Each entry identifies its author, source, licence and prerequisites. Some workflows are designed around a particular platform or design system; choose the one that matches the team's setup.

## Working across brands

Reuse the process while checking the facts for each brand. Products, claims, offers, audiences, event fields, voice and approval requirements must come from that brand's current sources.

Follow current Swayleo SOPs and the task's agreed scope. If a skill contains an outdated assumption or conflicts with the brief, flag it before proceeding. Suggested benchmarks, cadences and examples are starting points to evaluate.

Review and approval remain part of the workflow. A completed draft or passing QA check does not authorize a send, activation, publication or change to a live account. Keep client data and credentials out of this public repository.

## Keep the library useful

When a repeated task becomes easier or more reliable, capture the improvement in the relevant skill. Include when it applies, the inputs it needs, the decisions that matter, the expected output and how to check it.

Preserve supporting files and source credits when updating external material. Keep Swayleo procedures separate from vendor instructions, and review platform-specific guidance when tools change.

For source versions, coverage and validation limits, see [the audit notes](AUDIT.md), [external sources](external-manifest.json) and [licence notes](LICENSE-NOTES.md).

---

<div align="center">

**Better work, with less repeated work.**

Swayleo · A shared agency playbook

</div>
