# **The Galaxy ACCESS-CI Gateway 2023/24 allocation: A supplement Request**

# **History Archival**

Since the beginning of 2024, we have made significant progress on our usage of Ranch, archiving a total of 256 TB of user data from Corral over a period of two months (Figure 1). As we have reached our quota, this progress has stopped, however, we have demonstrated an ability to make significant and effective use of this resource.

|  |
| :-: |
|  |
| \*\*Figure 1.\*\* Disk usage on Corral over the beginning of 2024. Archival efforts began on January 17 and the existing quota (0.25 PB) was exhausted on March 6. The amount of data removed from Corral is greater than 0.25 PB due to the use of compression on archives. |

Because Galaxy histories are often small (but numerous), archiving individual histories was not feasible. We thus undertook writing *gxyarchiver* (https://github.com/galaxyproject/gxyarchiver/), a tool for archiving histories out of Galaxy and to Corral. Once a sufficient bulk of history archives are present on Corral, gxyarchiver bundles these into a tar file and writes out a manifest for later reidentification. History archive bundles are appropriately sized as per Ranch performance guidelines, currently approximately 300 TB each. gxyarchiver writes bundles of history archives out to Corral and removes the individual history archives once the bundle is complete. Finally, a *bundle rancher* process copies these to Ranch and removes the bundle upon successful transfer.

# **Scratch Storage**

In addition to our archival efforts, we have developed features to encourage Galaxy users to not leave data behind on permanent storage (Corral) after their analysis is complete. This comes in the form of *Scratch Storage*. Users may now choose whether their data are created in “Long Term” or “Short Term” Storage on Corral. Long term data are kept permanently, with eventual archival to Ranch after a period of inactivity, and are subject to the existing 250 GB quota. Short term data, on the other hand, are removed 30 days after creation but afforded a much larger 1 TB quota, further enabling the types of assembly and downstream analyses discussed in the Main document. As additional space is freed on Corral, we intend to increase the short term quota and decrease the long term quota to further encourage Galaxy users to prefer the storage location where data are automatically cleaned up.

|  |
| :-: |
|  |
| \*\*Figure 2.\*\* Storage selection interface currently present on UseGalaxy.org. |

  