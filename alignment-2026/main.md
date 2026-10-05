# All-to-all whole-genome alignment across the vertebrate tree

**Principal Investigator:** Erik Garrison, University of Tennessee Health Science Center

## 1. Summary

We request compute to extend our completed alignment of 581
Vertebrate Genomes Project (VGP) assemblies to a quality-controlled catalogue
of publicly available vertebrate reference genomes. We will align every new
assembly against the completed set and every other new assembly, then use the
result to study genome conservation, structural evolution, and phylogenetic
conflict without choosing a single reference genome or guide tree.

The work is already underway on ACCESS infrastructure. We computed the
complete directional all-to-all alignment of 568 vertebrate assemblies and 13
phylogenetic outgroups — 581 assemblies and 336,980 ordered pairs — on TACC
Stampede3. We publish the initial results as
an interactive similarity and coverage atlas, and we are publishing the
pair-level alignments through GenomeArk. Every unit cost in this request derives from
measured consumption of that completed work.

Our NCBI survey on 2026-08-01 found 14,247 current vertebrate assemblies
representing 6,358 species across all assembly levels. The survey separates
paired GenBank and RefSeq accessions so that the same biological assembly is
not counted twice [12]. It identifies **4,467 complete or chromosome-level
assemblies representing 1,896 species** as the first expansion target.

We request **1,000,000 Stampede3 SUs** for the next clade-balanced tranche.
The production FastGA route costs 0.263 node-hours per ordered pair. To remain
conservative, we size the tranche at the highest standard CPU charge rate,
SPR's 2 SUs per node-hour. Adding approximately 800 assemblies requires
1,568,800 new pairs, 412,594 node-hours, and at most approximately 825,000 SUs.
The remaining approximately 175,000 SUs cover input-dependent runtime
variation and bounded rework. `impg` indexing is a lightweight collation step
performed off-allocation or at the end of each genome-versus-all batch.

| Requested resource | Amount | Basis |
| --- | ---: | --- |
| Stampede3 compute | **1,000,000 SUs** | approximately 825,000 SUs for alignment at the conservative SPR rate plus approximately 175,000 SUs for runtime variance and rework |

The 4,467 complete or chromosome-level assemblies define the multi-allocation
Phase 1 universe, not a claim that this award completes all of it. This award
advances from 581 to approximately 1,381 assemblies. Later requests will
continue through Phase 1 and then admit as many scaffold- and contig-level
assemblies as pass explicit usability checks.

We froze the 800-assembly tranche against the NCBI survey dated August 1,
2026. Of the 581 pilot records, 568 match Vertebrata and 13 are deliberate
tunicate, cephalochordate, echinoderm, or hemichordate outgroups. The tranche
adds 19 orders, 200 families, 779 genera, and 800 vertebrate species. Its exact
accession manifest and reproducible selection script accompany the working
materials.Stampede3 bills node-hours at queue-specific rates: 1 SU on SKX, 1.5 SUs on
ICX, and 2 SUs on SPR [14]. The request and
tranche projection therefore use allocation-level SUs rather than core-hours.

## 2. Background and completed work

### 2.1 What has been done

The VGP aims ultimately to produce high-quality assemblies for all extant
vertebrate species [1]. Our initial catalogue contains 581 VGP-derived
assemblies spanning the major vertebrate clades. It provides a deliberately
high-quality pilot, but it excludes suitable assemblies produced by other
consortia and individual projects. The proposed catalogue expansion turns that
pilot into a broader community resource.

Existing comparative approaches that scale to hundreds of eukaryotic genomes
rely on phylogenetic guide trees. Guide trees bias the analysis of incomplete
lineage sorting, which matters most in clades where rapid radiation obscures
direct phylogenetic inference. To build an unbiased view of vertebrate
evolution we compute a direct all-versus-all alignment instead. The task is
quadratic in the number of assemblies, which is why it requires resources at
this scale.

That alignment is finished. Our `sacct` export covers June 10, 2025 through
July 30, 2026 — 13.7 months spanning the October 1 allocation renewal. It
contains 3,265 job records and reconstructs 331,119 node-hours and 25,050,213
core-hours across portions of two award periods. Current-period `taccinfo`
shows 221,283 of 500,000 SUs consumed since October 1, 2025. These figures are
consistent in scope once the accounting boundary is recognized. We use the
full job window for method performance and current-period `taccinfo` for
award utilization.

### 2.2 Execution model

Alignment commands are written one per line and split into chunks sized by the
number of jobs that can be queued at once. pylauncher distributes tasks across
nodes and ParaFly manages concurrency within each node. Jobs run to the
48-hour wall-clock limit, terminate as TIMEOUT, and the next round re-splits
whatever work remains.

This design has a consequence for how our accounting reads. Raw job records
show 56.7% of node-hours ending in TIMEOUT. Under a checkpoint-and-resume
model TIMEOUT is the normal terminal state of an intermediate link in a chain,
not a failure. Genuinely unrecoverable work — node failures and hard errors —
is 18,666 node-hours, **5.6% of total consumption. Effective utilization is
approximately 94%.**

### 2.3 Method development at high divergence

Vertebrate all-versus-all alignment spans roughly 500 million years of
divergence. This is the regime where aligners break, and both of the aligners
we evaluated broke in it. Results that were correct on demonstration data
proved wrong on distant species pairs, and the problems were visible only after
a complete round had finished. We ran three full rounds with wfmash and two
with FastGA.

The job accounting shows this directly. wfmash consumption falls into three
campaigns — two short pilots in June and July 2025 totalling 1,522 node-hours,
followed by a 97-day production campaign consuming 209,753. FastGA runs across
six campaigns between January and July 2026, the first consuming 17,432
node-hours and each subsequent one smaller.

This is why our downstream design exists. FastGA is fast but produces a high
false-positive rate at these divergences. `wfmash` is far more sensitive and
correspondingly expensive [8,9]. We use the `wfmash` result as the reference
set against which `SweepGA` filtering of the FastGA output is calibrated, with
CMA-ES fitting the filter parameters [11]. The 211,275 node-hours spent on wfmash are the
cost of validating a method that makes the cheaper aligner usable at scale.

### 2.4 Measured aligner comparison

Both aligners produced a complete result set over the same 336,980 alignments.
This gives a cost comparison on identical input at full scale.

| Aligner | Node-hours | Per alignment | Relative |
| --- | ---: | ---: | ---: |
| FastGA | 88,546 | 0.263 node-h | 1.0× |
| wfmash | 211,275 | 0.627 node-h | 2.4× |

The 63,254 node-hours submitted under generic chunk names cannot be separated
between aligners retrospectively. The table assigns all of them to FastGA,
which maximizes the production cost and yields the conservative 2.4× ratio.
Assigning any share to `wfmash` only strengthens the production-method choice.

### 2.5 Public preliminary products

The completed calculation already supports a usable comparative resource. Our
interactive atlas displays weighted-Jaccard similarity and directional genome
coverage for every pair in the 581 × 581 matrix. Users can search by species or
assembly accession and retrieve the underlying directional PAF files through
the GenomeArk data portal [2,3]. The `pangenome/lifetree` repository records the
versioned `wfmash` and `lastz` workflows used in method development, together
with downstream analyses of incomplete lineage sorting and BUSCO gene
alignments [10]. These products demonstrate that the proposed atlas is a
continuation of delivered work rather than a new dissemination plan.

## 3. Research objectives

**O1. Expand the alignment beyond the VGP pilot in taxonomically balanced
tranches.** Phase 1 includes all 4,467 current NCBI complete and chromosome-
level vertebrate assemblies. Subsequent phases admit usable scaffold and contig
assemblies. We will add only ordered pairs involving a newly admitted assembly,
preserving all completed work.

**O2. Build an implicit pangenome with `impg`.** We will index the filtered
all-to-all alignments with `impg`, which treats the alignment network as an
implicit pangenome graph. This avoids materializing a whole-genome graph and
allows transitive projection of a selected locus across thousands of genomes
[13].

**O3. Analyze conservation and phylogenetic conflict by locus.** We will use
`impg query`, `impg similarity`, and partitioned regional analyses to extract
homologous sequence, calculate distance matrices, test incomplete lineage
sorting, and measure BUSCO gene conservation. We have already applied these
workflows to ape loci and VGP BUSCO genes in `pangenome/lifetree` [10].

**O4. Publish a vertebrate alignment atlas.** We will release the assembly
manifest, pairwise PAF files, `impg` indexes, summary matrices, regional
analysis products, and reproducible workflow on public research infrastructure. The existing 581-genome heatmap
and GenomeArk collection demonstrate this delivery path [2,3].

## 4. Efficient use of resources

Three points, each supported by measurement.

**Incremental alignment rather than recomputation.** Adding M assemblies to an
existing N does not require recomputing N(N−1). The incremental cost is
M(2N + M − 1). At the 4,467-assembly Phase 1 target, this avoids recomputing
the 336,980 completed ordered pairs. The saving is modest relative to 19.9
million total pairs, but it is exact and preserves validated results.

**Aligner selection driven by measurement, not preference.** FastGA at 0.263
node-hours per alignment against wfmash at 0.627 is a measured 2.4× difference
on identical input. The filtering framework in §2.3 exists so that the cheaper
aligner can carry the production workload.

**Retention decided against regeneration cost.** We retain the compressed
production alignment set and regenerate experimental raw and filter variants
from bounded validation subsets when needed. This avoids carrying five
quadratically growing working sets.

## 5. Resource usage plan

### 5.1 Incremental alignment

Measured unit cost is 0.263 node-hours per ordered pair, derived from 88,546
node-hours over 336,980 completed alignments.

| Milestone | Assemblies | Total pairs | New pairs | Projected alignment SUs* |
| --- | ---: | ---: | ---: | ---: |
| Completed VGP-derived pilot | 581 | 336,980 | — | measured across two award periods |
| This request: add approximately 800 | approximately 1,381 | 1,905,780 | 1,568,800 | approximately 825,000 |
| Phase 1 universe | 4,467 | 19,949,622 | 19,612,642 | not requested in this award |

\* The projection applies the measured 0.263 node-hours per pair to the SPR
charge rate of 2 SUs per node-hour. This upper standard CPU rate avoids assuming
that all work receives the cheaper SKX or ICX rate. Approximately 175,000 SUs
remain for `impg` analysis and variance.

### 5.1.1 Clade-balanced tranche construction

We will freeze each tranche before execution. Within Phase 1, all 4,467
assemblies are eligible, but their order follows taxonomic novelty rather than
accession date or the density of sequencing in model organisms. We first add an
assembly from every unrepresented class, then order, family, genus, and species.
Within an equally represented clade, we rank assembly level, RefSeq status,
scaffold N50, contig N50, and release date. Additional assemblies from an
already represented species follow assemblies that add a species or deeper
lineage.

After Phase 1, scaffold and contig candidates must have a live NCBI accession,
reported sequence length and contiguity statistics, no suppressed status, and
no duplicate paired GenBank/RefSeq record. We will reject assemblies whose
fragmentation or sequence content prevents FastGA from completing a pilot
alignment. We apply the same farthest-first taxonomic ordering, so every
completed tranche maximizes breadth even if the project ends before all usable
assemblies are included.

For a tranche adding K assemblies to a catalogue of N, the exact workload is
K(2N + K − 1) ordered pairs. We will choose K so the measured FastGA cost fits
the tranche's compute and storage budget.

The contingency is bounded rather than open-ended. The completed pilot already
contains pairs spanning the deepest vertebrate divergences, so most additions
increase sampling density within represented clades rather than extending the
maximum divergence. We will verify that statement against the final manifest.

### 5.2 `impg` indexing

`impg` does not require us to materialize a whole-genome pangenome graph. It
builds reusable interval indexes over the PAF alignment network, stores CIGAR
operations compactly, and resolves a query by projecting ranges through direct
or transitive alignments [13]. Per-file indexing supports incremental rebuilds,
which matches an expanding catalogue because newly added pair files can be
indexed without rebuilding unchanged files.

Indexing is negligible beside alignment. We build per-file indexes during
collation at the end of each genome-versus-all batch, or on local resources
after the compressed PAF files reach GenomeArk. We therefore request no
separate SUs for `impg` indexing.

### 5.3 Regional analysis with `impg`

We have already used `impg` in two analyses committed to
`pangenome/lifetree`. The incomplete lineage sorting workflow divides the
human assembly into 25 kb windows and runs `impg similarity` across ape
homologs with 48 concurrent tasks. A second workflow uses `impg query` to
project BUSCO gene intervals through pairwise PAF files and measures coverage
and fragmentation in the homologous gene region [10].

The expanded analysis will use the same operations. We will query annotated
loci and genome windows, walk transitive alignments where required, calculate
pairwise similarity and distance matrices, and aggregate conservation and
phylogenetic conflict across loci. Each region is independent, so this stage is
task-parallel across windows and genes.

These regional `impg` operations are post-production science analyses rather
than a separately requested compute line. They run locally or use otherwise
idle capacity within the alignment tranche.

### 5.4 Active data and public release

The five pilot experimental sets and their intermediates occupy approximately
50 TB on scratch, while the compressed public production PAF release is
approximately 1.5 TB. We will not retain five full variants at the expanded
scale. Each genome-versus-all batch is filtered, compressed, indexed, uploaded
to the sponsored GenomeArk public bucket, verified, and then eligible for
scratch deletion. Experimental comparisons use bounded subsets.

Scaling the compressed release by ordered-pair count projects approximately
8.5 TB of durable public output after this tranche. This is hosted through the
AWS Open Data Program and is not an ACCESS storage request. Stampede3 scratch
holds only active batches and can remain near the pilot's measured footprint.
We request no ACCESS storage or tape resource.

## 6. Resource appropriateness

**Memory.** Pairwise FastGA tasks run on one node. The existing `impg` regional
workflows also run on one node per task and parallelize across independent
windows or genes. The request uses standard Stampede3 CPU nodes and asks for no
large-memory or GPU resource.

**Concurrency, not aggregate SUs, is our binding constraint.** Chunk sizing is
set by how many jobs can be queued at once, not by how much work remains.
Across multi-submission jobs, cumulative queue wait is 21,817 job-hours, of
which 12,823 on SKX alone, where wait is 17.1 hours at the median and 100.5
hours at the 90th percentile. The pilot spanned portions of two awards, and
repeated queue waits extended its calendar time. Higher concurrency is
necessary to consume the larger tranche within the award period.

## 7. Access to other computational resources

We hold no allocated storage or compute outside ACCESS beyond the following.

**AWS S3.** Source assemblies and durable public outputs reside in the
GenomeArk bucket, hosted under the AWS Open Data Program. This is sponsored
public hosting, not an allocated compute resource under our control, and it
carries no egress cost to us. We stage only active genome-versus-all batches on
Stampede3 scratch, then filter, compress, verify, and upload them to GenomeArk.
We request no ACCESS storage resource.

**Local hardware.** One L40S GPU server supports development, `impg` indexing,
and small-scale testing. It cannot execute the pairwise production campaign and
is not a substitute for the requested Stampede3 compute.

**Current ACCESS allocation.** All Stampede3 work described here ran under
TG-MCB140147, the Galaxy gateway allocation. It serves here only as completed
preliminary work and the empirical basis for unit costs. This request covers
only new ordered pairs and downstream analyses not charged previously.

The Galaxy allocation PI has approved citation of this completed preliminary
work. No SUs in this request duplicate previously charged ordered pairs.

## 8. Code performance and scaling

Summarized here and detailed in the Code Performance document.

The alignment workload is embarrassingly parallel — N(N−1) independent pairwise
tasks — and distributes across arbitrary numbers of nodes and across multiple
systems without modification. This is why access to several resources in
parallel is useful to us rather than merely convenient.

Measured per-alignment cost is 0.263 node-hours for FastGA and 0.627 for
`wfmash`, over 336,980 completed alignments. The N(N−1) tasks have no
inter-task communication, so throughput scales with the number of nodes until
queue concurrency becomes limiting. `impg` indexing is a negligible collation
step and does not drive the resource request.
