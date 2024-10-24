# Brief
This is folder is a detailed archive for the procedure, and scripts used in the manuscript, Restoring flowcell type and basecaller configuration from FASTQ files of nanopore sequencing data.


# Content
| Folder | Contents |
| :---: | :---: |
| SRA_status | ONT raw data, flowcell and basecaller version labelling in SRA database |
| ONTsoftware_misuse_configs | Benchmark of Clair3, Shasta, medaka with correct or wrong configs |
| longBow_training | Training, testing, and source code of LongBow |
| longBow_testing | LongBow testing on basecalled labelling dataset and SRA human ONT data |
| LongBowDB | Source code for LongBowDB |
| COGUK | Repeat and reanalysis of COGUK SARS-CoV-2 data |
| Others | Downsamping test, Close Guppy version similarity, SRA fast5 data simplex, duplex |
| Artex_code | Code of Artex |
| longbow_code | Code of LongBow |


# Programming language and software
## Programming language
To run the Python scripts we provided, one should use Python 3.7 or higher version. To run the Matlab scripts we provided, one should use MATLAB 2023a or higer version. The exact versions of programming languages we used were listed below:
| Language | Version |
|:---:|:---:|
| MATLAB | R2023a |
| Python | 3.7.3 |


## Software version
### Basecalling software
Basecalling software used in the manuscript.
| Basecaller | Version | Basecalling mode |
|:---:|:---:|:---:|
| Dorado | 0.4.1, 0.4.3 | FAST/HAC/SUP |
| Guppy6 | 6.4.6, 6.3.8 | FAST/HAC/SUP |
| Guppy5 | 5.0.11 | FAST/HAC/SUP |
| Guppy4 | 4.0.11, 4.2.2 | FAST/HAC |
| Guppy3 | 3.6.1 | FAST/HAC |
| Guppy2 | 2.3.7 | NO MODE |


## Other softwares
### Conda version
Many of the following softwares are installed through `Conda` environment. We have tested Conda version `24.1.2` and version `24.4.0`.
<mark>We strongly recommend Conda version >= `24.1.x` installed.</mark>

### Version list
| Software | Version |
|:---:|:---:|
| Artic | 1.2.4 |
| bcftools | 1.19 |
| Bioawk | 20110810 |
| Chopper | 0.7.0 |
| Clair3 | 1.0.4 |
| Flye | 2.9.3-b1797 |
| hdf5 | 1.12.1 |
| Medaka | 1.11.3 |
| Minimap2 | 2.22-r1101 |
| ont-fast5-api | 4.1.1 |
| pod5 | 0.2.4 |
| seqtk | 1.3-r106 |
| Shasta | 0.11.1 |
| yak | 0.1-r56 |



