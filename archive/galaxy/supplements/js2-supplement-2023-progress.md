# **The Galaxy ACCESS-CI Gateway 2023/24 allocation: A supplement Request**

# **Better Utilization of Allocations**

Beginning in mid-March, 2024, we shifted jobs from m3.xl and m3.2xl Jetstream2 CPU instances to r3.large and r3.xl Jetstream2 Large Memory instances. Because many jobs require a large amount of memory but encounter diminishing returns (if not decreases in performance) with increasing core counts, Jetstream2 Large Memory instances are ideal for some types of jobs, since they offer 8 GB/core as opposed to the 4 GB/core of m3 instances types. For example, Kraken2 (<https://ccb.jhu.edu/software/kraken2/>) requires at least as much memory as the database selected by the user. The largest such database is now nearly 1 TB, which cannot be run on even the largest m3 instance type. Smaller databases can fit on m3.3xl instances, but the 128 core count is somewhat wasted. Initially we planned to hold back Jestream2 Large Memory capacity for Vertebrate Genomes Project (VGP) jobs, but this proved to be unnecessary by Spring 2024, and we allowed more regular jobs to run in the Large Memory allocation. 

|  |
| :-: |
|  |
| \*\*Figure 1.\*\* CPU Hours on Jetstream2 resources since the beginning of 2024. A significant increase in Jetstream2 Large Memory hours, and a decrease in Jetstream2 CPU hours can be seen when changes were made to our scheduling algorithm in March.  |

At the same time as this increase in normal jobs to r3 instances, VGP compute utilization increased on both Jetstream2 resources. As a result, we exhausted our Jetstream2 CPU allocation earlier than expected, and utilized more of the Large Memory allocation than expected in a short time frame.