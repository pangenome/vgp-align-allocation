# ACCESS-CI allocation requests — VGP all-to-all whole-genome alignment

PI: Erik Garrison, University of Tennessee Health Science Center.

Working repo for the ACCESS-CI (formerly XSEDE) Maximize request **BIO260405**,
*All-to-all whole-genome alignment across the vertebrate tree*, and for the
appeal and renewal that follow it.

## Status

BIO260405 was submitted in the June 15 – July 31, 2026 window, asking 1,000,000
Stampede3 SUs. On 2026-09-16 the AARC returned a **provisional award**: 6 months,
2026-10-01 → 2027-03-31, 100,000 Stampede3 node hours.

- **Appeal of the reduced allocation: due 2026-10-14.** Draft in
  [`reviews/2026-08-maximize-BIO260405/appeal.md`](reviews/2026-08-maximize-BIO260405/appeal.md).
- **Renewal with "Addressing Reviewer Comments": 2026-12-15 → 2027-01-31.**
  Plan in
  [`reviews/2026-08-maximize-BIO260405/response-plan.md`](reviews/2026-08-maximize-BIO260405/response-plan.md).

## Documents

`alignment-2026/` holds the submitted drafts.

| Document | File | Page limit | Required? |
| --- | --- | --- | --- |
| Main Document | [`main.md`](alignment-2026/main.md) | 10 | Yes |
| Code Performance & Resource Costs | [`perf.md`](alignment-2026/perf.md) | 5 | Yes |
| Curriculum Vitae | [`cv/erik-garrison.md`](alignment-2026/cv/erik-garrison.md) | 2 | Yes |
| References | [`references.md`](alignment-2026/references.md) | none | Optional |
| Special Requirements | [`special-requirements.md`](alignment-2026/special-requirements.md) | 1 | Optional |
| Abstract | [`abstract.md`](alignment-2026/abstract.md) | n/a | Yes (form field) |

[`CHECKLIST.md`](alignment-2026/CHECKLIST.md) tracks the submission steps, and
[`PORTAL-ANSWERS.md`](alignment-2026/PORTAL-ANSWERS.md) holds the field-by-field
portal answers.

## `reviews/`

One directory per reviewed request.

```
reviews/2026-08-maximize-BIO260405/
  award-and-review.md            verbatim award notice + reviewer comments
  appeal.md                      draft appeal of the reduced allocation
  response-plan.md               plan for "Addressing Reviewer Comments" / renewal
  missing-citation-vgp-phase1.md VGP Phase I preprint found after submission
```

`award-and-review.md` is interned verbatim from the ACCESS email. Do not edit the
quoted text.

## `notes/`

| Path | Contents |
| --- | --- |
| `notes/alignment/` | NCBI vertebrate survey, the frozen 800-accession tranche manifest and audit, Stampede3 usage data, and the scripts and JSON/TSV data behind them |
| `notes/access-rules-2026.md` | Researched ACCESS rules, each claim sourced |
| `notes/2026-cycle-requirements.md` | Maximize window dates and required documents |
| `notes/resource-landscape.md` | Allocated-resource inventory and capacities |

Stampede3 job accounting for the completed pilot is in
`notes/alignment/usage-data-stampede3.md`.

## Typesetting

Markdown → HTML (pandoc) → PDF (headless Chrome). No LaTeX. Sources stay plain
Markdown so they diff cleanly in git, and all layout lives in one stylesheet.

```
./build.sh                    # build the documents, draft notes visible
./build.sh --final            # strip draft notes — the submission build
./build.sh main perf          # build only named docs
```

`build.sh` takes its document set from the `SRC` variable, which defaults to
`alignment-2026`. PDFs and intermediate HTML land in `build/` (git-ignored).

**Pipeline.** `pandoc --from gfm-tex_math_dollars --to html5 --standalone -c
../access.css`, then a Python pass over the HTML, then Chrome
`--headless=new --print-to-pdf`. The `-tex_math_dollars` flag is mandatory:
without it pandoc reads `$` amounts as math and mangles them.

**Styling** is [`access.css`](access.css): US Letter, 1 in margins, 10 pt Arial
at 1.18 line height (≤ 6 lines/inch), justified body, booktabs tables at 7.5 pt
with no vertical rules. ACCESS does not publish typographic requirements as
strict as NSF PAPPG, but the page limits are hard, so the conservative settings
carry over.

**Draft notes.** Any paragraph opening with `[TODO` and any blockquote containing
`REVIEW NOTE` renders as an orange **DRAFT NOTE** box in a normal build, and is
deleted outright by `--final`. This keeps open questions visible in the review
PDF while guaranteeing they cannot reach a submitted one. Check before sending:

```
./build.sh --final && strings build/*.pdf | grep -c 'DRAFT NOTE'   # must be 0
```

**Page limits are enforced by the build.** Each document's limit is declared in
`build.sh`; exceeding it prints `** OVER the N-page limit **` and exits nonzero,
so it fails loudly rather than at submission time.

**Figures** are inlined as vector SVG. Drop `.svg` files in `assets/` and
reference them as `![](../assets/name.svg)` — the build splices the SVG source
into the HTML so the PDF carries true vector art at any zoom. There is no
`assets/` directory yet.

Requires `pandoc` and Chrome. `build.sh` looks for Chrome at the standard macOS
and Linux paths and honors `CHROME=/path/to/browser` if set.

## Writing style

Prose follows the scientific-manuscript conventions recorded in
[`CLAUDE.md`](CLAUDE.md): active voice, first-person plural, concrete numbers
stated plainly, tool names in backticks, Vancouver citations `[1]`, each
abbreviation defined once.

## Layout

```
alignment-2026/     BIO260405 drafts and submission material
reviews/            award notice, reviewer comments, appeal, response plan
notes/              working research notes and data
  alignment/        NCBI survey, tranche manifest, Stampede3 usage data
build.sh            typesetting pipeline
access.css          stylesheet
CLAUDE.md           working notes and repo rules
```

## Source material

- VGP Phase I preprint: Formenti et al., bioRxiv 2026,
  doi:10.64898/2026.06.24.732306. Supplies the biological rationale and reports
  the pilot counts. Notes in
  [`reviews/2026-08-maximize-BIO260405/missing-citation-vgp-phase1.md`](reviews/2026-08-maximize-BIO260405/missing-citation-vgp-phase1.md).
- NCBI vertebrate assembly survey and the clade-balanced tranche of 800
  accessions: `notes/alignment/`.
- Stampede3 job accounting for the completed pilot:
  `notes/alignment/usage-data-stampede3.md`.

## Origin

This repository began as a copy of Anton Nekrutenko's ACCESS-CI allocation
repository. That repository's earlier drafts and submission history are still
present as `galaxy-2026/` and `archive/`, exported verbatim from Google Drive.
They are prior material and are not part of this request.
