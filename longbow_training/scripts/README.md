# Description
This directory archives the pipelines for LongBow model training. Each model includes QV distribution and autocorrelation in `.csv` file. 
For autocorrelation, a leave-one-out test is also included to get the best lag.


# Execution environment
Use the LongBow environment for the following two pipelines
```bash
conda env create -f longbow.yaml;
```

# Training data
Nanopore raw data of 7 model organism, namely _Homo sapiens_, _Mus musculus_, _Danio rerio_, _Drosophila melanogaster_, _Arabidopsis thaliana_, _Saccharomyces cerevisiae_, and _Escherichia coli_ were used for LongBow training.
| index |Species name | Flowcell type | Flowcell type (FLO-) | Sequencing kit (SQK-) | Source |
|:--:|:-------:|:---:|:---:|:---:|:---:|
| 1 | _Homo sapiens_ | R10 | PRO114M | LSK114 | [GIAB HG004](https://labs.epi2me.io/askenazi-kit14-2022-12/) |
| 2 | _Homo sapiens_ | R10 | PRO114M | LSK114 | [GIAB HG002](https://labs.epi2me.io/giab-2023.05/) |
| 3 | _Danio rerio_ | R10 | MIN114 | LSK114 | [VGP zebrafish](https://www.genomeark.org/genomeark-all/Danio_rerio.html) |
| 4 | _Drosophila melanogaster_ | R10 | MIN114 | LSK114 | [Oxford Nanopore Open Data](https://labs.epi2me.io/open-data-drosophila/) |
| 5 | _Arabidopsis thaliana_ | R10 | MIN112 | LSK112 | [SRA database : ERR7919757](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=ERR7919757&display=data-access) |
| 6 | _Escherichia coli_ | R10 | MIN112 | LSK112 | [SRA database : ERR9127552](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=ERR9127552&display=data-access) |
| 7 | _Homo sapiens_ | R9 | PRO002 | LSK109 | [Human Pangenome HG02723](https://s3-us-west-2.amazonaws.com/human-pangenomics/index.html?prefix=NHGRI_UCSC_panel/HG02723/nanopore/) |
| 8 | _Mus musculus_ | R9 | PRO002 | LSK109 | [SRA database : SRR15959871](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR15959871&display=data-access) |
| 9 | _Drosophila melanogaster_ | R9 | MIN106 | LSK109 | [Paper _Highly contiguous assemblies of 101 drosophilid genomes_](https://elifesciences.org/articles/66405) |
| 10 | _Arabidopsis thaliana_ | R9 | PRO002 | LSK109 | [SRA database : SRR16149191](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR16149191&display=data-access) |
| 11 | _Saccharomyces cerevisiae_ | R9 | MIN106 | LSK109 | [SRA database : SRR14729830](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR14729830&display=data-access) |
| 12 | _Escherichia coli_ | R9 | MIN106 | PBK004 | [Zenodo record 7388709](https://zenodo.org/records/7388709) |

For the basecalling of the training data we use the following combination. Python script `get_QV_autocorrelation_model.py` and `autocorrelation_LOO_lag.py` are used to calculate the model of the basecalled FASTQ file and produce the corresponding 120 model csv files in `../data/model`.
| Flowcell type | Basecaller and version | Basecalling mode |
|:---:|:---:|:---:|
| R9 | Guppy2.3.7 | \ |
| R9 | Guppy4.5.4 | FAST, HAC |
| R9 | Guppy6.4.6 | FAST, HAC, SUP |
| R9 | Dorado0.4.1 | FAST, HAC, SUP |
| R10 | Guppy6.4.6 | FAST, HAC, SUP |
| R10 | Dorado0.4.1 | FAST, HAC, SUP |



# Pipelines
1. Conduct leave-one-out(LOO) test to determine the best lag for R9G4, R9G6, R9D0, R10G6, and R10D0
```bash
python autocorrelation_LOO_lag.py -i ../data/model -o ../results/R9G4_autocorrelation_lag_accuracy.txt --subject R9G4;
python autocorrelation_LOO_lag.py -i ../data/model -o ../results/R9G6_autocorrelation_lag_accuracy.txt --subject R9G6;
python autocorrelation_LOO_lag.py -i ../data/model -o ../results/R9D0_autocorrelation_lag_accuracy.txt --subject R9D0;
python autocorrelation_LOO_lag.py -i ../data/model -o ../results/R10G6_autocorrelation_lag_accuracy.txt --subject R10G6;
python autocorrelation_LOO_lag.py -i ../data/model -o ../results/R10D0_autocorrelation_lag_accuracy.txt --subject R10D0;

```

# Result description
1. The result of the LOO test is located in `../results`, 5 txt files record the accuracy verus different lags in different basecalling configurations.
