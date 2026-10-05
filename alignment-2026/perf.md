# Code Performance and Resource Costs

All figures in this document come from TACC Stampede3 project TG-MCB140147.
The `sacct` window runs from June 10, 2025 through July 30, 2026, crossing the
October 1 allocation renewal. It contains 3,265 jobs and reports 331,119
node-hours and 25,050,213 core-hours across portions of two award periods.
Current-period `taccinfo` shows 221,283 of 500,000 SUs consumed since October 1,
2025. We use the full job window for method performance and current-period
`taccinfo` for award utilization.

## 1. Codes in use

| Code | Role | Parallelism |
| --- | --- | --- |
| FastGA | pairwise whole-genome alignment, production | multithreaded, single node per task |
| wfmash | pairwise alignment, high-sensitivity reference set | multithreaded, single node per task |
| SweepGA | false-positive filtering of FastGA output | multithreaded |
| CMA-ES driver | filter parameter optimization | task-parallel |
| `impg` | indexing and regional queries over the implicit alignment graph | multithreaded within task, task-parallel across loci |
| pylauncher | cross-node task dispatch | distributed |
| ParaFly | within-node concurrency and process management | node-local |

## 2. Execution model and how to read our job accounting

Alignment commands are written one per line and split into chunks sized by the
number of jobs that can be queued at once. pylauncher dispatches tasks across
nodes and ParaFly manages concurrency within each node. A job runs to the
48-hour wall-clock limit, terminates as TIMEOUT, and the next submission
resumes from the recorded completion state. Chunk names are reused across
rounds with different contents.

**A raw reading of our job states is therefore misleading.** Job records show
56.7% of node-hours ending in TIMEOUT, which under this design is the normal
terminal state of an intermediate link in a resumption chain.

| Outcome | Node-hours | Share |
| --- | ---: | ---: |
| TIMEOUT, resumed by next submission | 187,887 | 56.7% |
| COMPLETED | 96,120 | 29.0% |
| CANCELLED | 28,286 | 8.5% |
| NODE_FAIL | 13,613 | 4.1% |
| FAILED | 5,053 | 1.5% |

Work that is genuinely unrecoverable is NODE_FAIL plus FAILED — **18,666
node-hours, 5.6% of total consumption. Effective utilization is approximately
94%.**

Of the 71 named job chains submitted three or more times, 48 reach a COMPLETED
state and account for 291,053 node-hours, 88% of all consumption. The two
largest:

| Chain | Submissions | Node-hours | TIMEOUT | COMPLETED | Span |
| --- | ---: | ---: | ---: | ---: | ---: |
| wfmash | 535 | 208,604 | 72 | 201 | 75 days |
| FastGA | 631 | 25,291 | 37 | 283 | 161 days |

## 3. Pairwise alignment: measured unit cost

Both aligners completed the same workload — all 336,980 ordered pairs among
581 vertebrate assemblies. This gives a direct cost comparison on identical
input at production scale.

| Aligner | Node-hours | Per alignment | Relative |
| --- | ---: | ---: | ---: |
| FastGA | 88,546 | 0.263 node-h | 1.0× |
| wfmash | 211,275 | 0.627 node-h | 2.4× |

The 63,254 node-hours under generic chunk names cannot be separated
retrospectively. We assign all of them to FastGA, maximizing the production
cost and giving the conservative 2.4× ratio. Assigning any share to `wfmash`
only strengthens the method choice.

**Scaling with problem size is analytic and exact.** Directional all-to-all is
N(N−1) independent tasks. Cost scales as N² in both compute and working-output
volume.

For request sizing, we convert the measured FastGA rate of 0.263 node-hours per
pair at the highest standard CPU charge, SPR's 2 SUs per node-hour. This gives a
conservative **0.526 SU per ordered pair** without mixing award periods.

| Milestone | Assemblies | Total pairs | New pairs | Projected alignment SUs | Working output |
| --- | ---: | ---: | ---: | ---: | ---: |
| Completed pilot | 581 | 336,980 | — | measured across two awards | 10 TB/set |
| Requested tranche | approximately 1,381 | 1,905,780 | 1,568,800 | approximately 825,000 | 59 TB/set |
| Phase 1 universe | 4,467 | 19,949,622 | 19,612,642 | not requested now | 620 TB/set |

We request 1,000,000 SUs. The approximately 175,000-SU balance above the
conservative pairwise projection covers input-dependent runtime variation and
bounded rework. `impg` indexing is performed off-allocation or during batch
collation and does not receive a separate compute line.

The 10 TB pilot figure is a per-set working footprint containing intermediates
and indexes. The compressed public production PAF release is approximately 1.5
TB. We retain only that production representation at expanded scale.

**Distribution.** The tasks are independent and carry no inter-task
communication. The workload distributes across arbitrary node counts and across
multiple systems without modification, which is why breadth across resources
is useful to us rather than merely convenient.

## 4. Implicit pangenome analysis with `impg`

`impg` treats the all-to-all PAF collection as an implicit pangenome graph. It
indexes alignment intervals and compact CIGAR deltas, projects a target range
through direct or transitive alignments, and calculates regional similarity or
distance without materializing a whole-genome graph. Per-file index mode allows
new alignment files to be added without rebuilding unchanged indexes.

We have already used `impg` in the public `pangenome/lifetree` workflows. The
incomplete lineage sorting analysis divides the human assembly into 25 kb
windows and executes `impg similarity` across ape homologs with 48 concurrent
tasks. The BUSCO workflow executes `impg query` for each annotated gene and
calculates coverage and fragmentation from the returned PAF records.

Index construction is negligible relative to alignment. Per-file indexes are
built off-allocation or as collation jobs at the end of each genome-versus-all
batch. `impg query` and `impg similarity` operate on independent regions and
parallelize across windows or genes. None of these operations drives the
requested amount.

## 6. Throughput, queue behaviour, and the binding constraint

Our constraint is not aggregate SUs. It is how much work we can hold in flight.

Chunk sizing is set by the number of jobs that can be queued at once rather
than by the work remaining. Across the 2,697 jobs belonging to
multi-submission chains, cumulative queue wait is **21,817 job-hours, of which
12,823 on SKX alone**.

| Partition | Jobs | Median wait | 90th percentile | Maximum |
| --- | ---: | ---: | ---: | ---: |
| skx | 381 | 17.1 h | 100.5 h | 144.4 h |
| icx | 120 | 1.0 h | 61.8 h | 172.3 h |
| spr | 1,728 | 0.0 h | 10.3 h | 158.4 h |
| h100 | 48 | 0.0 h | 2.0 h | 31.7 h |

Under a resumption model each chain link pays this wait again. The pilot
spanned two award periods, and these repeated waits drove its calendar time. The requested tranche contains substantially more
independent work, so higher concurrency is necessary to consume 1M SUs within
the award period.

## 7. Data movement

The five pilot experimental sets and intermediates occupy 51,684 GB across
45,002,364 scratch files. The compressed public production release is
approximately 1.5 TB. For the new campaign, each genome-versus-all batch is
filtered, compressed, indexed, uploaded to GenomeArk, verified, and then
eligible for scratch deletion. This streaming retention policy keeps active
scratch near the demonstrated pilot footprint. We request no ACCESS storage.
