# ACCESS-CI allocation requests — VGP alignment and Galaxy gateway

Working repo for ACCESS-CI (formerly XSEDE) allocation requests, migrated from
Google Drive (the `Allocations` folder) in July 2026. Public at
<https://github.com/pangenome/vgp-align-allocation>.

Two request lines live here:

| Line | PI | Drafts | Archive |
| --- | --- | --- | --- |
| VGP all-to-all whole-genome alignment | Erik Garrison (UTHSC) | [`alignment-2026/`](alignment-2026/) | none yet |
| Galaxy science gateway (<https://usegalaxy.org>) | Anton Nekrutenko (Penn State) | [`galaxy-2026/`](galaxy-2026/) | [`archive/galaxy/`](archive/galaxy/) |

Galaxy co-PIs: Michael Schatz (JHU), Nate Coraor (Penn State), Enis Afgan (JHU),
and Philip Blood (PSC).

The two lines are independent requests with separate PIs and separate
allocations. They share only this repo and the submission portal.

## Current activity: BIO260405 appeal and renewal

The VGP alignment line was submitted in the June 15 – July 31, 2026 window as
Maximize request **BIO260405**, *All-to-all whole-genome alignment across the
vertebrate tree*, asking 1,000,000 Stampede3 SUs. On 2026-09-16 the AARC
returned a **provisional award**: 6 months, 2026-10-01 → 2027-03-31, 100,000
Stampede3 node hours.

- **Appeal of the reduced allocation: due 2026-10-14.** Draft in
  [`reviews/2026-08-maximize-BIO260405/appeal.md`](reviews/2026-08-maximize-BIO260405/appeal.md).
- **Renewal with "Addressing Reviewer Comments": 2026-12-15 → 2027-01-31.**
  Plan in
  [`reviews/2026-08-maximize-BIO260405/response-plan.md`](reviews/2026-08-maximize-BIO260405/response-plan.md).

The Galaxy 2026/27 renewal drafts in [`galaxy-2026/`](galaxy-2026/) were prepared
for the same June 15 – July 31, 2026 window. Its
[`CHECKLIST.md`](galaxy-2026/CHECKLIST.md) lists what is still open, including
the mandatory CVs, which are not in this repo.

## Directories

| Path | Contents |
| --- | --- |
| [`alignment-2026/`](alignment-2026/) | BIO260405 drafts and submission material |
| [`galaxy-2026/`](galaxy-2026/) | 2026/27 Galaxy renewal drafts |
| [`reviews/`](reviews/) | Award notifications, reviewer comments, appeals, response plans |
| [`notes/`](notes/) | Working research notes and parsed data |
| [`archive/`](archive/) | Prior Galaxy cycles, exported verbatim from Google Drive |
| [`access.css`](access.css), [`build.sh`](build.sh) | Typesetting |

### `alignment-2026/`

| Document | File | Page limit | Required? |
| --- | --- | --- | --- |
| Main Document | [`main.md`](alignment-2026/main.md) | 10 | Yes |
| Code Performance & Resource Costs | [`perf.md`](alignment-2026/perf.md) | 5 | Yes |
| Curriculum Vitae | [`cv/erik-garrison.md`](alignment-2026/cv/erik-garrison.md) | 2 | Yes |
| References | [`references.md`](alignment-2026/references.md) | none | Optional |
| Special Requirements | [`special-requirements.md`](alignment-2026/special-requirements.md) | 1 | Optional |
| Abstract | [`abstract.md`](alignment-2026/abstract.md) | n/a | Yes (form field) |

Plus [`CHECKLIST.md`](alignment-2026/CHECKLIST.md) and
[`PORTAL-ANSWERS.md`](alignment-2026/PORTAL-ANSWERS.md): portal form answers and
the remaining pre-submit checks.

### `galaxy-2026/`

Same document set as above, with a Progress Report
([`progress.md`](galaxy-2026/progress.md), 3 pages, renewals only) and no CV
directory. The Progress Report is the document reviewers check against the
archived prior years.

### `reviews/`

One directory per request that has been reviewed:

```
reviews/2026-08-maximize-BIO260405/
  award-and-review.md            verbatim award notification + reviewer comments
  appeal.md                      draft appeal of the reduced allocation
  response-plan.md               plan for "Addressing Reviewer Comments" / renewal
  missing-citation-vgp-phase1.md VGP Phase I preprint found after submission
```

`award-and-review.md` is interned verbatim from the ACCESS email. Do not edit
the quoted text.

### `notes/`

| Path | Contents |
| --- | --- |
| `notes/2026-cycle-requirements.md` | Maximize window dates and required documents |
| `notes/access-rules-2026.md` | Researched ACCESS rules, each claim sourced |
| `notes/prior-cycle-issues.md` | Defects in prior submissions, flagged so they are not repeated |
| `notes/request-history.md` | Per-resource requested amounts by year |
| `notes/resource-landscape.md` | Allocated-resource inventory and capacities |
| `notes/usage-data.md` | Galaxy usage figures and their source workbook |
| `notes/data/` | Parsed dumps of the Galaxy usage workbook |
| `notes/alignment/` | VGP alignment line: NCBI vertebrate survey, the frozen 800-accession tranche manifest and audit, Stampede3 usage data, and the scripts and JSON/TSV data behind them |

## Typesetting

Same mechanism as `~/git/writing/grants/NSF-26-509`: **Markdown → HTML (pandoc)
→ PDF (headless Chrome)**. No LaTeX. Sources stay plain Markdown so they diff
cleanly in git, and all layout lives in one stylesheet.

```
./build.sh                    # build all docs, draft notes visible
./build.sh --final            # strip draft notes — the submission build
./build.sh main progress      # build only named docs
```

`build.sh` currently targets the `galaxy-2026/` document set via its `SRC`
variable. Point `SRC` at `alignment-2026/` to build the alignment set. PDFs and
intermediate HTML land in `build/` (git-ignored).

**Pipeline.** `pandoc --from gfm-tex_math_dollars --to html5 --standalone -c
../access.css`, then a Python pass over the HTML, then Chrome
`--headless=new --print-to-pdf`. The `-tex_math_dollars` flag is mandatory:
without it pandoc reads `$` amounts as math and mangles them.

**Styling** is [`access.css`](access.css), adapted from `nsf.css`: US Letter,
1 in margins, 10 pt Arial at 1.18 line height (≤ 6 lines/inch), justified body,
booktabs tables at 7.5 pt with no vertical rules. ACCESS does not publish
typographic requirements as strict as NSF PAPPG, but the page limits are hard,
so the conservative NSF settings carry over.

**Draft notes.** Any paragraph opening with `[TODO` and any blockquote
containing `REVIEW NOTE` renders as an orange **DRAFT NOTE** box in a normal
build, and is deleted outright by `--final`. This keeps open questions visible
in the review PDF while guaranteeing they cannot reach a submitted one. Check
before sending:

```
./build.sh --final && strings build/*.pdf | grep -c 'DRAFT NOTE'   # must be 0
```

**Page limits are enforced by the build.** Each document's limit is declared in
`build.sh`; exceeding it prints `** OVER the N-page limit **` and exits
nonzero, so it fails loudly rather than at submission time.

**Figures** are inlined as vector SVG. Drop `.svg` files in `assets/` and
reference them as `![](../assets/name.svg)` — the build splices the SVG source
into the HTML so the PDF carries true vector art at any zoom.

Requires `pandoc` and Chrome. `build.sh` looks for Chrome at the standard macOS
and Linux paths and honors `CHROME=/path/to/browser` if set.

## Writing style

Prose follows the scientific-manuscript conventions recorded in
[`CLAUDE.md`](CLAUDE.md): active voice, first-person plural, concrete numbers
stated plainly, tool names in backticks, Vancouver citations `[1]`, each
abbreviation defined once. The banned-word list and the no-semicolons rule in
body prose come from the same house style.

## Layout

```
alignment-2026/     VGP all-to-all alignment (BIO260405) drafts
galaxy-2026/        Galaxy gateway 2026/27 renewal drafts
reviews/            award notifications, reviewer comments, appeals, response plans
archive/            previous Galaxy cycles, exported verbatim from Google Drive
  galaxy/           the usegalaxy.org gateway award
    2023/  2024/  2025/  supplements/
notes/              research notes, usage data, resource landscape
  alignment/        VGP alignment survey, tranche manifest, Stampede3 usage data
```

There is no `assets/` directory yet. The build inlines figures from `assets/`
when they exist; create it when a document first needs a figure.

## History

Galaxy has been supported by an XSEDE/ACCESS-CI allocation since 2015. Prior
requests are archived by year; each cycle consists of a Main document, a
Progress Report, a Performance and Scaling report, and an Abstract. Mid-cycle
supplement requests (Jetstream2, Ranch) are in `archive/galaxy/supplements/`.

The VGP alignment line is new for the 2026/27 cycle and has no archive yet.

## Source material

Galaxy gateway:

- Usage dashboard: <http://lookerstudio.google.com/reporting/8cfee054-2ddd-4711-af5a-a7a8d62076bb/page/nrqdD>
- Publication library: <https://www.zotero.org/groups/1732893/galaxy/items/L5WWHAIU/library>
- Original Drive folder: <https://drive.google.com/drive/u/0/folders/1RX2rta5zhr46mCC2tt-qdlcnQQust4iG>

VGP alignment:

- VGP Phase I preprint: Formenti et al., bioRxiv 2026,
  doi:10.64898/2026.06.24.732306 — supplies the biological rationale and reports
  the pilot counts. Archived notes in
  [`reviews/2026-08-maximize-BIO260405/missing-citation-vgp-phase1.md`](reviews/2026-08-maximize-BIO260405/missing-citation-vgp-phase1.md).
- NCBI vertebrate assembly survey and the clade-balanced tranche of 800
  accessions: `notes/alignment/`.
- Stampede3 job accounting for the completed pilot:
  `notes/alignment/usage-data-stampede3.md`.
