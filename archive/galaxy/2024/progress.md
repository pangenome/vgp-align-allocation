# **The Galaxy ACCESS-CI Gateway 2024/25 allocation**

# **Progress report (2023 allocation period)**

During the last allocation period our primary focus was on more efficiently using the compute resources allocated to us, as well as improving our ability to balance jobs across the least-loaded resources.

Because the current allocation period has not ended, we will consider average compute hours per month to evaluate compute usage for the Galaxy Gateway, through the end of June 2024. Please note that due to extensions in 2020, the allocation periods are not equally sized 

|  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: |
|   | \*\*2020\*\* | \*\*2021\*\* | \*\*2022\*\* | \*\*2023\*\* |
| Galaxy Dedicated | 164,312 | 163,940 | 140,261 | 119,242 |
| Frontera (non-ACCESS) | 53 | 11,316 | 0 | 1,046 |
| Jetstream 1/2 | 105,029 | 208,609 | 103,715 | 184,804 |
| Bridges-2 | 81,197 | 94,488 | 74,739 | 142,718 |
| Expanse | 1,523 | N/A | 4,593 | 283,321 |
| Stampede 2/3 | 33,313 | 138,099 | 335,309 | 71,553 |
| Rockfish | N/A | N/A | 5,229 | 124,551 |
| Total | 385,427 | 616,453 | 663,846 | 928,162 |
| Total ACCESS | 221,062 | 441,196 | 523,586 | 807,874 |
| \*\*Percent ACCESS\*\* | \*\*57%\*\* | \*\*73%\*\* | \*\*79%\*\* | \*\*87%\*\* |

  

The Galaxy Dedicated and Jetstream 2 compute hour calculations were performed using Galaxy’s internal accounting and is an undercalculation compared to the other resources, which used the more accurate Slurm accounting database. However, the complete or near exhaustion of our allocations on Jetstream 2, Expanse, Bridges-2, and Rockfish corroborate this increase in ACCESS resource utilization, especially considering the significant increase in Jetstream 2 SUs (5.5M CPU, 3.5M Large Memory) allocated to the Galaxy project over previous allocation periods (3M CPU).

In this allocation period, we requested time on three resources that are similar in configuration: Bridges-2, Expanse, and Anvil. This decision was made after we successfully exhausted our Bridges-2, Expanse, and Rockfish allocations in previous years, had successfully shifted more of our workload to shared node allocations, and demonstrated an ability to efficiently balance workloads across multiple resources. In addition, adjustments to our scheduling policy resulted in a more efficient usage of Stampede3, which allocates full nodes to jobs.

During the 2022-2023 allocation period we developed and deployed a metascheduling system for Galaxy, the Galaxy Total Perspective Vortex (TPV) (<https://total-perspective-vortex.readthedocs.io/>), a rule- and tag-based system for deciding where to route Galaxy jobs. This was in preliminary use as of the end of that period, but we began routing all Galaxy jobs through it during the 2023-2024 period. This allowed us to fully utilize our allocations on Bridges-2, Rockfish, Expanse, and Jetstream 2.

Galaxy stores 5.8 TB of genomic and other bioinformatics reference data in CVMFS (<https://cernvm.cern.ch/fs/>), a global read-only filesystem designed for software and data distribution. Because this filesystem is not mounted on HPC systems, this limited our ability to send certain types of jobs to those systems. During the 2022-2023 allocation period, we successfully deployed the cvmfsexec package (<https://github.com/cvmfs/cvmfsexec>) to provide this data. Combined with Apptainer (<https://apptainer.org/>), we have been able to produce a compute environment on unprivileged, shared HPC systems that exactly mirrors the environment on our dedicated cluster and cloud instances on Jetstream 2. During the 2023-2024 period, we refined this environment to eliminate sources of job failures.

  
**Figure 1**. Galaxy Gateway compute utilization (per month) by resource.

Leveraging this work, we have been able to make more efficient use of all resources supporting the Galaxy Gateway, including dedicated resources. Overall, utilizing ACCESS resources, we have enabled **35% more analysis hours per month** compared to the last period.