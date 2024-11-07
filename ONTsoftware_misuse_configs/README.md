# ONT software misuse config or models

## ONT softwares which requires flowcell or basecaller info to set the correct config
Numerous state-of-the-art algorithms for ONT data analysis such as sequence alignment, variant calling, haplotype phasing, genome assembly and genome polishing have a direct or indirect reliance on the specific flowcell type and basecaller configuration.

**The proof of the needed information is given in the hyperlink attached to each software name.**

| Software | Application | Flowcell type | Basecaller type | Basecaller version | Basecalling mode | Indirect dependence |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [Minimap2](https://github.com/lh3/minimap2/releases/tag/v2.27) | Sequence alignment | :white_check_mark: |  |  |  |  |
| [HERRO](https://github.com/lbcb-sci/herro) | Error correction | :white_check_mark: |  |  |  |  |
| [Clair3](https://github.com/HKU-BAL/Clair3?tab=readme-ov-file#pre-trained-models) | Variant calling | :white_check_mark:  | :white_check_mark:  | :white_check_mark: | HAC/SUP <sup>[1]</sup> |  |
| [DeepVaraint](https://github.com/google/deepvariant) | Variant calling | :white_check_mark:  |  |  |  |  |
| [PEPPER](https://github.com/kishwarshafin/pepper) | Variant calling | :white_check_mark:  | :white_check_mark:  | :white_check_mark: | SUP |  |
| [Dysgu](https://github.com/kcleal/dysgu?tab=readme-ov-file#calling-svs) | Variant calling | :white_check_mark: | | | | |
| [nanomonsv](https://github.com/friend1ws/nanomonsv#get) | Variant calling | :white_check_mark: | :white_check_mark: | :white_check_mark:  | unspecified |  |
| [Medaka](https://github.com/nanoporetech/medaka#models) | Variant calling | :white_check_mark: | :white_check_mark: | :white_check_mark: | FAST, HAC, SUP | |
| [WhatsHap](https://github.com/whatshap/whatshap) | Haplotype phasing | | | :white_check_mark: |
| [Margin](https://github.com/UCSC-nanopore-cgl/margin#parameter-files) | Haplotype phasing | :white_check_mark: | :white_check_mark: | :white_check_mark:  | unspecified |  |
| [HapCut2](https://github.com/vibansal/HapCUT2) | Haplotype phasing | | | | | :white_check_mark: <sup>[2]</sup> |
| [LongPhase](https://github.com/twolinin/longphase) | Haplotype phasing | | | | | :white_check_mark: <sup>[2]</sup> |
| [Flye/MetaFlye](https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md#oxford-nanopore) | Genome assembly | :white_check_mark: | :white_check_mark: | :white_check_mark: | HAC/SUP |  |
| [Shasta](https://paoloshasta.github.io/shasta/Configurations.html) | Genome assembly | :white_check_mark: | :white_check_mark: | :white_check_mark: | HAC for Guppy4, SUP for Guppy6 | |
| [Canu](https://canu.readthedocs.io/en/latest/tutorial.html) | Genome assembly | :white_check_mark: | | | | |
| [wtdbg2](https://github.com/ruanjue/wtdbg2/blob/master/README-ori.md#for-higher-error-rate-long-sequences) | Genome assembly | | | | | :white_check_mark: <sup>[3]</sup> |
| [MarginPolish](https://github.com/UCSC-nanopore-cgl/MarginPolish) | Genome polishing | :white_check_mark: | | | | |
| [HomoPolish](https://github.com/ythuang0522/homopolish#introduction) | Genome polishing | :white_check_mark: | | | | |
| [Medaka](https://github.com/nanoporetech/medaka#models) | Genome polishing | :white_check_mark: | :white_check_mark: | :white_check_mark: | FAST, HAC, SUP | |

[1] Clair3 uses the same model for the HAC and SUP modes of R9 Guppy 6 data, but uses different models for the HAC and SUP modes of R10 data.
[2] These algorithms depend on the outputs of variant callers, which may be influenced by flowcell type or basecaller configuration.
[3] Wtdbg2 depends on sequencing error rate, which is influenced by flowcell type and basecaller configuration.


<a id="ont-software"></a>
## ONT software performances using the correct and wrong config
We tested three popular ONT data analysis software which required flowcell type or basecaller to select the best model or choose the specific parameter using the popular [HG002](https://github.com/human-pangenomics/HG002_Data_Freeze_v1.0) data. 

The exact version of the tested software is listed below.

| Software | Version | Application | Detail documentation |
|:---:|:---:|:---:|:---:|
| Clair3 | 1.0.4 | variant calling | [Clair3](./clair3.md) |
| Shasta | 0.11.1 | genome assembly | [Shasta](./shasta.md) |
| Medaka | 1.11.3 | genome polishing | [Medaka](./medaka.md) |
