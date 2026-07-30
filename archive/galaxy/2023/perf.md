# **The Galaxy ACCESS-CI Gateway 2022/23 allocation**

*Our performance and scalability metrics remain the same. A unique feature of our system is that we are supporting a wide variety of usage scenarios covering the full spectrum of compute job types ranging from simple text file manipulations to complex genome assembly tasks requiring specialized large memory and multi-core hardware.* 

# **Performance and scaling**

The Galaxy gateway enables users to run a wide variety of software tools with highly varied compute needs and scaling capabilities. The vast majority of these tools are either single core or single node and scalability at the level of individual tools is not a major problem. Throughput is achieved by serving many users simultaneously. Scheduling across resources is thus the primary area for potential improvements in efficiency, and we have made substantial progress in this area (see Progress Report). However, for certain types of jobs, special hardware resources are needed, below we describe our evaluation of these resources.

## **Jetstream-2**

We have successfully demonstrated integration of *Jetstream* into Galaxy. Jetstream (in both its iterations) has become the primary “overflow” or “bursting” resource supplementing Galaxy’s small (128 core) fixed cluster at TACC. In the past year, we have successfully utilized a large number and a wide variety of Jetstream2 instances. Galaxy utilizes Slurm’s Cloud Computing functionality to automatically scale Jetstream2 instances to efficiently utilize the resource. The majority of jobs we dispatch to Jetstream2 run on m3.medium instances with a maximum of 48 of those instances possible to run simultaneously. Galaxy can also spin instances from m3.tiny to m3.xl as job resource requirements demand. Such instances are configured to be shared, so that if jobs are already running on an instance but not requiring all of that instance’s cores or memory, additional jobs can utilize the spare resources.

In addition to typical cluster jobs, we also operate a scalable Kubernetes cluster in Jetstream2 for Galaxy to run *Galaxy Interactive Tools* (GxITs). GxITs are special tools that allow unprecedented levels of user control on a shared resource like Galaxy and include Jupyter and R Studio. Jetstream2 provides a platform that allows us to serve these tools to users in a safe and secure manner.

Finally, we have allocated up to four g3.small GPU instances for the few tools that utilize GPUs for performance increases. This usage will increase greatly as we deploy the AlphaFold2 tool (https://www.nature.com/articles/s41594-021-00650-1) to Galaxy. AlphaFold2 has been a massive success on the Australian Galaxy server, which utilizes Azure to provide GPUs. Jetstream2 GPU instances allow us to provide this valuable tool to researchers at no cost.

Because Jetstream is a cloud-style resource, it suits Galaxy’s operational style more closely than traditional HPC resources. It allows us to directly provide our software and data stacks, making it easy to schedule a variety of existing tools. It also allows us to run jobs rapidly, without long queue wait times that are unexpected for users of an interactive system such as Galaxy.

Jetstream is also used to provide persistent “stratum 1” CernVM-FS (CVMFS) filesystem replicas of reference data and Singularity images used by jobs running on Jetstream, the dedicated Galaxy Cluster at TACC, Galaxy’s other ACCESS-allocated resources, and other Galaxy instances running worldwide.

## **Bridges-2 / Expanse / Rockfish**

The primary analysis type we have run on large memory nodes is *de novo* assembly of RNA-seq data (currently in use), as well as assembly of DNA sequencing data (currently in use for viral \[e.g., SARS-CoV2\], bacterial genomes, and increasingly for vertebrate genomes). 

For assembly we are utilizing a package called Unicycler. Unicycler incorporates SPAdes, a deBruijn graph-based assembler with built-in error correction. Unicycler generates highly accurate assemblies by combining high accurate short reads from the Illumina sequencing platform with long error-prone reads from Pacific Biosciences or Oxford Nanopore technologies. We have determined that the maximum amount of memory that SPAdes can effectively use is 250 GB, making the nodes of Bridges-2, Expanse, and Rockfish a suitable fit for this tool.

We found that the memory and core counts in the RM partition were more than needed for Unicycler and SPAdes. Because of this, we run these jobs on shared node partitions, allocating only 32 cores and 64 GB of memory per job, further improving our resource utilization.

In 2023 and beyond we will increasingly use these resources for performing large genome assembly based on our Vertebrate Genomes Project (VGP) workflows (<https://training.galaxyproject.org/training-material/topics/assembly/tutorials/vgp_genome_assembly/tutorial.html>) 

As Galaxy has over 7,000 active users per month, and the types of analysis we aim to support are growing significantly in scale \[VGP\], we have found that HPC systems may have a significant amount of CPU time to offer, but effectively using that time can be difficult, especially for the single-node types of jobs that Galaxy runs. For example, Stampede-2 limits users to 20 jobs in the queue, and Expanse limits users to 64 jobs in the queue. Galaxy loads are bursty and unpredictable, and the ability to spread the load out across multiple resources allows for greater throughput for large parallel workflows such as those used with COVID and VGP analysis, and periods of high traffic. In order to account to this limitation we will request allocation on all three of Bridges-2 / Expanse / Rockfish for similar workloads.

## **Stampede-2**

We have primarily scheduled long-running single node alignment jobs on *Stampede 2*. These include Bowtie and BWA (tools for mapping sequence reads back to a reference sequence), and HiSat (a tool for mapping reads derived from RNA back to a genome), as well as aligners such as various tools from the BLAST suite. All of these tools have been previously shown to readily scale across cores within a single node. Due to the new ability to access our reference data on HPC systems such as Stampede-2, we have greatly increased our ability to utilize this resource, and exhausted our 2021 allocation for the first time since being awarded time on the resource. Because of this, we are increasing our allocation request for Stampede-2.

  