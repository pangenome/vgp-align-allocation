# **The Galaxy ACCESS-CI Gateway 2026/27 allocation**

# **Progress report (2025/26 allocation period)**

> **Hard limit: 3 pages.** Keep the publication list out of this document — it belongs in References, which has no page limit. The 2025 report overran on exactly this.

## **1. Resource utilization**

The current allocation period has not ended, so we evaluate compute usage as average core-hours per month, through the end of **June 2026** (nine months of the period).

| Core-hours/month | **Oct 23–Sep 24** | **Oct 24–Sep 25** | **Oct 25–Jun 26** |
| --- | --- | --- | --- |
| Galaxy Dedicated (non-ACCESS) | 130,396 | 165,608 | 126,795 |
| Jetstream2 | 203,268 | 359,042 | **626,661** |
| Jetstream2 GPU | 425 | 1,285 | 903 |
| Bridges-2 | 117,276 | 128,633 | 73,268 |
| Expanse | 224,939 | 141,545 | 88,326 |
| Anvil | 0 | 171,587 | 46,835 |
| Stampede3 | 133,650 | 42,064 | 700 |
| Rockfish | 93,414 | 0 | 0 |
| Frontera (non-ACCESS) | 1,167 | 2,174 | 0 |
| **Total ACCESS** | **772,971** | **844,155** | **836,693** |
| **Total, all sources** | 904,534 | 1,011,937 | 963,487 |

Over the nine recorded months of the current period the gateway consumed **7,530,233 ACCESS core-hours**; the completed prior year totaled 10,129,862.

Galaxy Dedicated and Jetstream2 figures come from Galaxy's internal accounting and undercount relative to the other resources, which use the more accurate Slurm accounting database.

### **Consolidation onto Jetstream2**

Aggregate ACCESS consumption held steady across the two periods—844,155 versus 836,693 core-hours per month—but its distribution changed substantially. Jetstream2 grew **75%** and now carries roughly three quarters of our ACCESS compute, up from two fifths a year earlier, while every HPC line declined.

This is the intended behavior of the scheduling work described in §2, not a drop in demand. The Total Perspective Vortex routes each job to the destination matching its resource profile, and the majority of Galaxy's workload—short, single-core to single-node, latency-sensitive, and submitted in unpredictable bursts by thousands of independent users—matches a cloud-style elastic resource far better than a batch HPC queue. As TPV routing matured, that majority migrated to where it runs most efficiently. The HPC allocations continue to serve the workloads they are uniquely suited to: large-memory assembly on Bridges-2 and Expanse, and whole-node parallel jobs on Stampede3.

[TODO — the one thing this section still needs. Two declines require explicit explanation under the ACCESS requirement that a progress report describe "the reasons for the underutilization and any mitigation":

1. **Stampede3 fell to 700 core-hours/month, effectively zero.** We are reducing the request from 500K to 250K node-hours in response. State the reason plainly — whole-node allocation is a poor fit for the current tool mix, and shared-node resources absorbed the work.
2. **Anvil fell 73%** (171,587 → 46,835 core-hours/month). This one is genuinely puzzling, since it was ramping steeply through mid-2025, and it needs a real explanation rather than a guess. Was there an outage, a TPV routing change, an allocation lapse, or did the work simply move to Jetstream2?

Reviewers score "Efficient Use of Resources." Naming these declines and explaining them reads far better than letting the table speak for itself.]

## **2. Efficiency and scheduling improvements**

[TODO: describe what changed in 2025/26. The prior arc, for continuity: developed TPV (2022/23); routed all jobs through it and deployed `cvmfsexec` + Apptainer, yielding 35% more analysis hours per month (2023/24); ran that environment in production and made all Galaxy jobs runnable on ACCESS resources (2024/25). The Jetstream2 consolidation documented above is the natural headline for this period — quantify what drove it.]

Galaxy stores ~5.8 TB of genomic and other bioinformatics reference data in CVMFS (<https://cernvm.cern.ch/fs/>), a global read-only filesystem designed for software and data distribution. Because this filesystem is not natively mounted on HPC systems, we deploy `cvmfsexec` (<https://github.com/cvmfs/cvmfsexec>) with Apptainer (<https://apptainer.org/>) to produce a compute environment on unprivileged, shared HPC systems that exactly mirrors the environment on our dedicated cluster and on Jetstream2.

## **3. User statistics**

Demand set records during this period. Users ran **1,010,496 jobs in October 2025**, the highest monthly total in the platform's history, and passed one million again in **May 2026 (1,000,040)**. **November 2025 saw 11,109 active users**, also an all-time high. By June 2026, **479,604 researchers** had registered accounts.

| Period | Jobs | New registrations | Mean active users/mo |
| --- | --- | --- | --- |
| Oct 2022 – Sep 2023 | 6,159,432 | 42,691 | 7,023 |
| Oct 2023 – Sep 2024 | 7,649,740 | 48,539 | 7,888 |
| Oct 2024 – Sep 2025 | 9,416,835 | 60,534 | 9,073 |
| Oct 2025 – Jun 2026 (9 mo) | 6,744,172 | 54,455 | 9,322 |

New user registration is accelerating: 54,455 researchers registered in nine months, which annualizes to roughly 72,600 and represents a **20% increase** over the prior full year. An "active user" is a registered user who submitted at least one job in the given month.

[TODO: refresh the following from the Looker dashboard — they are quoted at their June 2025 values and are not in the workbook: job failure rate (10.3%, ~70,000/month, overwhelmingly from malformed user data rather than infrastructure; the new-user rate was *lower*, at 8.8%); histories created (11.1M); datasets generated (128.4M); workflows created (>492,000) and invoked (>868,000); distinct tools installed (6,900 — note the workbook's own tool-count cell reads 2008 and is years stale, so use the live API).]

## **4. Scientific output enabled by the gateway**

The service we provide is well established and widely used; as a result it is often taken for granted and not cited properly. The full — still incomplete — list of publications resulting from community use of Galaxy is maintained at <https://www.zotero.org/groups/1732893/galaxy/items/L5WWHAIU/library>.

[TODO: publication counts for 2025 and 2026 to date. Prior: 183 (2024), 322 (2025). Do not paste the list here — that is what broke the page limit last time.]

## **5. Vertebrate Genomes Project and GenomeArk2**

[TODO: cumulative assembly count as of mid-2026. Known checkpoints: over 150 (July 2024), 348 (July 2025), 417 (October 2025). The public page at galaxyproject.org/projects/vgp still reads "Last updated January, 2025 with 315 assemblies of 188 species" — update it, since a reviewer following the citation will otherwise find a smaller, older number than this proposal claims.]

Assemblies produced through this allocation span genome sizes from ~1 Gb to over 3 Gb, with contig N50 values between 40 Mbp and 355 Mbp—often encompassing complete chromosomes and chromosome arms. The methods are published [27].

During this period we launched GenomeArk2 (<https://genomeark2.org>), the central distribution hub for VGP data, built on Jetstream2 object storage. It provides open access to petabyte-scale assemblies, annotations, and downstream analysis results with versioning and metadata support, and integrates directly with Galaxy so that researchers can discover, access, and analyze VGP data entirely within public computational environments.

[TODO: if the VGP Phase 1 publications have appeared or are in press, say so and cite them. As of October 2025 a series was in preparation for *Nature* under the Phase 1 umbrella, featuring Jetstream2 as enabling infrastructure. A published Phase 1 paper crediting ACCESS is the single most valuable item this report can carry.]

## **6. Whole-genome alignment**

[TODO: report what fraction of the all-to-all alignment of 477 vertebrate assemblies completed during 2025/26, and what it consumed. The 2025 request stated the workflows were developed and "will be put into production during the next allocation phase" — reviewers who read that will look for the result here. Note that Jetstream2 GPU consumption fell this period (903 core-hours/month), which does not suggest a heavy GPU production run; if it has not started, say so and explain why rather than leaving it unaddressed.]
