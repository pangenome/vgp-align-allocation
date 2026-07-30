# ACCESS-CI Allocation Requests — Galaxy Gateway

Working repo for ACCESS-CI (formerly XSEDE) allocation requests for the Galaxy
science gateway (<https://usegalaxy.org>). Migrated from Google Drive
(`Allocations` folder) in July 2026.

PI: Anton Nekrutenko (Penn State). Co-PIs: Michael Schatz (JHU), Nate Coraor
(Penn State), Enis Afgan (JHU), Philip Blood (PSC).

## Current cycle: 2026/27 renewal

**Submission window: June 15 – July 31, 2026. Awards start October 1, 2026.**

Drafts live in [`galaxy-2026/`](galaxy-2026/).

| Document | File | Page limit | Required? |
| --- | --- | --- | --- |
| Main Document | [`galaxy-2026/main.md`](galaxy-2026/main.md) | 10 | Yes |
| Progress Report | [`galaxy-2026/progress.md`](galaxy-2026/progress.md) | 3 | Renewals only |
| Code Performance & Resource Costs | [`galaxy-2026/perf.md`](galaxy-2026/perf.md) | 5 | Yes |
| Curriculum Vitae | `galaxy-2026/cv/` | 2 per person | Yes, per PI/co-PI |
| References | [`galaxy-2026/references.md`](galaxy-2026/references.md) | none | Optional |
| Special Requirements | [`galaxy-2026/special-requirements.md`](galaxy-2026/special-requirements.md) | 1 | Optional |
| Abstract | [`galaxy-2026/abstract.md`](galaxy-2026/abstract.md) | n/a | Yes (form field) |

Review criteria: Appropriateness of Methodology, Appropriateness of Research
Plan, Efficient Use of Resources.

Submit at <https://allocations.access-ci.org/>.

## Typesetting

Same mechanism as `~/git/writing/grants/NSF-26-509`: **Markdown → HTML (pandoc)
→ PDF (headless Chrome)**. No LaTeX. Sources stay plain Markdown so they
diff cleanly in git, and all layout lives in one stylesheet.

```
./build.sh                    # build all docs, draft notes visible
./build.sh --final            # strip draft notes — the submission build
./build.sh main progress      # build only named docs
```

PDFs and intermediate HTML land in `build/` (git-ignored).

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

Requires `pandoc` and Google Chrome at the standard macOS path.

## Writing style

Prose follows the house style in
[`~/git/writing/grants/SKILL.md`](file:///Users/anton/git/writing/grants/SKILL.md)
and its parent `~/git/writing/SKILL.md`. Load those before editing. The rules
that bite most often here: **no semicolons in body prose** (period, em-dash, or
comma instead — reference entries and table cells are exempt), em-dashes are
authentic and should be kept, first-person plural throughout, claims stated flat
with concrete numbers, and the banned-word list in §3 (`leverage`, `barrier`,
`foster`, `substrate`, mechanical `Moreover`/`Furthermore`, and the rest).

## Layout

```
galaxy-2026/        current cycle drafts
archive/            previous cycles, exported verbatim from Google Drive
  galaxy/           the usegalaxy.org gateway award
    2023/  2024/  2025/  supplements/
notes/              research notes, usage data, resource landscape
assets/             figures
```

## History

Galaxy has been supported by an XSEDE/ACCESS-CI allocation since 2015. Prior
requests are archived by year; each cycle consists of a Main document, a
Progress Report, a Performance and Scaling report, and an Abstract. Mid-cycle
supplement requests (Jetstream2, Ranch) are in `archive/galaxy/supplements/`.

## Source material

- Usage dashboard: <http://lookerstudio.google.com/reporting/8cfee054-2ddd-4711-af5a-a7a8d62076bb/page/nrqdD>
- Publication library: <https://www.zotero.org/groups/1732893/galaxy/items/L5WWHAIU/library>
- Original Drive folder: <https://drive.google.com/drive/u/0/folders/1RX2rta5zhr46mCC2tt-qdlcnQQust4iG>
