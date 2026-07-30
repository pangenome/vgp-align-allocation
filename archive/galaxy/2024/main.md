# **The Galaxy ACCESS-CI Gateway 2024/25 allocation**

Anton Nekrutenko, Penn State University

Michael Schatz, Johns Hopkins University

Nate Coraor, Penn State University

Enis Afgan, Johns Hopkins University  
Philip Blood, Pittsburgh Supercomputing Center

  

# **1. Summary**

  - Galaxy (<https://usegalaxy.org>) is a Science Gateway that supports tens of thousands of users and hundreds of thousands of individual analyses each month, primarily performing analysis of Genomic Data. It has been freely available to researchers since 2006, and supported by an XSEDE/ACCESS-CI allocation since 2015.
  - The Galaxy gateway utilizes ACCESS-CI resources both to run types of analysis that cannot be supported without specialized resources (highly parallel long running jobs on Stampede 2, large-memory jobs on Bridges-2) as well as burst capacity (through Jetstream 2)
  - Galaxy uses ACCESS-CI infrastructure to develop, maintain, and deploy data analysis workflows that are directly relevant to the current efforts aimed at understanding infection dynamics and pathogenicity of the SARS-CoV2, MonkeyPox, Influenza, HIV, and other human pathogens. Starting in 2022 Galaxy has become the first and only publicly available resource allowing any researcher to perform assembly of large eukaryotic genomes. ACCESS-CI resources allow these practices to be universally accessible to anyone and provide an open, standardized, scalable, and reproducible analysis environment. 
  - For the 2024/25 allocation year we are requesting (all projected from current usage, and justified in detail below):
      
      - IU JetStream2 CPU: 5M SUs
      - IU JetStream2 Large Memory: 4M SUs
      - IU JetStream2 GPU: 200K SUs
      - IU JetStream2 Storage: 200 TB (200K GB)
      - PSC Bridges-2 RM: 1.5M SUs
      - PSC Bridges-2 EM: 100K SUs
      - PSC Ocean: 20 TB (20K GB)
      - SDSC Expanse CPU: 1.5M SUs
      - SDSC Expanse Storage: 20 TB (20K GB)
      - Purdue Anvil CPU: 1.5M SUs
      - TACC Stampede3: 500K SUs (node hours)
      - TACC Ranch: 4 PB (4M GB)

# **2. Background**

In reading this document you will find similarities to the previous allocation cycle. This is because fundamentally our mission did not change: we support a vibrant community of users performing various types of data analyses. What has changed is demand. Our successes in the areas of genome assembly and protein folding has brought us even more users. All this makes us even more dependent on fantastic resources provided by ACCESS-CI. Aside from that we have a new exciting research area that will dramatically benefit from this allocation: generation of whole genome alignments across hundreds of newly sequenced genomes. See section 3.3. 

## **2.1 Intended communities and anticipated impact (also see 2.5)**

The success of biological research depends on the ability of all participants, regardless of their expertise, to take maximum advantage of the available data. To be successful, our project needs to precisely identify the participants, assess their needs, and enable their collaboration. For example, sequencing and genomics employ “traditional” bioinformatics techniques, while evolutionary dynamics and epidemiology involves interpretation of variation and phenotypic data in population context using statistical approaches. Similarly, genomic data science draws extensively from developments in statistics and informatics, while social and educational aspects of pandemic research rely on effective dissemination and instructional efforts. After analysis methods and algorithms are defined, software development is needed to implement them as robust and efficient computational tools accessible to experimentalists. Finally, data need hardware and software to be stored and analyzed. This requires system design and administration. Such logic points to three communities driving biomedical research:

**Biomedical and clinical researchers** have the knowledge necessary for the formulation and testing of hypotheses and for translation of research results into clinical practice. These are individuals ranging from “wet” bench molecular biologists to “dry” evolutionary biologists and epidemiologists with quantitative training. *Our system addresses the needs of this community by providing a platform that allows experimentalists to analyze complex datasets using a GUI while providing programmatic access to simultaneously satisfy needs of computational researchers and bioinformaticians.*

**Tool and workflow developers** are individuals with quantitative degrees solving algorithmic challenges and producing specialized software as well as technicians responsible for data processing at institutional bioinformatics facilities. *Galaxy provides a platform for tool deployment and integration. Any new or existing command-line or web-based tool can be readily integrated into Galaxy and made available to thousands of users.*

**Educators** are high school, college, university, and industry instructors who develop and maintain training materials, deliver training sessions, and organize training events. They need to be able to access a wide variety of data and tools and provide the opportunity for their trainees to perform hands-on analyses. *A portfolio of training materials covering a wide variety of topics will be further expanded and supported by a community of trainers who will ensure that its content is up-to-date. In addition, we will provide a mechanism to deploy and configure computational infrastructure necessary to run interactive workshops.* 

## **2.2 Enabling data intensive biological research**

The Galaxy team develops software infrastructure for deploying Galaxy instances. An instance of Galaxy is an application that allows users to apply a wide variety of command-line, web-based, or interactive tools to any type of data through a web-browser (or programmatically via application programming interface \[API\]). There are three major global Galaxy instances in US [\[1\]](https://paperpile.com/c/UoC9br/zPjp0), EU [\[2\]](https://paperpile.com/c/UoC9br/02eIQ), and Australia [\[3\]](https://paperpile.com/c/UoC9br/BM1XR) in addition to regional instances (see [\[4\]](https://paperpile.com/c/UoC9br/lTouU)). This constellation of instances (collectively known as usegalaxy.\*) serves tens of thousands of researchers worldwide each month. The US (and Americas in general) are served by the US instance [\[5\]](https://paperpile.com/c/UoC9br/N9FZE). It operates from the Texas Advanced Computing Center (TACC) and has access to a variety of ACCESS-CI resources. It performs \~750,000 analyses per month for \~7,500 monthly users. A Galaxy instance can be configured to manage local or remote computational resources to schedule tool runs on any modern computational infrastructure including local hardware, conventional clusters, and commercial or public clouds if the use of existing public instances is impractical due to, for example, data privacy concerns. Table 1 lists examples of functionalities that Galaxy brings to the three communities described in 2.1 above.

|  |  |
| :-: | :-: |
| \*\*Table 1\*\*. Galaxy impact four communities driving biomedical research  |  |
| \*\*Community\*\* | \*\*An example usage scenario\*\* |
| Biomedical and clinical researchers | A researcher has 1,000 fastq files containing Illumina reads from individuals infected with virus X. She needs to identify which strains of the virus X are present in the samples. She uploads all data to a Galaxy instance (either public or institutional). From Galaxy’s graphical interface she invokes a variant calling workflow that returns a list of variants. All analyses are performed on infrastructure that Galaxy provides. She can use workflow as-is or modify any steps, explore new tools, experiment with their options, and create new workflows (Example: \[\\\[6\\\]\](https://paperpile.com/c/UoC9br/lA55F)). |
| Tool and workflow developers | A tool developer created a new tool for analysis of sequence data. He needs to put this tool into use with his experimental colleagues. He can create a BioConda package or software container with the tool and quickly deploy it on public or institutional Galaxy. His experimental colleagues will be able to readily use this tool. Galaxy will provide necessary infrastructure, interface components, and execution environment (Example: \[\\\[7\\\]\](https://paperpile.com/c/UoC9br/YZ3BL)). |
| Educators | A research group involved in pathogen research is performing routine surveillance of sewage samples. Only a few individuals are familiar with data analysis principles and none is familiar with metagenomics. Galaxy's portfolio of tutorials can be used to run training events ranging from one day to week-long courses (Example: \[\\\[8\\\]\](https://paperpile.com/c/UoC9br/CHR8X)). |

  

A detailed description of Galaxy operation is outside the scope of this allocation request. However there is a comprehensive collection of tutorials covering all aspects of Galaxy from basic functionality to advanced analyses [\[9,10\]](https://paperpile.com/c/UoC9br/cICS5+eJiC6). It is an excellent resource for learning about Galaxy.

## **2.3 Development of the Galaxy ACCESS-CI Gateway**

The main goal of Galaxy has been the development of software that enables any genomics researcher to perform complex computational analyses by hiding technical complexities associated with management of underlying programs and high-performance compute infrastructure. However, as a direct consequence of our initial success we reached a point where it became difficult to sustain the potential growth of analysis load and associated biological data storage on our public servers. To address this we initially worked with our colleagues at TACC to move the Galaxy main instance to their more robust compute and storage infrastructure. This was highly successful, but also offered the opportunity to expand both the number of jobs we could allow users to run, and also offer new types of analyses by integrating with XSEDE resources. To implement this, in 2014 we requested an XSEDE Gateway allocation aimed at establishing a national computational biology gateway. During the first two years of the award, we made significant progress developing Galaxy support for scheduling on XSEDE resources. This included support for scheduling Galaxy jobs on Stampede (and now Stampede 2) and Blacklight (and now Bridges), as well as a resubmission scheme for moving jobs to appropriate resources based on run time. We have demonstrated the ability to effectively use substantial amounts of allocated ACCESS-CI resources to advance our users' scientific research (Fig. 1).

We have had particular success with scheduling jobs on Jetstream2. Because Jetstream2 is a cloud-style system we have been able to rapidly move a number of different types of analyses with minimal modification to our software stack. We have also leveraged Jetstream2 and containers to enable a Galaxy feature – Interactive Galaxy Tools – which allow users to work with their Galaxy data in programming environments such as Jupyter. We have also had substantial uptake in usage of Bridges, which is particularly well suited to genome and transcriptome assembly problems. 

## **2.4 Resource Usage and Control**

Galaxy contains functionality for both monitoring and controlling resource usage which will allow efficient allocation of ACCESS-CI resources to end users of the Galaxy service. Fine-grained limits can be placed on the “destination” of a Galaxy job, meaning that users can be prevented from over-utilizing a specialized ACCESS-CI resource while not hindering them from using other resources (such as Galaxy’s dedicated cluster at TACC). These limits come in multiple forms. We can control the concurrency of jobs on a particular resource or with a set of parameters, such as only allowing a single “big memory” job for a user at a time, or only four nodes on Stampede, etc. We can also redirect jobs to specific resources or reject them entirely if a user has reached a configured job threshold. The use of XSEDE/ACCESS-CI resources has made it possible to expand the type of jobs enabled on the Galaxy gateway to multi-core jobs that require up to an order of magnitude more CPU time. The combination of Jetstream, Stampede, and Bridges offers a well-rounded pool of resources that the dedicated Galaxy cluster could not satisfy.

**Figure 1**: Key usage statistics of https://usegalaxy.org running on ACCESS-CI resources. User statistics per month (green = active users per month; red - new registrations) and Jobs executed per month (blue) on the main public Galaxy instance https://usegalaxy.org. Both the number of users and the number of analyses being executed continue to increase. 

Currently data storage for Galaxy Main is hosted by TACC. Galaxy has a data accounting and quota system that pauses a user’s analysis if their data usage exceeds a defined limit (currently set at 250 GB). The data quota is one of the factors that limits the Galaxy service’s usability in its current state. To enable larger genomic analyses, we grant users a limited-time increase to 1 TB for the completion of a specific project. As of July 2022 the Galaxy main site has accumulated \~5.0Pb Petabytes (PB) of user data. These data are stored at the Texas Advanced Computing Center (TACC) Corral system, effectively occupying over 10% of its total capacity.  This allocation has been previously subsidized by the iPlant/Cyverse program, which has been discontinued. As a result the current Galaxy installation at TACC is simply not sustainable in the long run. To address these issues and to pave the way towards sustainable management of user data while granting users enough storage to perform meaningful analysis we are collaborating with TACC on adopting Galaxy to take advantage of tiered storage architecture (Currently funded NSF Proposal 1929694 “CIBR: Collaborative Research: Providing sustainable Galaxy service on XSEDE resources”). We have made significant progress in implementing tiered storage in Galaxy. To take advantage of tiered storage we are requesting 4Pb allocation on the Ranch system for archival purposes. This would significantly decrease our footprint on the Corral system. Note that substantial progress has been made in advancing the goals of this proposal as can be seen in [\[11\]](https://paperpile.com/c/UoC9br/1TJLx). 

## **2.5. New communities for new allocation**

While the bulk of the Galaxy usage continues to be in the biological domain, we are seeing increasing usage of the Galaxy platform in diverse non-biological applications. Below we are including a set of new non-biological scientific driving projects that would influence the development of platforms and its usage in the new allocation period (Table 2). These projects are organized by broad disciplines. Each section contains (1) a short description of the project, (2) how it will use proposed infrastructure, and (3) which communities will use it. In each case we will ensure that necessary tools are contained with Biocontainers registry [\[12\]](https://paperpile.com/c/UoC9br/v2uNC), assemble them into workflows, and ensure that workflows can be executed from GUI, CLI, and Notebook environments. 

|  |
| :-: |
| \*\*Table 2\*\*. New scientific use drivers for 2022/23 allocation period.  |
| \*\*Ecology and Climate\*\* |
| \*\*Analysis of terrestrial ecosystems.\*\* \*Description\*: Terrestrial ecosystem models have been widely used to study the impact of climate changes on vegetation and terrestrial biogeochemical cycles in the climate modeling community. They are also more and more applied in ecological studies to help ecologists to better understand the processes. But the technical challenges are still too high for most of the ecologists to use them. Using Galaxy infrastructure we will deploy workflows for terrestrial ecosystem analysis and comprehensive analysis with the Pangeo framework \[\\\[13\\\]\](https://paperpile.com/c/UoC9br/dRxIf). \*Infrastructure utilization\*\*:\* Climate and ecological analyses utilize infrastructure typical for big data manipulation including clusters and clouds with conventional nodes. \*Target communities:\* This work will be targeted and conducted together with the Pangeo community for big data geoscience.  |
| \*\*Citizen science assessment of biodiversity.\*\* \*Description\*: Ecology and climate communities have recognized the Galaxy platform as versatile software that can easily be adapted to their analytical needs and they created respective flavors of Galaxy \[\\\[14\\\]\](https://paperpile.com/c/UoC9br/SYGgS). Galaxy-E is an initiative to help biodiversity oriented citizen science projects to share data, tools, and analytical processes. \*Infrastructure utilization\*\*:\* The current initiative is being used to tackle processing of remote sensing data from the Sentinel 2 mission, using Geographical Information System (GIS) data, or managing netCDF treatment. Similarly, the community around the Galaxy Climate flavor has integrated their own toolsuites for the growing needs of its community. \*Target communities:\*  Galaxy Climate community |
| \*\*Machine learning\*\* |
| \*\*Development of ML workbench and adoption of specialized hardware.\*\* \*Description\*\*\*:\*\* This work will focus on training machine learning models, creating model catalogs, and increasing their accessibility to a variety of users, helping democratize availability of this fast-moving field. \*Infrastructure utilization\*\*:\* To achieve these goals we will work on making ARM-based infrastructure available for building and testing ML-tools images from Biocontainers registry to allow more of ACCESS-CI infrastructure to be utilized by Galaxy. Separately, Galaxy is exploring the use of quantum computing in life sciences. Initial work has been done in incorporating Qiskit into Galaxy, IBM’s python-based software stack for quantum computing. It is expected this technology will initially have the most influence on protein structure prediction so we have been developing a full biophysics workflow for Galaxy as a way to learn and educate others about the transformative potential this technology will have for domain scientists. \*Target communities:\* Growing number of fields directly benefiting from ML approaches including biology, climate, NLP, and others.  |
| \*\*Chemistry\*\* |
| \*\*Cheminformatics.\*\* \*Description\*\*\*:\*\* A set of one hundred cheminformatics tools has been integrated into Galaxy to enable researchers easy-to-use, reproducible, and transparent access to computational chemistry software libraries and drug discovery tools \[\\\[15\\\]\](https://paperpile.com/c/UoC9br/lbAJp). It includes applications for similarity and substructure searches, clustering of compounds, prediction of properties and descriptors, filtering, and many other tools that range from drug-likeness classification to fragmentation and fragment-merging. Infrastructure utilization: high energy synchrotron X-ray diffraction and imaging techniques continue to push the limits of what can be captured spatially and temporally in evolving microstructures, leading to massive datasets (\\\>Tbs) and complex data reduction and analysis workflows that require substantial computing resources. \*Target communities\*: Most first-time users from the structural materials science community are not prepared for the magnitude of scientific computing expertise required to complete data reduction and analysis in this field. The community has adopted Galaxy, integrated tools, and developed synchrotron-centric data workflows. We will continue working with partners and relevant community leaders to deploy chemistry and materials science flavors of Galaxy as part of Galaxy service. |
| \*\*Material science\*\* |
| X-ray imaging of microstructures. \*Description\*. Over the last 3 years, the X-ray Imaging for Microstructures Gateway (XIMG) based on the Galaxy framework was developed and deployed for the structural materials science community at the Cornell High Energy Synchrotron Source (CHESS). The advanced X-ray diffraction and imaging techniques at synchrotron facilities can resolve the three-dimensional microstructural and micromechanical state of crystalline materials. These techniques capture data at sufficient speed and resolution to observe structural responses at the sub-micron scale for materials subjected to thermal, mechanical, or other types of loading. \*Infrastructure utilization.\* These information-rich datasets are of increasingly high demand but come at the cost of unprecedented data sizes (\\\>TBs of data for a single experiment) – challenging to analyze and curate except by a very small number of experts. \*Target communities\*: Material science, X-ray imaging, Imaging |

  

# **3. Request Justification**

Reviewers will note that in this application we request a larger allocation compared with previous years. The chief reason for this increase is the sheer amount of data generated by two new initiatives: our infectious disease monitoring efforts and our partnership with Vertebrate Genome Consortium (VGP) as well as the new whole genome alignment generation effort. The three initiatives represent two extremes of current biological computation. The infectious disease analysis involves processing thousands of relatively small datasets, while VGP and whole genome alignment generation involves manipulation of a few very large datasets. 

## **3.1 Continuing pandemic/infectious disease analytics efforts**

First, we are continuing our active involvement in the global infectious disease analysis efforts [\[16\]](https://paperpile.com/c/UoC9br/RBvjh). In essence, we are providing a global resource enabling researchers to (1) analyze very large sequencing datasets on public computational infrastructures in a matter of hours, and (2) transform outcomes of these analyses into publishable results by incorporating current information about emerging deseases.  As the need for active monitoring of emerging variants is becoming more acute we expect that the amount of available sequencing and epidemiological data will grow exponentially.  Second, we commenced new efforts directed toward analyses of other pathogens such as MonkeyPox (see <https://galaxyproject.org/projects/mpxv/>). These efforts will concentrate on developing a variety of workflows for analysis of different pathogens including Influenza, HIV, Newcastle virus, Avian flu and others. These workflows will be accessible to thousands of researchers worldwide as a result of this allocation request.

## **3.2 Vertebrate Genome Project**

VGP is a global effort (phase 1 includes over 70,000 species with global distribution). As such the ability to analyze and assemble sequencing data must also have global reach. At this time VGP uses DNAnexus as the primary analysis environment. This effectively prevents utilization of VGP analysis workflows by the global community. The advances in sequencing technologies (such as HiFi approach from PacBio and further refinement of Oxford Nanopore Technology) allow assembly of human-sized genomes using machines with \~1Tb of RAM or less (For example, HiCanu, a state of the art genome assembly tool, can assemble a human genome in \~4,000 core hours with 128 GB of RAM. Peregrine can perform assembly in \~100 core hours with 500GB of RAM). The infrastructure available via ACCESS-CI allocations will allow us to keep up with the demand and, most importantly, create the first public resource allowing assembly of large genomes on the web\! **As of July 2024 we have assembled over 150 new vertebrate genomes using Galaxy workflows deployed on ACCESS-CI infrastructure (see** [**https://galayxproject.org/projects/vgp**](https://galayxproject.org/projects/vgp)**).** A manuscript describing this effort has been published in *Nature Biotechnology* [\[17\]](https://paperpile.com/c/UoC9br/hSZ6).

## **3.3. Computing whole genome alignments across hundreds of eukaryotic genomes**

Existing comparative genomic approaches (such as those stemming from generation of hundreds of genomes by efforts like VGP described above)  that are meant to scale to hundreds of eukaryote scale genomes are based on phylogenetic guide trees. The use of these guide trees can bias our ability to understand incomplete lineage sorting, which is of particular relevance to clades where rapid radiation obscures and complicates any direct phylogenetic analysis. In order to build an unbiased perspective on evolution across the vertebrate clade, we are using the Galaxy allocation on Stampede3 and Expanse to compute a direct all-to-all alignment of the vertebrate genomes. Because the alignment task is fundamentally quadratic, this requires substantial resources that have been enabled by TACC. Our initial estimates, based on completion of 10% of the task, suggest that we will require around 5 million CPU hours to complete one iteration of the all-to-all alignment of 477 high quality genome assemblies. The indexes required for the initial homology mapping require around 7TB of disk space, which has been easy to achieve due to the flexible scratch storage on stampede3. We estimate the output alignment will require around 10-15TB. In 2024-2025 we hope to greatly extend these analyses. We hope to combine the existing VGP with the human pangenome reference consortium (HPRC) near-telomere-to-telomere human assemblies, which will nearly double the size of the genome set. Additional inclusion of a pangenome for chimpanzee and bonobo plus inclusion of other near-VGP quality genomes will yield a near quadrupling of the genome set. The quadratic nature of the unbiased alignment approach we are pursuing suggests a factor of 10-20x increase in compute requirements. Alongside this work in vertebrates, we will begin two new studies to explore similar approaches in prokaryotes (bacteria) and plants, albeit at a smaller scale. We estimate we would require an allocation of 5 million SU to explore this new research space through multiple iterations and refinement of the analysis. We additionally will require storage and publicly accessible web endpoints for dissemination of the unprecedented comparative and population genomic resources which we will products. We expect this work to result in several new results including: 1) unbiased view on phylogeny and incomplete lineage sorting across all assembled genomes, 2) a resource (based on "implicit" pangenome graphs, [github.com/pangenome/impg](http://github.com/pangenome/impg)) that researchers can use to subset alignments by target genome region for any genome in our set, 3) ancestral allele assignment for all letters in all the human genomes in the HPRC, 4) complete perspective on concerted evolution of multi-copy gene families which recent research suggests are of crucial importance to human phenotypes and disease. 

 **Note** that the two new efforts described above are in addition to our normal user load, which also continues to grow (Fig. 1). 

# **4. Galaxy community allocation**

Given the large and active community currently using the main Galaxy instance, there is already very high demand for the additional resources and capabilities provided by ACCESS-CI. During the previous allocation cycle we made *all* Galaxy jobs runnable on ACCESS-CI resources. Based on this increasing traffic, participation in activities mentioned above, and current ACCESS-CI utilization, we are making the following requests for 2024/25:

**Jetstream-2 CPU: 5,000,000 SUs** to maintain a pool of virtual machines of various sizes for short running high-throughput jobs. This is an increase from our previous request and is a projection based on current, awarded supplement, and expected usage. We have developed a system to scale out Jetstream-2 usage for workshops that will result in an increase in usage during the next year. This allocation will enable the absolute majority of multi-core Galaxy jobs such as mapping sequencing reads against reference genomes (core activity of our pandemic monitoring efforts).

**Jetstream-2 Large Memory: 4,000,000 SUs** to enable assemblies of large genomes such as those of plants and animals with higher ploidy. These organisms have a genome that can be many fold larger than that of the human and require a large amount of RAM. Specifically, our Jetstream-based assembly-specific Galaxy instance at <https://vgp.usegalaxy.org> will be utilizing these resources. 

**Jetstream-2 GPU: 200,000 SUs** to enable running of tools providing native GPUs support. This would be particularly important for our ability to analyze Oxford Nanopore Datasets (ONT) as many software tools for the analysis of ONT data (e.g., base calling, DNA and RNA modification detection) rely on access to GPUs.

**Stampede 2:** **10,000 SUs (node-hours)** for long running parallel jobs. This is no change from the amount of our previous year’s request, and projected from our current usage. 

**PSC’s Bridges-2 Regular Memory:** **1,500,000 SUs** for medium-memory assembly jobs, in particular genome and transcriptome assembly. 

**PSC’s Bridges-2 Expanded Memory:** **100,000 SUs** for large-memory assembly jobs, in particular genome and transcriptome assembly.

**UCSD Expanse**: 1,500,000 SUs to support additional capacity for generation of multiple-genome alignments. 

**TACC Ranch: 4 Pb** for transitioning to tiered storage and decreasing our current Corral footprint.

**Purdue Anvil:** **1,500,000 SUs** to support additional capacity for large-memory jobs when capacity is reached on Bridges-2, Expanse, and Stampede-2.

Below we explain these allocation requests in detail.

## **4.1 Jetstream-2**

Genomic analyses tend to be quite “bursty” in nature, meaning that resource requirements can change dramatically depending on the type of analysis, or even within the steps of a single analysis workflow. Consequently, the “elasticity” offered by cloud computing environments matches very well with the needs of genomic researchers. 

As proposed previously, we have successfully integrated Jetstream into the Galaxy gateway. To do so we utilized the CernVM File System (CVMFS) to allow Galaxy’s shared static data to be easily used from VMs running at TACC or IU. Galaxy Main (<https://usegalaxy.org>) is using up to 32 “large” VMs to support job execution, four “medium” VMs for infrastructure (Slurm, CVMFS, and NFS servers), and one “medium” VM to support interactive environments. Dataset Collections in Galaxy allow users to map tools over hundreds-to-thousands of datasets. An increase in the usage of dataset collections and identifying more multicore-capable tools has increased the amount of bursting performed on Galaxy in the past year. 

## **4.2 Stampede 2**

During the first two years of the Galaxy ACCESS-CI gateway we demonstrated the ability to reschedule long-running Galaxy jobs to stampede. Stampede can accommodate longer running jobs, at the expense of longer initial wait times; job resubmission balances these concerns. 

**Example analysis: Mapping assembly of RNA-seq reads using Cufflinks/Tophat and HiSat/StringTie:** This workflow aligns reads to a reference genome and assembles RNA transcripts from the reads. This workflow is well-suited to distributed-memory systems. This continues to be one of the most popular analyses on Galaxy main. Integration with ACCESS-CI resources will significantly reduce the turnaround time for researchers doing these analyses. Similar types of analysis include large genome mapping jobs (e.g. mapping with BWA and Bowtie) and large metagenomic jobs (e.g. Kraken analysis of taxonomy). **In 2022 as well as in 2023 RNA seq analyses remained the most popular types of non-COVID19 related jobs run on the main Galaxy instance.** Based on current usage levels for Stampede 2 we anticipate using 10,000 node hours on Stampede 2 in the next allocation period. 

## **4.3 Bridges-2 / Expanse / Anvil**

These three resources are equally well suited for performing large genome and transcriptome assembly jobs. However, considering the large and continuously growing number of Galaxy users, the queue limits (\~15-20 active jobs on many systems) make large amounts of SUs on one system not as usable. Instead we will be spreading these jobs across the three resources to increase usability and improve user experience.

With the retirement of the Bridges phase 1 large shared memory (LSM) nodes, we request time on the Regular Memory nodes of the Bridges-2 system at PSC. These nodes are ideal for de novo assembly applications but do not generally require more than 10-20 cores per job.

## **4.4. Example of analyses enabled by this allocation**

**4.4.1. Example analysis 1:** ***de novo*** **assembly of RNA-seq reads using Trinity.** This workflow assembles RNA-seq reads *de novo*, without any reference genome, into RNA transcripts.   Taking a *de novo* assembly approach allows researchers to study many more species (i.e. “non-model organisms”) than would otherwise be possible, since quality reference genomes have been produced for relatively few species. Trinity, which is widely recognized as the state-of-the-art tool for *de novo* transcriptome assembly, requires large shared memory systems. Hence, Trinity jobs will be directed to Bridges-2 RM or EM based on the estimated amount of memory required.

**4.4.2. Example analysis 2:** ***de novo*** **assembly of viral and bacterial genomes at scale.** Metatranscriptomic data from individual COVID-19 patients is often used to create independent assemblies of the viral genomes. Such datasets are often large with multiple millions of sequencing reads. Galaxy on ACCESS-CI resources are used to perform viral and bacterial pathogen assemblies using Unicycler software that benefits from having large memory**.** 

  

|  |
| :-: |
|  |
| \*\*Figure 2.\*\* A set of 10 prototype workflows for the assembly of genomes using PacBio HiFi data. Stages 1 - 5 correspond to the first five rows of Tab. 1. Eight analysis trajectories are possible depending on the combination of input data. Decision on invocation of workflow 6 is based on the analysis of QC output of  workflows 3, 4, or 5 (see Supplemental data for full explanation). Thicker lines connecting workflows 7, 8, and 9 represent the fact that these workflows are invoked separately for each phased assembly. The first stage of the pipeline is generation of \*k\*-mer profiles for estimation of genome size, heterozygosity, repetitiveness, and error rate necessary for parameterizing downstream workflows. \*K\*-mer counts can be generated from HiFi data only (Workflow 1) or include data from parental reads for trio-based phasing (Workflow 2). The second stage is the contig assembly. In addition to using only HiFi reads (Workflow 3), the contiging step can leverage HiC (Workflow 4) or parental read (Workflow 5) data to produce better-phased initial hap1/hap2 or parental/maternal assemblies. The contiging workflows also produce a number of critical quality control (QC) metrics such as \*k-\*mer multiplicity profiles \[\\\[18\\\]\](https://paperpile.com/c/UoC9br/foTmT). Inspection of these profiles provides information necessary for deciding whether the third stage—purging—is required. Purging (Workflow 6) identifies and resolves haplotype-specific assembly segments incorrectly labeled as primary contigs as well as heterozygous contig overlaps increasing continuity and quality of final assembly \[\\\[19\\\]\](https://paperpile.com/c/UoC9br/ITHrV). The purging stage is generally unnecessary if HiC or Trio data is available. The fourth stage, scaffolding, produces chromosome-level scaffolds using information provided by optical mapping (BioNano, Workflow 7) and HiC (Workflow 8) data. The final stage of nuclear genome assembly is the decontamination procedure (Workflow 9) designed to remove exogenous (e.g. viral and bacterial) sequences. An additional dedicated workflow (Workflow 0) is tailored to  mitochondrial genome assembly.  |

**4.4.3. Example analysis 3:** ***de novo*** **assembly of a large vertebrate genome.** This is a state of the art workflow designed in collaboration with VGP consortium. It is entirely based on long reads generated by Pacific Biosciences (PacBio) HiFi process (Fig. 2) and relies on our Bridges 2 allocation. This workflow accepts three inputs representing three distinct types of data necessary for accurate assembly: (1) PacBio HiFi reads, (2) optical maps generated with BioNano technology, and (3) genome adjacency data generated with HiC protocol. It produces final assembled sequences suitable for genome annotation. 

# **5. Metrics for success**

## **5.1. Usage monitoring**

We propose similar metrics as for the previous years of the proposal. As we have now performed most of the integration for three of the five resources we are requesting, we expect to increase availability:

First, increase the amount of time that submission/resubmission to ACCESS-CI resources is enabled. For *Stampede 2*, *Bridges*, and *Jetstream* we will target 95% time enabled, which we expect to easily meet since testing is complete. 

Second, we would like to continue to increase the number of users whose jobs are able to run on ACCESS-CI, by analyzing usage patterns and identifying additional tools that can benefit from ACCESS-CI. There is considerably less room for improvement on these metrics as we have already been quite successful in moving analysis. However with improvements in job prediction and resubmission we are targeting increasing the number of jobs sent to ACCESS-CI by 50%.

## **5.2. Assessing usability by soliciting feedback** 

The project combines software development with resource maintenance and administration efforts. The quality assurance aspects of the software process including version control, continuous integration, team coordination, and testing. To ensure the quality of our public site we employ continuous monitoring as well as the communication channels described above. These support channels provide a reliable way to identify pain points that are experienced by multiple users. Errors arising during execution of Galaxy tools are reported using a built-in mechanism. This mechanism allows users to provide additional details about the error they experience. All training materials contain built-in questionnaires to provide us with feedback.

## **5.3. Support and communication**

Our online forum was moved to a Discourse-based platform and mailing lists have been replaced with Galaxy Gitter channels for conversational discussion. Both shifts make Galaxy more welcoming and engaging. News is communicated primarily through Galaxy Newsletters and Twitter (@galaxyproject, \>13,700 followers). Other communication channels include the Galaxy News feed [\[20\]](https://paperpile.com/c/UoC9br/I1DrU), the Galactic Blog [\[21\]](https://paperpile.com/c/UoC9br/vaKwA), and the Galaxy Events calendar [\[22\]](https://paperpile.com/c/UoC9br/UkRoV), all of which are promoted on Twitter and in the newsletters. All are part of a larger effort—the Galaxy Community Hub [\[23\]](https://paperpile.com/c/UoC9br/YXMhL).

# **References**

1\.  [Galaxy \[Internet\]. \[cited 2022 Feb 12\]. Available from: ](http://paperpile.com/b/UoC9br/zPjp0)<https://usegalaxy.org>

2\.  [Galaxy \[Internet\]. \[cited 2022 Feb 12\]. Available from: ](http://paperpile.com/b/UoC9br/02eIQ)<https://usegalaxy.org.au>

3\.  [Website \[Internet\]. Available from: ](http://paperpile.com/b/UoC9br/BM1XR)<https://usegalaxzy.org.au>

4\.  [Galaxy Platform Directory: Servers, Clouds, and Deployable Resources - Galaxy Community Hub \[Internet\]. \[cited 2022 Feb 12\]. Available from: ](http://paperpile.com/b/UoC9br/lTouU)<https://galaxyproject.org/use/>

5\.  [Galaxy \[Internet\]. \[cited 2022 Feb 12\]. Available from: ](http://paperpile.com/b/UoC9br/N9FZE)<https://usegalaxy.org>

6\.  [Galaxy Training: Mutation calling, viral genome reconstruction and lineage. \[Internet\]. \[cited 2022 Feb 17\]. Available from: ](http://paperpile.com/b/UoC9br/lA55F)<https://training.galaxyproject.org/training-material/topics/variant-analysis/tutorials/sars-cov-2-variant-discovery/tutorial.html>

7\.  [Building Galaxy Tools Using Planemo — Planemo 0.75.0.dev0 documentation \[Internet\]. \[cited 2022 Feb 17\]. Available from: ](http://paperpile.com/b/UoC9br/YZ3BL)<https://planemo.readthedocs.io/en/latest/writing_standalone.html>

8\.  [Teaching and Hosting Galaxy training \[Internet\]. \[cited 2022 Feb 17\]. Available from: ](http://paperpile.com/b/UoC9br/CHR8X)<https://training.galaxyproject.org/training-material/topics/instructors/>

9\.  [Batut B, Hiltemann S, Bagnacani A, Baker D, Bhardwaj V, Blank C, Bretaudeau A, Brillet-Guéguen L, Čech M, Chilton J, Clements D, Doppelt-Azeroual O, Erxleben A, Freeberg MA, Gladman S, Hoogstrate Y, Hotz H-R, Houwaart T, Jagtap P, Larivière D, Le Corguillé G, Manke T, Mareuil F, Ramírez F, Ryan D, Sigloch FC, Soranzo N, Wolff J, Videm P, Wolfien M, Wubuli A, Yusuf D, Galaxy Training Network, Taylor J, Backofen R, Nekrutenko A, Grüning B. Community-Driven Data Analysis Training for Biology. Cell Syst. 2018 Jun 27;6(6):752–758.e1. PMCID: PMC6296361](http://paperpile.com/b/UoC9br/cICS5)

10\.  [Galaxy Training \[Internet\]. \[cited 2022 Feb 12\]. Available from: ](http://paperpile.com/b/UoC9br/eJiC6)<https://training.galaxyproject.org>

11\.  [Website \[Internet\]. Available from: ](http://paperpile.com/b/UoC9br/1TJLx)<https://github.com/search?q=org%3Agalaxyproject+irods&type=commits>

12\.  [da Veiga Leprevost F, Grüning BA, Alves Aflitos S, Röst HL, Uszkoreit J, Barsnes H, Vaudel M, Moreno P, Gatto L, Weber J, Bai M, Jimenez RC, Sachsenberg T, Pfeuffer J, Vera Alvarez R, Griss J, Nesvizhskii AI, Perez-Riverol Y. BioContainers: an open-source and community-driven framework for software standardization. Bioinformatics. 2017 Aug 15;33(16):2580–2582. PMCID: PMC5870671](http://paperpile.com/b/UoC9br/v2uNC)

13\.  [Pangeo — Pangeo documentation \[Internet\]. \[cited 2023 Jun 18\]. Available from: ](http://paperpile.com/b/UoC9br/dRxIf)<https://pangeo.io/>

14\.  [Royaux C, Arnaud E, Sananikone J, Jossé M, Madelin M, Pelletier D, Norvez O, Le Bras Y. Open Science for Better FAIRness: A biodiversity virtual research environment point of view. Pensoft Publishers. Pensoft Publishers; 2022. p. e95110.](http://paperpile.com/b/UoC9br/SYGgS)

15\.  [Bray SA, Lucas X, Kumar A, Grüning BA. The ChemicalToolbox: reproducible, user-friendly cheminformatics analysis on the Galaxy platform. J Cheminform. 2020 Jun 1;12(1):40. PMCID: PMC7268608](http://paperpile.com/b/UoC9br/lbAJp)

16\.  [Baker D, van den Beek M, Blankenberg D, Bouvier D, Chilton J, Coraor N, Coppens F, Eguinoa I, Gladman S, Grüning B, Keener N, Larivière D, Lonie A, Kosakovsky Pond S, Maier W, Nekrutenko A, Taylor J, Weaver S. No more business as usual: Agile and effective responses to emerging pathogen threats require open data and open analytics. PLoS Pathog. 2020 Aug;16(8):e1008643. PMCID: PMC7425854](http://paperpile.com/b/UoC9br/RBvjh)

17\.  [Larivière D, Abueg L, Brajuka N, Gallardo-Alba C, Grüning B, Ko BJ, Ostrovsky A, Palmada-Flores M, Pickett BD, Rabbani K, Antunes A, Balacco JR, Chaisson MJP, Cheng H, Collins J, Couture M, Denisova A, Fedrigo O, Gallo GR, Giani AM, Gooder GM, Horan K, Jain N, Johnson C, Kim H, Lee C, Marques-Bonet T, O’Toole B, Rhie A, Secomandi S, Sozzoni M, Tilley T, Uliano-Silva M, van den Beek M, Williams RW, Waterhouse RM, Phillippy AM, Jarvis ED, Schatz MC, Nekrutenko A, Formenti G. Scalable, accessible and reproducible reference genome assembly and evaluation in Galaxy. Nat Biotechnol. 2024 Mar;42(3):367–370. PMID: 38278971](http://paperpile.com/b/UoC9br/hSZ6)

18\.  [Rhie A, Walenz BP, Koren S, Phillippy AM. Merqury: reference-free quality, completeness, and phasing assessment for genome assemblies. Genome Biol. 2020 Sep 14;21(1):245. PMCID: PMC7488777](http://paperpile.com/b/UoC9br/foTmT)

19\.  [Guan D, McCarthy SA, Wood J, Howe K, Wang Y, Durbin R. Identifying and removing haplotypic duplication in primary genome assemblies. Bioinformatics. 2020 May 1;36(9):2896–2898. PMCID: PMC7203741](http://paperpile.com/b/UoC9br/ITHrV)

20\.  [Galaxy News \[Internet\]. \[cited 2023 May 2\]. Available from: ](http://paperpile.com/b/UoC9br/I1DrU)<https://galaxyproject.org/news/>

21\.  [The Galactic Blog - Galaxy Community Hub \[Internet\]. \[cited 2023 May 2\]. Available from: ](http://paperpile.com/b/UoC9br/vaKwA)<https://galaxyproject.org/blog/>

22\.  [Galaxy Event Horizon \[Internet\]. \[cited 2023 May 2\]. Available from: ](http://paperpile.com/b/UoC9br/UkRoV)<https://galaxyproject.org/events/>

23\.  [Home - Galaxy Community Hub \[Internet\]. \[cited 2023 May 2\]. Available from: ](http://paperpile.com/b/UoC9br/YXMhL)<https://galaxyproject.org>

  