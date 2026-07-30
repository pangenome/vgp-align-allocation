# **The Galaxy ACCESS-CI Gateway 2026/27 allocation**

# **Progress report (2025/26 allocation period)**

> **Hard limit: 3 pages.** The publication list must not live in this document — put it in the References document (no page limit) or cite the Zotero library. The 2025 report overran on exactly this.
>
> **Blocking gap:** the compute-hour table below stops at June 2025. The period this report must cover is Oct 2025 – Sep 2026, for which no data exists in any of the Drive workbooks. Pull it from XDMoD (<https://xdmod.access-ci.org>) before submitting. See `notes/usage-data.md`.

## **1. Resource utilization**

Because the current allocation period has not ended, we evaluate compute usage for the Galaxy Gateway using average compute hours per month, through [TODO: end of June 2026 — and say June 2026, not June 2024; the 2025 report carried this date forward without updating it].

Average compute hours per month by resource, by allocation year (Oct 1 – Sep 30):

| | **Oct 21–Sep 22** | **Oct 22–Sep 23** | **Oct 23–Sep 24** | **Oct 24–Sep 25** | **Oct 25–Jun 26** |
| --- | --- | --- | --- | --- | --- |
| Galaxy Dedicated | 163,940 | 137,257 | 130,396 | 179,968\* | TODO |
| Frontera (non-ACCESS) | 11,316 | 0 | 1,167 | 2,899\* | TODO |
| Jetstream2 | 10,164 | 103,715 | 203,268 | 318,555\* | TODO |
| Jetstream2 GPU | — | — | 425 | 1,255\* | TODO |
| Bridges-2 | 94,488 | 74,739 | 117,276 | 171,510\* | TODO |
| Expanse | 0 | 4,593 | 224,939 | 158,848\* | TODO |
| Anvil | — | — | 0 | 197,602\* | TODO |
| Stampede 2/3 | 138,099 | 335,309 | 133,650 | 56,085\* | TODO |
| Rockfish | — | 5,229 | 93,414 | 0 | — |
| **Total ACCESS** | 441,196 | 470,130 | 772,971 | 903,854\* | TODO |
| **Total (all)** | 616,453 | 607,387 | 904,534 | 1,086,721\* | TODO |
| **Percent ACCESS** | 72% | 77% | 85% | 83%\* | TODO |

\* Nine months only (Oct 2024 – Jun 2025); the workbook has no data past June 2025.

Note: label columns by explicit date range rather than a bare year. Past reports labeled these columns by starting year while the source workbook labels them by ending year, and the two documents consequently print different values for what a reader takes to be the same year. See `notes/usage-data.md`.

The Galaxy Dedicated and Jetstream2 compute hour calculations were performed using Galaxy's internal accounting and undercount relative to the other resources, which use the more accurate Slurm accounting database.

### Trends to state explicitly

Growth is substantial and continuing. Straight-lining the nine recorded months of Oct 2024 – Sep 2025 gives approximately 10.85M ACCESS core-hours, **a 17% increase over the completed prior year (9.28M)**. Within that:

- **Anvil went from zero to production at scale** — 197,602 hrs/mo average, and 835,549 core-hours in June 2025 alone. This validates the decision to add Anvil to the request.
- **Jetstream2 grew 57%** (203,268 → 318,555 hrs/mo) and **Bridges-2 grew 46%** (117,276 → 171,510 hrs/mo).
- **Expanse fell 29%** and **Stampede3 fell 58%**.

[TODO — resolve before writing this section. Bridges-2, Stampede3, and Rockfish all report **exactly zero** for both May and June 2025. That pattern reads as allocation exhaustion or expiry, not as weak demand. Which it was determines what this report says:
- If those allocations were **exhausted**, the Stampede3 decline is not underutilization at all and should be reported as saturation — a completely different and much stronger argument.
- If they were **underutilized**, ACCESS requires this report to "briefly describe the reasons for the underutilization and any mitigation," and the Stampede3 request should come down accordingly.

Do not assert either without checking the portal. This single question changes both the Progress Report narrative and the Stampede3 line in the request.]

## **2. Efficiency and scheduling improvements**

[TODO: rebuild with 2025/26 content. The narrative so far, for continuity:
- 2022/23: developed the Total Perspective Vortex (TPV) metascheduler.
- 2023/24: routed all Galaxy jobs through TPV; deployed `cvmfsexec` + Apptainer to reproduce our execution environment on unprivileged shared HPC nodes. Result: **35% more analysis hours per month** than the prior period.
- 2024/25: that environment ran in production throughout; all Galaxy jobs became runnable on ACCESS resources.
- 2025/26: needs a concrete, quantified efficiency claim. The Anvil ramp is the obvious candidate — going from zero to 835K core-hours in a month is evidence that our multi-resource scheduling works.]

Galaxy stores ~5.8 TB of genomic and other bioinformatics reference data in CVMFS (<https://cernvm.cern.ch/fs/>), a global read-only filesystem designed for software and data distribution. Because this filesystem is not natively mounted on HPC systems, we deploy `cvmfsexec` (<https://github.com/cvmfs/cvmfsexec>) combined with Apptainer (<https://apptainer.org/>) to produce a compute environment on unprivileged, shared HPC systems that exactly mirrors the environment on our dedicated cluster and on Jetstream2. This has been in production use since the 2024/25 period and lets us make efficient use of every resource supporting the gateway.

## **3. User statistics**

Demand set records during this period. In **October 2025 users ran 1,010,496 jobs — the highest monthly total in the platform's history** — and in **November 2025 the platform served 11,108 active users, also an all-time record**. As of January 2026 approximately **448,500 researchers** had registered accounts.

Job volume by allocation year:

| Period | Jobs | New registrations | Mean active users/mo |
| --- | --- | --- | --- |
| Oct 2022 – Sep 2023 | 6,159,432 | 42,691 | 7,023 |
| Oct 2023 – Sep 2024 | 7,649,740 | 48,539 | 7,888 |
| Oct 2024 – Sep 2025 | 9,416,802 | 60,534 | 9,073 |
| Oct 2025 – Jan 2026 (4 mo) | 3,038,717 | 23,350 | 9,488 |

Job volume grew **23% year over year** between the two most recent complete allocation years, and the partial current year is tracking above the last on active users. An "active user" is a registered user who submitted at least one job in the given month.

[TODO: extend the table through June 2026 — the source workbook stops at January 2026. Also refresh from the Looker dashboard, which is the source for the following, quoted here at their June 2025 values: job failure rate 10.3% (~70,000/month, overwhelmingly from malformed user data rather than infrastructure — the new-user failure rate was *lower*, at 8.8%); 11.1M histories created; 128.4M datasets generated; >492,000 workflows created and >868,000 workflow invocations; 6,900 distinct tools installed. Note the workbook's own tool-count cell reads 2008 and is years stale — use the live API, not that cell.]

## **4. Scientific output enabled by the gateway**

The service we provide is well established and widely used; as a result it is often taken for granted and not cited properly. The full — still incomplete — list of publications resulting from community use of Galaxy is maintained at <https://www.zotero.org/groups/1732893/galaxy/items/L5WWHAIU/library>.

[TODO: give publication counts for 2025 and 2026 to date. Prior counts: **183 for 2024**, **322 for 2025**. Do not paste the list into this document — that is what broke the page limit last time. Put it in the References document instead.]

## **5. Vertebrate Genomes Project and GenomeArk2**

[TODO: cumulative assembly count as of mid-2026. Known checkpoints: over 150 (July 2024), 348 (July 2025), 417 (October 2025). Note the public page at galaxyproject.org/projects/vgp still reads "Last updated January, 2025 with 315 assemblies of 188 species" — update it, since a reviewer following the citation will find a smaller, older number than the proposal claims.]

Assemblies produced through this allocation span genome sizes from ~1 Gb to over 3 Gb, with contig N50 values between 40 Mbp and 355 Mbp — often encompassing complete chromosomes and chromosome arms. The methods are published [27].

During this period we launched GenomeArk2 (<https://genomeark2.org>), the central distribution hub for VGP data, built on Jetstream2 object storage. It provides open access to petabyte-scale assemblies, annotations, and downstream analysis results with versioning and metadata support, and integrates directly with Galaxy so that researchers can discover, access, and analyze VGP data entirely within public computational environments.

[TODO: if the VGP Phase 1 publications have appeared or are in press, say so and cite them. As of October 2025 a series was in preparation for *Nature* under the Phase 1 umbrella, featuring Jetstream2 as enabling infrastructure. A published Phase 1 paper crediting ACCESS is the single most valuable item this report can carry.]

## **6. Whole-genome alignment**

[TODO: report what fraction of the all-to-all alignment of 477 vertebrate assemblies completed during 2025/26, and what it consumed. The 2025 request stated the workflows were developed and "will be put into production during the next allocation phase" — reviewers who read that sentence will look for the result here. This is a promise that has come due, and leaving it unanswered is worse than reporting partial progress.]
