# ONT software misuse config or model

## List of ONT data analysis software with reliance on flowcell types or basecaller configurations
Numerous state-of-the-art algorithms for ONT data analysis such as sequence alignment, error correction, variant calling, haplotype phasing, genome assembly and genome polishing have a direct or indirect reliance on the specific flowcell type and basecaller configuration.

**Evidence of the required information is provided via hyperlinks attached to each software name.**

| Software | Application | Flowcell type | Basecaller type | Basecaller version | Basecalling mode <sup>[1]</sup> | Indirect dependence |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [Minimap2](https://github.com/lh3/minimap2/releases/tag/v2.27) | Sequence alignment | :white_check_mark: |  |  |  |  |
| [HERRO](https://github.com/lbcb-sci/herro) | Error correction | :white_check_mark: |  |  |  |  |
| [Clair3](https://github.com/HKU-BAL/Clair3?tab=readme-ov-file#pre-trained-models) | Variant calling | :white_check_mark:  | :white_check_mark:  | :white_check_mark: | HAC/SUP <sup>[2]</sup> |  |
| [DeepVariant](https://github.com/google/deepvariant) | Variant calling | :white_check_mark:  |  |  |  |  |
| [PEPPER](https://github.com/kishwarshafin/pepper) | Variant calling | :white_check_mark:  | :white_check_mark:  | :white_check_mark: | SUP |  |
| [Dysgu](https://github.com/kcleal/dysgu?tab=readme-ov-file#calling-svs) | Variant calling | :white_check_mark: | | | | |
| [nanomonsv](https://github.com/friend1ws/nanomonsv#get) | Variant calling | :white_check_mark: | :white_check_mark: | :white_check_mark:  | unspecified |  |
| [Medaka](https://github.com/nanoporetech/medaka#models) | Variant calling | :white_check_mark: | :white_check_mark: | :white_check_mark: | FAST, HAC, SUP | |
| WhatsHap | Haplotype phasing | | | | | :white_check_mark: <sup>[3]</sup> |
| [Margin](https://github.com/UCSC-nanopore-cgl/margin#parameter-files) | Haplotype phasing | :white_check_mark: | :white_check_mark: | :white_check_mark:  | unspecified |  |
| HapCut2 | Haplotype phasing | | | | | :white_check_mark: <sup>[3]</sup> |
| LongPhase | Haplotype phasing | | | | | :white_check_mark: <sup>[3]</sup> |
| [Flye/MetaFlye](https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md#oxford-nanopore) | Genome assembly | :white_check_mark: | :white_check_mark: | :white_check_mark: | HAC/SUP |  |
| [Shasta](https://paoloshasta.github.io/shasta/Configurations.html) | Genome assembly | :white_check_mark: | :white_check_mark: | :white_check_mark: | HAC for Guppy4, SUP for Guppy6 | |
| [Canu](https://canu.readthedocs.io/en/latest/tutorial.html) | Genome assembly | :white_check_mark: | | | | |
| [wtdbg2](https://github.com/ruanjue/wtdbg2/blob/master/README-ori.md#for-higher-error-rate-long-sequences) | Genome assembly | | | | | :white_check_mark: <sup>[4]</sup> |
| [MarginPolish](https://github.com/UCSC-nanopore-cgl/MarginPolish) | Genome polishing | :white_check_mark: | | | | |
| [HomoPolish](https://github.com/ythuang0522/homopolish#introduction) | Genome polishing | :white_check_mark: | | | | |
| [Medaka](https://github.com/nanoporetech/medaka#models) | Genome polishing | :white_check_mark: | :white_check_mark: | :white_check_mark: | FAST, HAC, SUP | |

<sup>[1]</sup>  In “Basecalling mode”, “/” means the models might be used interchangeably, while “,” means each mode has a distinct associated model. If a mode is not listed, it means the current version of the software does not explicitly support it.

<sup>[2]</sup> Clair3 uses the same model for the HAC and SUP modes of R9 Guppy 6 data, but uses different models for the HAC and SUP modes of R10 data.

<sup>[3]</sup> These algorithms depend on the outputs of variant callers, which may be influenced by flowcell type or basecaller configuration.

<sup>[4]</sup> Wtdbg2 depends on sequencing error rate, which is influenced by flowcell type and basecaller configuration.


## ONT software performances using the correct and wrong config
We tested three popular ONT data analysis software which required flowcell type or basecaller to select the best model or choose the specific parameter using the widely used `HG002` data. 

The exact version of the tested software is listed below.

| Software | Version | Application | Detail documentation |
|:---:|:---:|:---:|:---:|
| Clair3 | 1.0.4 | variant calling | [Clair3](./clair3/scripts/README.md) |
| Shasta | 0.11.1 | genome assembly | [Shasta](./shasta/scripts/README.md) |
| Medaka | 1.11.3 | genome polishing | [Medaka](./medaka/scripts/README.md) |

## Data
### HG002 basecalled data
Please download the shared `HG002` FASTQ through ScienceDB and decompressed the FASTQ files to the folder `basecalled_data` before conducting ONT software performances evaluation.

<mark> The data is shared through <https://www.scidb.cn/en/detail?dataSetId=b9eca82475a64772a67ec9b7dac2beb3> </mark>

You can follow the instruction [here](../../ScienceDB/README.md) to download the shared data.
