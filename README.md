# LongBow manuscript code
This repository archive the pipeplines and codes in the manuscript of LongBow.

# Content
| Folder | Contents |
| :---: | :---: |
| SRA_status | ONT raw data, flowcell and basecaller version labelling in SRA database |
| ONTsoftware_misuse_configs | Benchmark of Clair3, Shasta, medaka with correct or wrong configs |
| LongBow_training | Training code of LongBow |
| LongBow_testing | LongBow testing on basecalled labelling dataset and SRA human ONT data |
| LongBowDB | Source code for LongBowDB |
| COGUK | Reanalysis of COGUK SARS-CoV-2 data |
| Others | Downsamping evaluation, Close Guppy version similarity, SRA fast5 data simplex and duplex |


# Programming language and software
## OS requirement
Codes were tested on _Linux_ operating systems.
Linux: Redhat enterprise linux 8
Linux: Ubuntu 22.04.1


## Software requirement
### Programming language
To run the Python scripts we provided, one should use Python 3.7 or higher version. 

### Conda version
Most of the following softwares are installed through `Conda` environment. We have run test on Conda version `24.1.2` and version `24.4.0`.
<mark>We strongly recommend Conda version >= `24.1.x` installed.</mark>

### Software version list
| Software | Version |
|:---:|:---:|
| Artic | 1.2.4 |
| bcftools | 1.19 |
| Bioawk | 20110810 |
| Chopper | 0.7.0 |
| Clair3 | 1.0.4, 1.0.10 |
| Flye | 2.9.3-b1797 |
| hdf5 | 1.12.1 |
| Medaka | 1.11.3 |
| Minimap2 | 2.26-r1175, 2.28-r1209 |
| ont-fast5-api | 4.1.1 |
| pod5 | 0.2.4 |
| seqtk | 1.3-r106 |
| Shasta | 0.11.1 |
| yak | 0.1-r56 |



