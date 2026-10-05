# Response plan — BIO260405 Maximize provisional award

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
| Ratings | #0 Fair, #1 Good, #2 Good |

The panel is not asking us to redo the science. It is asking for a defensible
resource argument, a biological rationale, and a consistency fix on funding.
The provisional 6 months of Stampede3 time is essentially one FastGA pilot's
worth of compute — the right scale to produce the evidence the reviewers said
was missing, under our **own** allocation rather than the Galaxy gateway one.

## 2. What the renewal package must contain

- Revised Main Document, Code Performance & Scaling, CV, References, Special
  Requirements (same page limits).
- An **"Addressing Reviewer Comments"** document, structured reviewer-by-reviewer.
- A **timeline of milestones** (asked by Review #2).
- A **research-team section** — roles, duties, time dedication (asked by Review #2).
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
| 1.1 | "unclear the biological imperative or impacts" | Add a biological rationale: what reference-free vertebrate alignment enables, questions addressed, impact on genomics | Main §1/§2; Abstract |
| 1.2 | "no publications or grants associated with the work" | Cite work products and the supporting grant; state manuscripts in preparation if any exist | References; Main funding section |
| 1.3 | "project seems associated with Galaxy… can't judge why this work is important" | Sharpen the separation: this work is independent of the Galaxy platform justification; state exactly what each allocation covers | Main §7 |
| 1.4 | "why all 4,467 NCBI chromosome-level assemblies" | Move the clade-balanced selection rationale up front, before the number | Main §1/§5.1.1 |

### Review #2 (Good)

| # | Comment | Action | Lands in |
| ---: | --- | --- | --- |
| 2.1 | "sections fail to exactly match application guidelines" | Reorder Main Document to the ACCESS section order | Main Document |
| 2.2 | "research team could be better elaborated — organization, duties, time dedication" | Add a team table: PI, co-PIs, roles, % effort | Main §new |
| 2.3 | "not supported by grants, no relevant manuscripts" | Same fix as 1.2 | References; Main |
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
   says it "shouldn't be difficult to provide justification" — do it in one
   strong paragraph plus objective sentences.
5. **Galaxy separation (1.3).** Make the independence of this allocation from
   the Galaxy gateway explicit and quantitative.
6. **Team, timeline, contingency, section order (2.1, 2.2, 2.4, 2.5).**
   Mechanical fixes; low risk, do them all.

## 5. The provisional award is the answer to Review #0

The strongest available response is the pilot we can now run **independently of
Galaxy**, on our own allocation:

- The pilot basis is measured and clean: 336,980 ordered pairs, FastGA **88,546
  node-hours** (0.263 node-h/pair), 331,119 node-hours total, 5.6% unrecoverable,
  ~94% effective utilization.
- 100,000 node-hours is roughly one such pilot — enough to align a new
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
| 2026-10 → 2026-11 | Run tranche under provisional award; capture per-node/per-thread + checkpoint measurements |
| 2026-11 → 2026-12-15 | Thread-scaling study; write "Addressing Reviewer Comments"; revise Main/Perf/Special Requirements |
| 2026-12-15 → 2027-01-31 | Submit renewal with interim results |
| 2027-01 → 2027-03-31 | Complete provisional-award tranche; carry results into renewal |

## 7. Open decisions / TODOs

- [ ] Which grants are cited, and are they active at submission? (TODO: confirm
      NSF 2118709 dates; identify NIH award(s) shown in the biosketch.)
- [ ] Co-PIs vs. collaborators: do Cao and/or Guarracino become co-PIs with
      stated effort? (Affects CV count and team section.)
- [ ] Reduction target for the contingency (currently ~175,000 SUs / 17.5%).
      (TODO: recompute from measured variance.)
- [ ] Exact job/chunk plan and restart-cost figures for the tranche.
      (TODO: extract from the next pilot; do not project.)
- [ ] Whether any manuscript is in preparation to cite (else state none).
- [ ] Reorder Main Document to ACCESS section order without losing content.
