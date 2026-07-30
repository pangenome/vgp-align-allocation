# **The Galaxy ACCESS-CI Gateway 2024/25 allocation**

# **Performance and Scaling report (2023 allocation period)**

*Our performance and scalability metrics remain the same. A unique feature of our system is that we are supporting a wide variety of usage scenarios covering the full spectrum of compute job types ranging from simple text file manipulations to complex genome assembly tasks requiring specialized large memory and multi-core hardware.* 

# **Performance and scaling**

The Galaxy gateway enables users to run a wide variety of software tools with highly varied compute needs and scaling capabilities. The vast majority of these tools are either single core or single node and scalability at the level of individual tools is not a major problem. Throughput is achieved by serving many users simultaneously. Scheduling across resources is thus the primary area for potential improvements in efficiency, and we have made substantial progress in this area (see Progress Report). However, for certain types of jobs, special hardware resources are needed, below we describe our evaluation of these resources.

## **Jetstream-2**

We have successfully demonstrated integration of *Jetstream* into Galaxy. Jetstream (in both its iterations) has become the primary “overflow” or “bursting” resource supplementing Galaxy’s small (128 core) fixed cluster at TACC. In the past year, we have successfully utilized a large number and a wide variety of Jetstream2 instances. Galaxy utilizes Slurm’s Cloud Computing functionality to automatically scale Jetstream2 instances to efficiently utilize the resource. Slurm automatically decides the size of the Jetstream2 instance to spin, from m3.tiny to r3.xl, based on each job’s resource requirements. Weight is given to spinning smaller instances so as not to underutilize resources, and node sharing is enabled, so most single-core jobs that are sent to Jetstream2 run on unused cores on larger instances started for multicore jobs.

In addition to typical cluster jobs, we also operate a scalable Kubernetes cluster in Jetstream2 for Galaxy to run *Galaxy Interactive Tools* (GxITs). GxITs are special tools that allow unprecedented levels of user control on a shared resource like Galaxy and include Jupyter and R Studio. Jetstream2 provides a platform that allows us to serve these tools to users in a safe and secure manner. Finally, we have allocated up to four g3.small and four g3.medium GPU instances for the few tools that utilize GPUs for performance increases. Most notably, we are performing genome sequence alignments with SegAlign (<https://github.com/galaxyproject/SegAlign>) on Jetstream2 GPU instances.

Because Jetstream is a cloud-style resource, it suits Galaxy’s operational style more closely than traditional HPC resources. It allows us to directly provide our software and data stacks, making it easy to schedule a variety of existing tools. It also allows us to run jobs rapidly, without long queue wait times that are unexpected for users of an interactive system such as Galaxy.

Jetstream is also used to provide persistent “stratum 1” CernVM-FS (CVMFS) filesystem replicas of reference data and Singularity images used by jobs running on Jetstream, the dedicated Galaxy Cluster at TACC, Galaxy’s other ACCESS-allocated resources, and other Galaxy instances running worldwide.

## **Bridges-2 / Expanse / Anvil**

The primary analysis type we have run on large memory nodes is *de novo* assembly of RNA-seq data (currently in use), as well as assembly of DNA sequencing data, increasingly for vertebrate genomes.

For assembly we are utilizing a package called Unicycler. Unicycler incorporates SPAdes, a deBruijn graph-based assembler with built-in error correction. Unicycler generates highly accurate assemblies by combining high accurate short reads from the Illumina sequencing platform with long error-prone reads from Pacific Biosciences or Oxford Nanopore technologies. We have determined that the maximum amount of memory that SPAdes can effectively use is 250 GB, making the nodes of Bridges-2, Expanse, and Anvil a suitable fit for this tool.

We found that the memory and core counts in the whole node partitions of these resources were more than needed for Unicycler and SPAdes. Because of this, we run these jobs on shared node partitions, allocating only 32 cores and 64 GB of memory per job, further improving our resource utilization.

In the previous allocation period we increasingly used both cloud and HPC ACCESS resources for performing large genome assembly based on our Vertebrate Genomes Project (VGP) workflows (<https://training.galaxyproject.org/training-material/topics/assembly/tutorials/vgp_genome_assembly/tutorial.html>). To date, 154(\!) vertebrate genome assemblies have been performed using ACCESS resources through Galaxy, and this number will continue to grow during the next allocation period. 

As Galaxy has over 7,000 active users per month, and the types of analysis we aim to support are growing significantly in scale \[VGP\], we have found that HPC systems may have a significant amount of CPU time to offer, but effectively using that time can be difficult, especially for the single-node types of jobs that Galaxy runs. For example, Stampede3 limits users to 4 jobs in the queue, and Expanse limits users to 64 jobs in the queue. Galaxy loads are bursty and unpredictable, and the ability to spread the load out across multiple resources allows for greater throughput for large parallel workflows such as those used with VGP analysis, and periods of high traffic. In order to account to this limitation we will request allocation on all three of Bridges-2 / Expanse / Anvil for similar workloads.

## **Stampede3**

We have primarily scheduled long-running single node alignment jobs on *Stampede3*. These include Bowtie and BWA (tools for mapping sequence reads back to a reference sequence), and HiSat (a tool for mapping reads derived from RNA back to a genome), as well as aligners such as various tools from the BLAST suite. However, because Stampede3 allocates whole nodes and other resources allow shared node allocations, we have begun to reserve Stampede3 for jobs requiring the highest core and memory counts. Fewer such tools are popular in Galaxy, and so the need for resources on Stampede3 has decreased slightly since the previous year. Because of this, we are decreasing our allocation request for Stampede3 from 1M SUs to 500K.

  