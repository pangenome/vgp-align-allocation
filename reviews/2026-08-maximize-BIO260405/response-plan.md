# Response plan: BIO260405 Maximize provisional award

Plan for the **"Addressing Reviewer Comments"** document and the December 15,
2026 – January 31, 2027 renewal submission. See
[`award-and-review.md`](award-and-review.md) for the verbatim review.

## 1. Where we stand

| Item | Value |
| --- | --- |
| Requested | 1,000,000 Stampede3 SUs |
| Awarded | 100,000 node-hours, provisional, 6 months (2026-10-01 → 2027-03-31) |
| Renewal window | 2026-12-15 → 2027-01-31 |
| Path to full award | Address reviewer comments in a "renewal"; full 12-month award and full SU request then eligible |
| **Interim option** | **Appeal of the reduced allocation, due 2026-10-14** (four weeks from 2026-09-16 notification). See [`appeal.md`](appeal.md) |
| Ratings | #0 Fair, #1 Good, #2 Good |

The panel is not asking us to redo the science. It is asking for a defensible
resource argument, a biological rationale, and a consistency fix on funding.
The provisional 6 months of Stampede3 time is essentially one FastGA pilot's
worth of compute, the right scale to produce the evidence the reviewers said
was missing, under our **own** allocation rather than the Galaxy gateway one.

## 2. What the renewal package must contain

- Revised Main Document, Code Performance & Scaling, CV, References, Special
  Requirements (same page limits).
- An **"Addressing Reviewer Comments"** document, structured reviewer-by-reviewer.
- A **timeline of milestones** (asked by Review #2).
- A **research-team section**: roles, duties, time dedication (asked by Review #2).
- A **funding/grants statement consistent with the biosketch and the portal**
  (asked by Review #0 and #1).
- Renewal, not new request: interim results from the provisional award must be
  reported.

## 3. Reviewer comment → action map

### Review #0 (Fair)

| # | Comment | Action | Lands in |
| ---: | --- | --- | --- |
| 0.1 | "no funding support in the main proposal document… biosketch shows NSF and NIH" | Add an explicit funding statement matching the biosketch and portal; reconcile NSF 2118709 and any NIH award | Main Document §7 / new "Supporting grants" |
| 0.2 | "does not show any usage of computational resource" | Lead the use-history with node-hours, jobs, nodes, and outcome breakdown; make it unmissable | Main §2.1; Perf §2 |
| 0.3 | "parallel use of nodes [not clear]" | Add per-task thread counts, nodes per job, concurrent tasks per node, and a thread-scaling curve for at least one representative step (1/2/4/8/16/32/48 threads) | Perf §new; Main §8 |
| 0.4 | "any reason to run calculations on SPR queue?" | State the queue rationale plainly: SPR is the fastest-turnaround queue in our measured data (median wait 0.0 h vs SKX 17.1 h), and SPR is used only as the conservative billing rate | Main §1/§5.1; Perf §6 |
| 0.5 | "how many calculations/jobs will be submitted" | Give an explicit job plan for the tranche: tasks per job, chunk size, expected submissions/rounds | Main §5.1; Perf §2 |
| 0.6 | "checkpoint to restart if it exceeds 48 hours?" | Document the checkpoint/resume mechanism and its granularity; quantify restart cost in node-hours and calendar terms | Main §2.2; Perf §2 |
| 0.7 | "time loss for restarting… how good are the checkpoint files" | Measure and report reworked node-hours, checkpoint write/read volume, and validated resume correctness | Perf §2 (new measurement) |
| 0.8 | "unclear… 'a longer queue is available we would use it'" | Name the specific queue(s)/walltime needed, or drop the phrasing and rest on the concurrency accommodation | Special Requirements §2 |
| 0.9 | "efficiency of using the requested time not clearly convinced" | Add a node-utilization / effective-core figure and the scaling curve from 0.3 | Perf §3, §new |

### Review #1 (Good)

| # | Comment | Action | Lands in |
| ---: | --- | --- | --- |
| 1.1 | "unclear the biological imperative or impacts" | Add a biological rationale: what reference-free vertebrate alignment enables, questions addressed, impact on genomics. The **VGP Phase I preprint** already states the impacts (ancestor reconstruction, sex-chromosome evolution, 3D architecture, methylation, IUCN risk); see [`missing-citation-vgp-phase1.md`](missing-citation-vgp-phase1.md) | Main §1/§2; Abstract |
| 1.2 | "no publications or grants associated with the work" | Cite the **VGP Phase I preprint** (co-authored by Garrison, Cao, Guarracino) and the supporting grant; state manuscript status | References; Main funding section |
| 1.3 | "project seems associated with Galaxy… can't judge why this work is important" | Sharpen the separation: this work is independent of the Galaxy platform justification; state exactly what each allocation covers | Main §7 |
| 1.4 | "why all 4,467 NCBI chromosome-level assemblies" | Move the clade-balanced selection rationale up front, before the number | Main §1/§5.1.1 |

### Review #2 (Good)

| # | Comment | Action | Lands in |
| ---: | --- | --- | --- |
| 2.1 | "sections fail to exactly match application guidelines" | Reorder Main Document to the ACCESS section order | Main Document |
| 2.2 | "research team could be better elaborated — organization, duties, time dedication" | Add a team table: PI, co-PIs, roles, % effort | Main §new |
| 2.3 | "not supported by grants, no relevant manuscripts" | Same fix as 1.2; the Phase I preprint addresses the "no manuscripts" half directly | References; Main |
| 2.4 | "the 17% contingency request may be too much" | Reduce or itemize the ~175,000-SU contingency; tie each piece to a measured quantity | Main §1/§5.1; Perf §3 |
| 2.5 | "a timeline of milestones would be useful" | Add a milestone/timeline table aligned to the award period | Main §new |

## 4. Cross-cutting workstreams

1. **Funding consistency (0.1, 1.2, 2.3).** One authoritative statement, checked
   against the CV and the portal before submission. Decide which awards are
   cited and whether NSF 2118709 is active at submission.
2. **Parallelism and efficiency evidence (0.2, 0.3, 0.6–0.9).** The reviewers
   read the completed 336,980-pair campaign as if no parallelism were
   demonstrated. Produce the thread-scaling study and the node-utilization
   figures; report jobs, nodes, threads, and outcome breakdown explicitly.
3. **Queue strategy (0.4, 0.8).** Replace "a longer queue if available" with the
   measured queue behavior (SPR 0.0 h median, SKX 17.1 h median / 100.5 h p90)
   and a concrete request.
4. **Biological rationale (1.1).** Add the "why" before the "how". Review #1
   says it "shouldn't be difficult to provide justification"; do it in one
   strong paragraph plus objective sentences.
5. **Galaxy separation (1.3).** Make the independence of this allocation from
   the Galaxy gateway explicit and quantitative.
6. **Recover the missing citation (1.1, 1.2, 2.3).** The VGP Phase I preprint
   (Formenti et al. 2026, bioRxiv doi:10.64898/2026.06.24.732306) should have
   been cited. It is co-authored by the team and directly supplies the
   biological rationale. Details and reconciliation TODOs in
   [`missing-citation-vgp-phase1.md`](missing-citation-vgp-phase1.md).
6. **Team, timeline, contingency, section order (2.1, 2.2, 2.4, 2.5).**
   Mechanical fixes; low risk, do them all.

## 5. The provisional award is the answer to Review #0

The strongest available response is the pilot we can now run **independently of
Galaxy**, on our own allocation:

- The pilot basis is measured and clean: 336,980 ordered pairs, FastGA **88,546
  node-hours** (0.263 node-h/pair), 331,119 node-hours total, 5.6% unrecoverable,
  ~94% effective utilization.
- 100,000 node-hours is roughly one such pilot, enough to align a new
  clade-balanced tranche and, critically, to emit **job-level, per-node,
  per-thread accounting** that the original submission could not separate out
  (the 63,254 node-hours under generic chunk names).
- This simultaneously answers #0's parallelism/checkpoint objections, #1's
  Galaxy confusion, and #2's call for interim milestones.

Frame the renewal as: *"we used the provisional award to reproduce the pilot
throughput on new assemblies under our own allocation, with the parallel and
checkpoint accounting the reviewers requested; here are the measurements."*

## 6. Timeline

| Window | Milestone |
| --- | --- |
| **by 2026-10-14** | **Submit Appeal of the reduced allocation** (see [`appeal.md`](appeal.md)) |
| 2026-10 | Appeal reviewed (~2-week response); provisional award begins |
| 2026-10 → 2026-11 | Run tranche under provisional award; capture per-node/per-thread + checkpoint measurements |
| 2026-11 → 2026-12-15 | Thread-scaling study; write "Addressing Reviewer Comments"; revise Main/Perf/Special Requirements; add VGP Phase I preprint and reconcile pilot counts |
| 2026-12-15 → 2027-01-31 | Submit renewal with interim results |
| 2027-01 → 2027-03-31 | Complete provisional-award tranche; carry results into renewal |

## 7. Corrections applied 2026-10-05

Done while preparing the appeal:

- **CV** (`alignment-2026/cv/erik-garrison.md`): removed the Qatari grant;
  corrected R01HG013017 to **Multiple PI, 2023–2028**; added U01HG013760,
  U41HG010972, R01HG013618; U01DA057530 dates 2023–2028.
- **References** (`alignment-2026/references.md`): added the VGP Phase I
  preprint as reference 15.
- **Appeal** (`appeal.md`): added an explicit **acknowledgment** that the
  submitted documents under-presented the measured usage data (several figures
  were in the working notes and not carried into the reviewed documents), and
  supplied the job-family and per-partition usage tables.

## 8. Open decisions / TODOs

- [x] Which grants are cited; corrected statement applied (R01HG013017 anchor).
- [x] Grants: R01HG013017 confirmed **Multiple PI, 2023–2028** (user,
      2026-10-05).
- [x] Co-PIs vs. collaborators: **Cao and Guarracino do not become co-PIs**
      (user, 2026-10-05). List them as collaborators with roles in the team
      section; no co-PI CVs required.
- [ ] Reduction target for the contingency (currently ~175,000 SUs / 17.5%).
      (TODO: recompute from measured variance.)
- [ ] Exact job/chunk plan and restart-cost figures for the tranche.
      (TODO: extract from the next pilot; do not project.)
- [ ] Whether any manuscript is in preparation to cite (else state none).
- [x] Add and cite the VGP Phase I preprint; reconcile pilot counts (566 + 13
      + 2 haplotypes = 581; confirm against Supplementary Table 11).
- [ ] Reorder Main Document to ACCESS section order without losing content.
- [x] Commitments softened: parallelism/scaling logging and contingency
      itemization are deferred to the renewal, not promised in the appeal.
