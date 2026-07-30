# Submission checklist — 2026/27 Maximize ACCESS renewal

**Window closes July 31, 2026 — TOMORROW.** Submit at <https://allocations.access-ci.org/>.

Triage, if there is not time for everything: **CVs are mandatory and are not in
this repo at all** — that is a hard blocker on submission rather than a quality
issue, so handle it first (2 pages each, NSF/NIH format, for Nekrutenko, Schatz,
Coraor, Afgan, Blood; the only ones archived are a 2018 Nekrutenko biosketch and
a 2020 Schatz biosketch, both too old to reuse). Figures are likewise absent —
they were embedded images in the Google Docs and did not survive the markdown
export, so re-export them from Drive. After that, the Progress Report's resource
table is the highest-value remaining item, because it is what reviewers check
against prior years.

## Blocking — cannot submit accurately without these

- [ ] **Pull 2025/26 compute usage from XDMoD** (<https://xdmod.access-ci.org>).
      The Drive workbooks stop at June 2025. The period this renewal must report
      on is Oct 2025 – Sep 2026, and there is currently **no data for it at
      all**. Everything in `galaxy-2026/progress.md` §1 depends on this.
- [ ] **Determine whether Bridges-2 and Stampede3 were exhausted or expired.**
      Both show exactly zero for May and June 2025. If exhausted, the Stampede3
      story is saturation and the request should hold; if underutilized, ACCESS
      requires an explanation and mitigation. This flips both the Progress
      Report narrative and the Stampede3 line in the request.
- [ ] **Get awarded amounts for 2025/26** from the allocations portal. The
      workbooks are usage-only, so burn-down against award cannot be computed
      from Drive data.
- [ ] **Jetstream2 Large Memory utilization.** The largest single line in the
      request (12M SU) has no usage tracking anywhere in our accounting.
- [ ] **PI sign-off on the request table** in `main.md` §1. Four lines change
      from last year (Anvil ↑, Bridges-2 ↑, Jetstream2 GPU ↓, Stampede3 ↓).

## Content to refresh

- [ ] Extend user/job statistics from January 2026 through June 2026 (source
      workbook: "User and Job Data ACCESS Allocation Request 2025", the Feb 2026
      refresh — *not* the one named 2026, which is an older copy).
- [ ] Current VGP assembly count. Checkpoints: >150 (Jul 2024), 348 (Jul 2025),
      417 (Oct 2025).
- [ ] Publication counts for 2025 and 2026. Prior: 183 (2024), 322 (2025).
- [ ] Whole-genome alignment: how much of the 477-genome all-to-all completed
      during 2025/26. The 2025 request promised production deployment — this is
      the promise coming due.
- [ ] VGP Phase 1 publication status. A published paper crediting ACCESS is the
      most valuable single item this renewal can carry.
- [ ] Live tool count via `curl usegalaxy.org/api/tools | jq ...` (the workbook
      cell reads 2008 and is years stale; the 2025 report said 6,900).
- [ ] CVMFS reference-data footprint (5.8 TB as of the 2025 report).
- [ ] Current queue-depth limits per resource for `special-requirements.md`.
- [ ] GenomeArk2 actual storage footprint and growth rate — drives the
      Jetstream2 Storage line, which may be requested too low at 500 TB.

## Documents to assemble

- [ ] Main Document — 10 pages. Currently ~5,400 words plus Table 1 and two
      figures. Moving references into their own document frees roughly a page
      and a half versus last year's layout; Table 1 is the next thing to trim
      if it runs long.
- [ ] Progress Report — **3 pages, hard**. Keep the publication list out of it.
- [ ] Code Performance & Resource Costs — 5 pages. Currently the weakest
      document: it needs real KegAlign benchmark timings and a derivation of the
      requested amounts from measured per-unit costs. Reviewers score "Efficient
      Use of Resources" and this is where that is won or lost.
- [ ] CVs — 2 pages each, NSF or NIH format, for Nekrutenko, Schatz, Coraor,
      Afgan, Blood. None are in this repo yet; `archive/` has only a 2018
      Nekrutenko biosketch and a 2020 Schatz biosketch, both too old to reuse.
- [ ] References — no page limit. Expand the Larivière et al. author list.
- [ ] Special Requirements — 1 page, optional but worth including.
- [ ] Figures 1–3 for the Main Document and Figure 1 for the Progress Report.
      Not in this repo; the Drive originals are embedded images in the Google
      Docs and did not survive the markdown export. Re-export from Drive or
      regenerate from the Looker dashboard.

## Consistency pass before submitting

- [ ] **Diff the §1 summary table against the §4.1 justifications line by line.**
      Both the 2023 and 2024 submissions contradicted themselves on this —
      different systems and different amounts in the two places. See
      `notes/prior-cycle-issues.md`.
- [ ] Update `https://galaxyproject.org/projects/vgp` before submitting. It
      currently reads "Last updated January, 2025 with 315 assemblies of 188
      species," which is *lower* than what the proposal will claim, and the
      proposal cites that page.
- [ ] Check every "through the end of June 20XX" date. The 2025 Progress Report
      said June 2024 while presenting data through June 2025.
- [ ] Confirm SU unit conversions per resource. Stampede3 charges node-hours,
      not core-hours; GPU lines use their own multipliers. Our tracking is in
      core-hours.
- [ ] Verify ACCESS Credits exchange rates and any Maximize caps at submission
      time.
