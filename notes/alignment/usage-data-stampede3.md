# Stampede3 usage and cost basis — TG-MCB140147

Source: `sacct -X` records for user shuocao2374, 2025-06-10 to 2026-07-30
(13.7 months), plus `taccinfo` as of 2026-07-31. All jobs charged to
`tg-mcb140147`.

Node core counts derived from the records themselves: SKX 48, ICX 80, SPR 112,
H100 96, nvdimm 80.

**Units caveat.** Everything below is node-hours and core-hours. Stampede3
bills in SUs and per-queue charge multipliers differ. Confirm the multipliers
in the Stampede3 user guide before any figure enters a request.

## 1. Completed milestone

The complete **bidirectional all-versus-all alignment of 581 vertebrate genome
assemblies — 336,980 pairwise alignments — is finished**, computed on
Stampede3. This is the single most useful fact in this document. It is also
the answer to the open question in the Galaxy gateway draft §3.4, which asks
how much of the all-to-all alignment completed during 2025/26.

Execution model: FastGA and wfmash command lines written one per line, split
into chunks sized by the number of jobs that can be queued at once, dispatched
across nodes by pylauncher, with ParaFly managing concurrency within each node.
Jobs run to the 48-hour wall limit, terminate as TIMEOUT, and the next round
re-splits whatever remains. Chunk names (`xaa`, `xab`, …) are **reused across
rounds with different contents**, so they cannot be treated as chains.

## 2. Totals

| Metric | Value |
| --- | ---: |
| Jobs | 3,265 |
| Node-hours | 331,119 |
| Core-hours | 25,050,213 |
| Scratch | 51,684 GB across 45,002,364 files |
| SUs remaining on TG-MCB140147 | 278,717, expiring 2026-09-30 |

By job family:

| Family | Jobs | Node-hours | Core-hours |
| --- | ---: | ---: | ---: |
| wfmash chain | 1,461 | 211,275 | 15,448,852 |
| x* (pylauncher all-vs-all) | 177 | 46,020 | 2,545,068 |
| FastGA chain | 634 | 25,292 | 2,538,558 |
| lastz | 25 | 20,865 | 1,583,995 |
| pylauncher_example | 51 | 17,234 | 1,930,186 |
| pggb | 82 | 1,657 | 181,761 |
| index.sh | 136 | 431 | 48,182 |
| CMA-ES / depth | 5 | 8 | 915 |
| other | 694 | 8,338 | 772,695 |

## 3. Cost per alignment, and a head-to-head aligner comparison

Both FastGA and wfmash produced a complete result set over the same 336,980
alignments. That makes this a measured cost comparison of two aligners on
identical input at full scale — unusually strong material for the
Appropriateness of Methodology criterion.

Attribution is clear for the `wfmash*` and `FastGA_1` job names. The 63,254
node-hours under `x*` and `pylauncher_example` are mixed and still need to be
split:

| If the mixed 63,254 goes to… | FastGA | per aln | wfmash | per aln | wfmash / FastGA |
| --- | ---: | ---: | ---: | ---: | ---: |
| all FastGA | 88,546 | 0.263 | 211,275 | 0.627 | 2.4× |
| half each | 56,919 | 0.169 | 242,902 | 0.721 | 4.3× |
| all wfmash | 25,292 | 0.075 | 274,529 | 0.815 | 10.9× |

**wfmash costs between 2.4× and 10.9× more per alignment than FastGA.** Even
the conservative end supports the tool choice. Splitting the mixed 63,254
sharpens the claim but does not change its direction.

A third family, `lastz`, consumed 20,865 node-hours (0.062 per alignment if it
also ran the full set). Confirm whether this is a third result set.

The three aligner families together account for 320,686 node-hours — 97% of all
Stampede3 consumption.

### Framing note

Running the same all-versus-all twice will read as duplicated work unless the
purpose is stated. The defensible framing is that wfmash serves as the
high-sensitivity reference set against which SweepGA filtering of the faster,
higher-false-positive FastGA output is calibrated, with CMA-ES used to fit the
filter parameters. Written that way, the 211,275 node-hours are the cost of
validating a method that makes the cheap aligner usable at scale. Written any
other way, they look like the same job run twice.

## 4. Quadratic projection

Bidirectional all-versus-all is N(N−1). Using the FastGA-route unit cost of
0.263 node-hours per alignment:

| Genomes | Alignments | vs. today | Node-hours | SKX core-hours |
| ---: | ---: | ---: | ---: | ---: |
| 581 | 336,980 | 1.00× | 88,545 | 4,250,174 |
| 700 | 489,300 | 1.45× | 128,569 | 6,171,316 |
| 850 | 721,650 | 2.14× | 189,622 | 9,101,840 |
| 1,000 | 999,000 | 2.96× | 262,499 | 12,599,928 |
| 1,250 | 1,561,250 | 4.63× | 410,236 | 19,691,329 |
| 1,500 | 2,248,500 | 6.67× | 590,819 | 28,359,298 |
| 2,000 | 3,998,000 | 11.86× | 1,050,520 | 50,424,938 |

This table is the core of the resource-usage plan. It is exactly the form the
ACCESS guidance asks for: a measured per-unit cost multiplied by a justified
number of units.

## 5. The binding constraint is queue concurrency, not SUs

The x* work ran in 11 rounds between 2025-10-28 and 2025-12-03. Chunk counts
per round run 2, 2, 8, 20, 1, 3, 18, 19, 1, 16, 21 — flat, because the split is
sized by how many jobs can be queued at once, not by remaining work.

Three rounds did nearly all the compute (44,439 of 46,020 node-hours). Several
rounds were cancelled without running at all: 19 of 19 on 2025-11-06, 16 of 16
on 2025-11-10, 83 of 86 on 2025-12-03.

Meanwhile 278,717 SUs sit unused and expire 2026-09-30.

Supporting figures: cumulative queue wait across multi-submission jobs is
21,817 job-hours, of which 12,823 on SKX alone. SKX wait is 17.1 h at p50 and
100.5 h at p90.

**This is the Special Requirements argument, and it should be made in terms of
turnaround and concurrency rather than efficiency.** Genuinely unrecoverable
work — NODE_FAIL plus FAILED — is 18,666 node-hours, 5.6% of total. Effective
utilization is roughly 94%.

### Presentation risk

Raw `sacct` and XDMoD summaries show 57% TIMEOUT. A reviewer who does not know
about the checkpoint-and-resubmit model will read that as 57% waste. The Code
Performance document must state the design explicitly and report the 5.6%
unrecoverable figure alongside the raw state breakdown.

## 6. The forward-looking case: Phase II

Index construction is settled and undemanding — it fits inside one SPR node's
128 GB, it chunks, and five sets cost roughly 420 node-hours at N=581, about
0.13% of consumption to date. No large-memory line and no walltime exception
are needed for it.

The request rests instead on aligning VGP Phase II together with Phase I.
Phase I is complete at 816 species; the Phase I comparative analysis was run
across a subset of 579 species, which is the 581 assemblies used here. Phase II
targets a representative of each vertebrate family, variously stated as
approximately 1,000, 1,045, 1,100 or 1,159 species. Pick one figure, cite it,
and use it consistently.

### Incremental alignment, not recomputation

Adding M assemblies to an existing N does not require recomputing N(N−1). The
incremental cost is M(2N + M − 1). Stating this explicitly is a direct answer
to the Efficient Use of Resources criterion — the completed Phase I work is
reused rather than repeated.

| Target N | Total alignments | Incremental | Incremental node-h | Full recompute | Saved | 5-set storage |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 816 | 665,040 | 328,060 | 86,280 | 174,906 | 51% | 99 TB |
| 1,100 | 1,208,900 | 871,920 | 229,315 | 317,941 | 28% | 179 TB |
| 1,400 | 1,958,600 | 1,621,620 | 426,486 | 515,112 | 17% | 290 TB |
| 1,900 | 3,608,100 | 3,271,120 | 860,305 | 948,930 | 9% | 535 TB |

At 0.263 node-hours and 31.1 MB per alignment, measured.

### The pggb figure does not hold up

Downstream work — full-scale pggb, then single-base and block conservation
across the alignment — is where the largest compute lines would sit, and it is
the least measured part of the request.

pggb consumption to date is 1,657 node-hours across 82 jobs, described as
small-scale tests. Ten times that is 16,570 node-hours, which is **7.2% of the
incremental alignment cost at N=1,100 alone**. A pangenome graph campaign over
1,100 vertebrate genomes costing a fourteenth of the pairwise alignment that
feeds it is not a claim a reviewer will accept without evidence, and it is
almost certainly an underestimate of the campaign rather than a real figure.

Note that pggb, unlike indexing, exhibits both constraints that would justify
the harder resource lines: peak RSS reaches 271 GB against a 128 GB node, and
28 of its 82 jobs hit the 48-hour wall. **The large-memory line and any
walltime exception rest on pggb, not on indexing** — but 1,657 node-hours is
too thin a base to extrapolate from.

Conservation analysis, single-base and block, has no measured cost at all.

### The measurement that unblocks the request

Build one pangenome graph end to end at realistic scale — one clade, or a
defined haplotype count — and record node-hours, peak RSS, wall time and output
size against haplotype count and total sequence length. Then run conservation
scoring over that one graph and record the same. Those two curves convert into
per-graph and per-megabase costs, and a stated number of graphs converts those
into the request.

## 6b. Smaller open items

1. **Split the mixed 63,254 node-hours** under `x*` and `pylauncher_example`
   between FastGA and wfmash, to sharpen the aligner cost ratio from a range
   (2.4×–10.9×) to a figure.
2. **Is `lastz` a third result set?** 20,865 node-hours, 25 jobs. Also 48 jobs
   on h100 and 2 on pvc — if GPU alignment was tested, that bears on any
   DeltaAI or GPU line.
3. **SweepGA filtering cost** per parameter set.
4. **Why five sets.** Raw as control, best-match as baseline, two CMA-ES
   candidates, wfmash as reference is defensible but must be stated — it
   multiplies index and storage by five.
5. **Whose S3 bucket**, and measured transfer time for staging 50 TB onto an
   ACCESS filesystem. See §7.
6. **Retention tradeoff.** Regenerating the raw set costs 88,626 node-hours;
   storing it costs 10 TB. State which sets are kept and which are regenerated
   on demand — this is the Efficient Use of Resources criterion answering
   itself.

## 7. Other resources, and the staging argument

The AARC rubric lists **"Proposal describes access to other compute
resources"** as grounds for rejection. Three things must be disclosed plainly
in the Main Document: the GenomeArk S3 bucket, a local L40S GPU server
(lambda01), and the Galaxy gateway allocation TG-MCB140147 under which all the
Stampede3 work to date has run.

The S3 disclosure is clean. GenomeArk is hosted under the AWS Open Data
Program — sponsored public hosting, not an allocated resource under the
group's control, and not adjacent to compute. There is no egress cost to
report and no argument that the group is declining to use storage it already
holds.

### Staging is the storage argument, and it is measured

Pulling the 50 TB working set from S3 onto an ACCESS filesystem takes **10
days**. That is 5 TB/day, roughly 61 MB/s — about one twenty-first of what a
10 Gbps link would deliver, which points at per-object overhead rather than
bandwidth as the limit.

The cost is paid per analysis cycle, not once, because the downstream work
requires the data on a local filesystem:

| Genomes | Working set | Staging time |
| ---: | ---: | ---: |
| 581 | 50 TB | 10 days |
| 700 | 73 TB | 15 days |
| 1,000 | 148 TB | 30 days |
| 1,250 | 232 TB | 46 days |
| 1,500 | 334 TB | 67 days |

At N=1,000, staging the data takes longer than most of the analysis that
follows it. Three downstream cycles at the current size is 30 days of pure
data movement. **This is the storage justification: not capacity, which the
sponsored bucket already provides, but residency next to compute.**

### It points at a specific resource

The Galaxy gateway draft §3.3 describes GenomeArk2 moving VGP data onto
Jetstream2 object storage precisely to get off commercial cloud. If the source
data lands on Jetstream2, then hosting the derived alignment sets on Jetstream2
storage collapses the 10-day staging problem into an intra-facility transfer,
and the request stops being "we need storage" and becomes "these products
belong on the same infrastructure as their sources."

Anticipate one reviewer objection: why not compute directly against object
storage? Because index construction and graph tooling need POSIX random access.
Say so explicitly.

## 8. Not computable from this export

`sacct -X` returned `TotalCPU` as `00:00:00` at the job-allocation level, so
true CPU efficiency cannot be derived here. Re-pull without `-X`, or use
`seff`.
