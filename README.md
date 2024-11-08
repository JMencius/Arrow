# Arrow
This repository archives the pipelines and source codes used in the LongBow manuscript.

# Contents
The contents are organized into six main folders. Please feel free to click on any title to view the detailed `README.md`.

1. [SRA_status](./SRA_status/scripts/README.md)

    Assessment of the availability and metadata labeling of Oxford Nanopore sequencing data in the SRA database
    - [ONT raw data availability in SRA database](./SRA_status/scripts/raw_ONTdata_search.md)
    - [BAM file availability in SRA datbase](./SRA_status/scripts/sra_bam_availability.md)
    - [flowcell and basecaller version labeling in SRA database](./SRA_status/scripts/README.md)
    - [Random selection of SRA run](./SRA_status/scripts/SRA_random_1000sample.md)


2. [ONTsoftware_misuse_configs](./ONTsoftware_misuse_configs/README.md)

    Benchmark of `Clair3`, `Shasta`, `Medaka` with correct or wrong configs/models
    - [Clair3](./ONTsoftware_misuse_configs/clair3/scripts/README.md)
    - [Shasta](./ONTsoftware_misuse_configs/shasta/scripts/README.md)
    - [Medaka](./ONTsoftware_misuse_configs/medaka/scripts/README.md)

  
3. [LongBow_training](./longbow_training/scripts/README.md)

    Training code of LongBow


4. [LongBow_testing](./longbow_testing/scripts/README.md)

    Testing LongBow on 66 groups of ONT data and human ONT SRA data.



5. [COGUK](./COGUK/scripts/README.md)

    Reanalysis of COGUK SARS-CoV-2 data


6. Others

    Other pipelines in the manuscript
    - [Downsampling evaluation](./Others/downsampling_test/scripts/README.md)
    - [Close Guppy version similarity](./Others/guppy_similarity/scripts/README.md)
    - [SRA fast5 data simplex and duplex percentage](./Others/sra_simplex_duplex/scripts/README.md)



# Requirement
## OS requirement
Codes were tested on _Linux_ operating systems. The following release is tested.
Linux: Redhat Enterprise Linux 8
Linux: Ubuntu 22.04.1


## Software requirement
### Conda version
Most of the following softwares are installed through `Conda` environment. We have run test on Conda version `24.1.2` and version `24.4.0`.
<mark>We strongly recommend installing Conda version >= `24.1.x`.</mark>

### Programming language
To run the Python scripts we provided, Python 3.7 or a higher version is required. 

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



