# **The Galaxy ACCESS-CI Gateway 2022/23 allocation**

# **Progress report (2022 XRAC period)**

During the last allocation period our primary focus was on increasing the types of jobs and tools that could be sent to a wider array of compute resources, as well as improving our ability to balance jobs across the least-loaded resources.

Because the current allocation period has not ended, we will consider average compute hours per month to evaluate compute usage for the Galaxy Gateway, through the end of June 2023. Please note that due to extensions in 2020, the allocation periods are not equally sized 

|  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: |
|   | \*\*2019 XRAC\*\* | \*\*2020 XRAC\*\* | \*\*2021 XRAC\*\* | \*\*2022 XRAC TD\*\* |
| Galaxy Dedicated | 120,813 | 164,312 | 163,940 | 140261 |
| Frontera (non-XSEDE) | N/A | 53 | 11,316 | 0 |
| Jetstream | 42,638 | 105,029 | 198,445 | 0 |
| Jetstream2 | N/A | N/A | 10,164 | 103,715 |
| Bridges-2 | 43,561 | 81,197 | 94,488 | 74,739 |
| Expanse | N/A | 1,523 | N/A | 4,593 |
| Stampede 2 | 24,716 | 33,313 | 138,099 | 335,309 |
| Rockfish | N/A | N/A | N/A | 5,229 |
| Total | 231,727 | 385,427 | 616,453 | 663,846 |
| Total ACCESS | 110¸914 | 221,062 | 441,196 | 523,586 |
| \*\*Percent ACCESS\*\* | \*\*48%\*\* | \*\*57%\*\* | \*\*73%\*\* | \*\*79%\*\* |

  

In this allocation period, we requested time on four resources that are very similar in configuration: Bridges-2, Stampede2, Expanse, and Rockfish. This decision was made after we successfully exhausted our Stampede2 and Bridges-2 allocations in previous years, and had successfully utilized Expanse to run our Bridges-2 jobs after that exhaustion during the 2021-2022 allocation period.

During the 2022-2023 period, it was necessary to develop and deploy a metascheduling system for Galaxy to balance the load across HPC resources granted by ACCESS. This was achieved in the form of the Galaxy Total Perspective Vortex (TPV) (<https://total-perspective-vortex.readthedocs.io/>), a rule- and tag-based system for deciding where to route Galaxy jobs. After the deployment of TPV in early 2023, we successfully began distributing jobs across all four of the allocated HPC systems, and expect this to continue and grow moderately across the final months of our 2022 allocation.

Galaxy stores 5.8 TB of genomic and other bioinformatics reference data in CVMFS (<https://cernvm.cern.ch/fs/>), a global read-only filesystem designed for software and data distribution. Because this filesystem was not mounted on HPC systems, this limited our ability to send certain types of jobs to HPC systems. During previous allocation periods, we had successfully used the CVMFS Parrot Connector (<https://cvmfs.readthedocs.io/en/stable/cpt-hpc.html#parrot-mounted-cernvm-fs-in-lieu-of-fuse-module>) as well as a path-rewriting scheme implemented through Galaxy’s remote execution engine, Pulsar (<https://pulsar.readthedocs.io/>). However, during the 2022-2023 allocation period, we successfully deployed the cvmfsexec package (<https://github.com/cvmfs/cvmfsexec>) to provide this functionality in a more straightforward and supported manner. Of note, the Pulsar-based method did not safely run on shared nodes such as those available on Bridges-2 and Expanse. The cvmfsexec utility does not have this limitation.

  
**Figure 1**. Galaxy Gateway compute utilization (per month) by resource type.

Leveraging both the CVMFS mount solution, TPV, and SlurmScale, the cloud autoscaling system we developed with ECSS support during a previous allocation cycle, we have been able to make more efficient use of all resources supporting the Galaxy Gateway, including dedicated resources. Overall, utilizing ACCESS resources, we have enabled **7% more analysis hours per month** compared to the last period.  The proportion of work performed on Galaxy that utilizes XSEDE resources has increased to 79% even as the total has increased, owing to significant increases in the types of jobs that can be sent to ACCESS resources.