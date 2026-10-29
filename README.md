# Swayleo Agentic Skills

Practical workflows for retention, lifecycle, copy, design, automation and operations.

## What is included

These are **new Swayleo workflow drafts**, written from the operations discussion. They are not copies of installed vendor plugins or a claim that those plugins are portable. No client data, transcripts, credentials or account connections are included.

- **swayleo-call-to-tasks** — Extract same-day tasks from call transcripts and after-call notes.
- **swayleo-operations-call** — Prepare the recurring Monday and Wednesday operations agenda.
- **swayleo-segmentation-strategy** — Audit client audiences and develop a continuing lifecycle segmentation strategy.
- **swayleo-campaign-calendar** — Build campaign calendars with explicit audiences, exclusions and production ownership.
- **swayleo-lifecycle-copy** — Draft lifecycle email and SMS copy from an approved client brief.
- **swayleo-email-design-qa** — Translate lifecycle copy into a design brief and inspect email implementation.
- **swayleo-client-folder** — Audit client folders against the agreed core document structure.
- **swayleo-monday-slack-sync** — Design or review synchronization between Monday.com boards and Slack trackers.
- **swayleo-academy-resource** — Curate internal and external training material for Swayleo Academy.

## Install

Give your agent this instruction:

> Review this repository. Install the Swayleo skill Markdown files I select into separate skill folders, naming each entrypoint SKILL.md. Preserve the YAML frontmatter. Do not overwrite existing skills. Tell me which service connections are missing before attempting actions.

Each swayleo-*.md file is a standalone skill. For Codex, copy its contents to ~/.codex/skills/<skill-name>/SKILL.md. Other agents may use different skill locations. Installing instructions does not install tools or grant account access. Downloading all files does not itself enable automatic discovery.

## Team decisions still open

- Which client segmentation audits come first.
- {Sway} versus {Swayleo} and the final naming structure.
- Whether +2 due dates means calendar or working days.
- Monday.com versus Slack field ownership.
- Whether the client-facing flow map becomes a standard fifth document.

## Existing plugin catalogue

Relevant installed capabilities observed in the originating Codex session:

| Area | Installed skill family | Setup needed |
| --- | --- | --- |
| Lifecycle messaging | Customer.io Journeys, Design Studio, Pipelines, SDK | Customer.io plugin and appropriate workspace access; not Klaviyo support |
| Analysis | Data Analytics: quality, KPI design, reporting, diagnostics, dashboards | Data plugin and source access |
| Design | Figma: design-to-code, diagrams, design libraries | Figma plugin and file access |
| Operations docs | Google Drive, Docs, Sheets, Slides | Google Drive plugin and account access |
| Deliverables | Documents, spreadsheets, presentations, PDF | Relevant runtime and libraries |
| Visuals | Image generation | Supported image generation tools |
| Building and automation | Vercel AI SDK, backend, agents, workflows, Chat SDK | Relevant plugin, runtime and service accounts |

Install those from their official sources in each teammate's environment. Their files have not been redistributed here, and this repository does not replace their dependencies. No dedicated Klaviyo or Monday.com plugin was visible in the inspected skill catalogue.

## Maintenance

Validate each draft against a real, authorized task before adopting it as an SOP. Update the relevant skill when the team agrees a process. Keep client examples and secrets out of this repository.

