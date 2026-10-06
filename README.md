# ACCESS-CI allocation request — vertebrate all-to-all alignment

Working repository for an ACCESS-CI request to expand a completed all-to-all
alignment of 581 Vertebrate Genomes Project (VGP) assemblies to a
quality-controlled catalogue of publicly available vertebrate reference
genomes.

The completed pilot comprises **336,980 ordered genome pairs** computed on TACC
Stampede3 under `TG-MCB140147`. Its interactive similarity and coverage atlas is
available at <https://unavailable-2374.github.io/vgp-heatmap/>, and the workflow
and related analyses are maintained in
<https://github.com/pangenome/lifetree>.

## Current draft

Drafts live in [`alignment-2026/`](alignment-2026/).

| Document | File | Page limit |
| --- | --- | ---: |
| Main Document | [`alignment-2026/main.md`](alignment-2026/main.md) | 10 |
| Code Performance & Resource Costs | [`alignment-2026/perf.md`](alignment-2026/perf.md) | 5 |
| Curriculum Vitae | [`alignment-2026/cv/erik-garrison.md`](alignment-2026/cv/erik-garrison.md) | 2 |
| References | [`alignment-2026/references.md`](alignment-2026/references.md) | none |
| Special Requirements | [`alignment-2026/special-requirements.md`](alignment-2026/special-requirements.md) | 1 |
| Abstract | [`alignment-2026/abstract.md`](alignment-2026/abstract.md) | portal field |
| Open decisions | [`alignment-2026/CHECKLIST.md`](alignment-2026/CHECKLIST.md) | n/a |

Measured Stampede3 usage and the cost derivation imported from `files.zip` are
kept in [`notes/alignment/usage-data-stampede3.md`](notes/alignment/usage-data-stampede3.md).

A reproducible NCBI survey dated 2026-08-01 found **14,247 current biological
assemblies representing 6,358 vertebrate species** across all assembly levels.
See [`notes/alignment/ncbi-vertebrata-survey-2026-08-01.md`](notes/alignment/ncbi-vertebrata-survey-2026-08-01.md).
The multi-allocation Phase 1 universe is all **4,467 complete and chromosome-
level assemblies representing 1,896 species**. This request asks for **1M
Stampede3 SUs** to add approximately 800 assemblies in the next clade-balanced
tranche. Later awards will complete Phase 1 and admit usable scaffold and contig
assemblies.

## Build

Markdown is converted to HTML with pandoc and printed to PDF with headless
Chrome.

```sh
./build.sh                         # alignment request, draft notes visible
./build.sh --final                 # alignment request, TODO blocks removed
./build.sh main perf               # selected documents
```

PDFs and intermediate HTML are written to `build/`. Page limits are enforced by
`build.sh`. A normal build renders paragraphs beginning with `[TODO` as orange
draft notes. A final build removes them. `SRC` selects the document set and
defaults to `alignment-2026`.

The automated build includes Erik Garrison's two-page CV from
`alignment-2026/cv/`.

## Repository layout

```text
alignment-2026/    current vertebrate alignment request
notes/alignment/   imported measurements and cost basis
access.css         PDF stylesheet
build.sh           Markdown-to-PDF pipeline
```

## Non-negotiable checks

- Do not invent assembly, usage, storage, or service-unit figures.
- Recompute ordered pairs as `N(N−1)` and incremental work beyond 581 as
  `M(2×581 + M−1)`, where `M=N−581`.
- Reconcile the measured 10 TB working set with the approximately 1.5 TB
  compressed public PAF release before finalizing storage.
- Obtain approval to use work charged to `TG-MCB140147` as preliminary results,
  and distinguish past work from the new request.
- Keep all submitted documents within their page limits.

## Origin

This repository began as a copy of Anton Nekrutenko's ACCESS-CI allocation
repository. That repository's earlier drafts and submission history are still
present as `galaxy-2026/` and `archive/`, exported verbatim from Google Drive.
They are prior material and are not part of this request.
