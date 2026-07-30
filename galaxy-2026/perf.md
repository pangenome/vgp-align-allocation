# **The Galaxy ACCESS-CI Gateway 2026/27 allocation**

# **Code Performance and Resource Costs (2025/26 allocation period)**

*A unique feature of our system is that we support a wide variety of usage scenarios covering the full spectrum of compute job types, ranging from simple text file manipulations to complex genome assembly and whole-genome alignment tasks requiring specialized large-memory, multi-core, and GPU hardware. Consequently, this document reports scaling behavior per workload class rather than for a single application.*

# **1. Performance and scaling**

The Galaxy gateway enables users to run a wide variety of software tools with highly varied compute needs and scaling capabilities. The vast majority of these tools are either single core or single node, and scalability at the level of individual tools is not a major problem. Throughput is achieved by serving many users simultaneously. Scheduling across resources is thus the primary area for potential improvements in efficiency, and we have made substantial progress in this area (see Progress Report). However, for certain classes of jobs, specialized hardware is required. Below we describe our evaluation of these resources.

## **1.1. Jetstream2**

Jetstream (in both its iterations) is the primary "overflow" or "bursting" resource supplementing Galaxy's relatively small (736 core) fixed cluster at TACC. Galaxy utilizes Slurm's Cloud Computing functionality to automatically scale Jetstream2 instances to efficiently utilize the resource. Slurm automatically decides the size of the Jetstream2 instance to spin up, from `m3.medium` to `r3.xl`, based on each job's resource requirements. Weight is given to spinning smaller instances so as not to underutilize resources, and node sharing is enabled, so most single-core jobs sent to Jetstream2 run on unused cores of larger instances started for multicore jobs.

In addition to typical cluster jobs, we operate a scalable Docker-based cluster in Jetstream2 for Galaxy to run *Galaxy Interactive Tools* (GxITs). GxITs allow unprecedented levels of user control on a shared resource like Galaxy and include Jupyter and RStudio. Jetstream2 provides a platform that allows us to serve these tools to users in a safe and secure manner. We also allocate GPU instances (`g3.small` and `g3.medium`) for tools that use GPUs for performance increases—most notably genome sequence alignment with KegAlign (<https://github.com/galaxyproject/KegAlign>) and protein folding with ColabFold's AlphaFold2 implementation (<https://github.com/sokrypton/ColabFold>).

Because Jetstream is a cloud-style resource, it suits Galaxy's operational style more closely than traditional HPC resources. It allows us to directly provide our software and data stacks, making it easy to schedule a variety of existing tools. It also allows us to run jobs rapidly, without the long queue wait times that are unacceptable for users of an interactive system such as Galaxy.

Jetstream is also used to provide persistent "stratum 1" CernVM-FS (CVMFS) filesystem replicas of reference data and Singularity images used by jobs running on Jetstream, the dedicated Galaxy cluster at TACC, Galaxy's other ACCESS-allocated resources, and other Galaxy instances running worldwide.

Jetstream2 object storage additionally underpins GenomeArk2 (<https://genomeark2.org>), the public distribution platform for Vertebrate Genomes Project data. This is a sustained-capacity requirement rather than a burst one.

## **1.2. Large-memory and shared-node HPC resources**

The primary analysis types we run on large-memory nodes are *de novo* assembly of RNA-seq data and assembly of DNA sequencing data, increasingly for vertebrate genomes.

For assembly we use Unicycler, which incorporates SPAdes, a de Bruijn graph-based assembler with built-in error correction. Unicycler generates highly accurate assemblies by combining highly accurate short reads from the Illumina platform with long, error-prone reads from Pacific Biosciences or Oxford Nanopore technologies. We have determined that the maximum amount of memory SPAdes can effectively use is 250 GB, making the shared nodes of Bridges-2, Expanse, and Anvil a suitable fit for this tool.

We found that the memory and core counts in the whole-node partitions of these resources exceed what Unicycler and SPAdes can use. Because of this, we run these jobs on shared-node partitions, allocating only 32 cores and 64 GB of memory per job, further improving our resource utilization.

We increasingly use both cloud and HPC ACCESS resources to perform large genome assembly based on our Vertebrate Genomes Project (VGP) workflows (<https://training.galaxyproject.org/training-material/topics/assembly/tutorials/vgp_genome_assembly/tutorial.html>). [TODO: update the cumulative assembly count — 348 as of July 2025, 417 as of October 2025.]

As Galaxy has thousands of active users per month, and the types of analysis we aim to support are growing significantly in scale, we have found that HPC systems may have a significant amount of CPU time to offer, but effectively using that time can be difficult, especially for the single-node job types Galaxy runs. Queue depth limits are the binding constraint: Stampede3 limits users to 12–40 jobs in the queue depending on partition, and Expanse limits users to 64 jobs in the queue. Galaxy loads are bursty and unpredictable, and spreading load across multiple resources allows greater throughput for large parallel workflows such as those used in VGP analysis and during periods of high traffic. **This is the reason we request allocations on several similarly configured resources for what is nominally the same workload: it is a throughput requirement imposed by per-user queue limits, not redundancy.**

## **1.3. Whole-node parallel jobs**

We have primarily scheduled long-running single-node alignment jobs on Stampede3. These include Bowtie and BWA (tools for mapping sequence reads back to a reference sequence), HISAT2 (a tool for mapping reads derived from RNA back to a genome), and aligners such as the various tools from the BLAST suite. However, because Stampede3 allocates whole nodes while other resources allow shared-node allocations, we reserve Stampede3 for jobs requiring the highest core and memory counts. Relatively few such tools are popular in Galaxy, which is why our request on this resource has remained modest.

[TODO: Stampede3 usage has fallen for three consecutive years — 133,650 core-hours/month in 2023/24, 42,064 in 2024/25, and **700** through June 2026. The request is reduced to 250K node-hours in response. Explain the decline here in performance terms: whole-node allocation is a poor match for a tool catalog dominated by single-core and single-node jobs, and shared-node resources absorb that work at higher efficiency. If no specific whole-node workload is planned for 2026/27, consider dropping the line rather than defending it.]

## **1.4. GPU-accelerated pairwise alignment (KegAlign)**

The all-to-all vertebrate genome alignment described in the Main Document is GPU-bound, and its cost model is what drives the GPU components of this request. KegAlign [19] optimizes pairwise alignment through diagonal partitioning, which addresses the load imbalance that limits GPU utilization in conventional seed-and-extend aligners.

[TODO: This section needs real benchmark numbers, and it is the single highest-value addition to this document. The Code Performance & Resource Costs document is explicitly required to "contain code performance timings, resource usage details, and scaling information" sufficient to support the calculation of the request. Supply:
- KegAlign wall-clock per genome pair on each GPU type (Jetstream2 g3, Expanse V100, Delta A100/H200), ideally showing the H200 speedup that was used to justify the Delta line in 2025.
- Scaling curve across GPUs per job.
- Derivation of total GPU-hours: pairs × hours/pair, versus the requested GPU SUs.
- The equivalent derivation for the ~5M CPU-hour all-to-all estimate, which is currently asserted from "completion of 10% of the task" without a supporting table.]

# **2. Resource cost derivation**

[TODO: Build a table mapping each requested resource line to the workload it serves and the arithmetic behind the number, e.g.:

| Resource | Workload | Unit cost | Volume | Requested |
| --- | --- | --- | --- | --- |
| Jetstream2 LM | VGP assembly | X SU/assembly | N assemblies/yr | ... |
| Jetstream2 CPU | general throughput | X SU/job | N jobs/yr | ... |
| GPU lines | KegAlign alignment | X GPU-h/pair | N pairs | ... |

Reviewers evaluate "Efficient Use of Resources," and prior versions of this document justified amounts by reference to past usage rather than by derivation. Deriving them from measured per-unit costs is what this document is for.]
