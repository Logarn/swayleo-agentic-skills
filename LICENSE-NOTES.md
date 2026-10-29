# Source and licence notes

This repository is a mixed-source collection, not a blanket relicensing of vendor material.

## Swayleo workflows

The files prefixed swayleo- and the corresponding skills/ folders are newly authored generalized workflows. Some recover procedures from prior work; each skill states its provenance. A public repository does not itself establish an open-source licence for all contents.

## Bundled existing skills

The vendor source packages in the downloadable archive retain their existing licences and notices:

| Package | Snapshot | Declared licence | Source |
| --- | --- | --- | --- |
| Google Drive | 0.1.22 | MIT | https://github.com/openai/plugins |
| Documents | 26.1017.22136 | MIT | Local OpenAI runtime package; metadata identifies https://github.com/openai/openai |
| PDF | 26.1017.22136 | MIT | Local OpenAI runtime package; metadata identifies https://github.com/openai/openai |
| Presentations | 26.1017.22136 | MIT | Local OpenAI runtime package; metadata identifies https://github.com/openai/openai |
| Spreadsheets | 26.1017.22136 | MIT | Local OpenAI runtime package; metadata identifies https://github.com/openai/openai |
| Vercel | 0.54.1 | Apache-2.0 | https://github.com/vercel/vercel-plugin |

The runtime source-repository metadata does not establish that those exact paths or versions are publicly accessible. The actual bundled source is the local dated snapshot. Each package includes SOURCE.json, and the archive manifest records file hashes. Existing in-file and third-party notices are preserved. Vercel's Apache licence text and copyright notice are included.

## Catalogue-only capabilities

Package manifests marked Proprietary, UNLICENSED or without a declared redistribution licence are not bundled merely because they are installed locally. They remain visible in the catalogue with their setup route. Install the official plugin under its terms.

Tool availability, service access and authorization remain separate from instruction-file licensing.

## Added external collection

The external source folders retain the original notices from Corey Haines, Rebecca Rae Barton, Email Love, Kinga Dow and magnus919 under MIT. Rob Palmer's five copywriting skills are distributed under CC BY 4.0, with credit to **Rob Palmer — https://robpalmer.com/blog/claude-code-copywriting-skills** and a link to https://creativecommons.org/licenses/by/4.0/.

No author endorsement is implied. Original source folders are unmodified; reading previews add an attribution/setup header and rewrite relative Markdown links to the pinned upstream revision. Source provenance and exact hashes are in external-manifest.json. Original licences accompany the packages and are copied by the optional installer. Kinga Dow's separately licensed example-brand image assets are excluded.
