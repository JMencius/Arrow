# LongBow manuscript code
This repository archive the pipeplines and codes in the LongBow manuscript.

# Contents
The contents are organized into eight folders. Please feel free to click on any title to view the detailed `README.md`.

1. [SRA_status](./SRA_status/scripts/README.md)

    Assessment of the availability and metadata labeling of Oxford Nanopore sequencing data in the SRA database
- [ONT raw data availability in SRA database](./SRA_status/scripts/raw_ONTdata_search.md)
- [BAM file availability in SRA datbase](./SRA_status/scripts/sra_bam_availability.md)
- [flowcell and basecaller version labelling in SRA database](./SRA_status/scripts/README.md)
- [Random selection of SRA run](./SRA_status/scripts/SRA_random_1000sample.md)


2. ONTsoftware_misuse_configs

    Benchmark of `Clair3`, `Shasta`, `Medaka` with correct or wrong configs
- Clair3
- Shasta
- Medaka

  
3. LongBow_training

    Training code of LongBow


4. LongBow_testing

    Testing LongBow on 66 groups of ONT data and human ONT SRA data.


5. LongBowDB

    Source code for LongBowDB


6. COGUK

    Reanalysis of COGUK SARS-CoV-2 data


7. Others

    Other pipelines in the manuscript
- Downsampling evaluation
- Close Guppy version similarity
- SRA fast5 data simplex and duplex precentage



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



