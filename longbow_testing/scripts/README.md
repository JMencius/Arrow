# LongBow testing
## Description
This directory archives the testing pipeline to evaluate the `LongBow` performance. The test data contains two separate categories: 

1. Our own basecalled data using raw FAST5/POD5 data; 

2. Top `10,000` sequences of human ONT sequencing data on SRA database until `2024-Jan-9`.


## Execution environment
Use the `LongBow` conda environment
```bash
conda env create -f longbow.yaml;
```

## Data
Please download the 66 groups of test data we shared through ScienceDB link to the `../data` directory and decompress it before running the following pipeline.

<mark> The data is shared through <https://www.scidb.cn/en/detail?dataSetId=47fc05aee6be46719aeb7cf03cfc70bf> </mark>

You can follow the instruction in [here](../../ScienceDB/README.md) to download the shared data.
```bash
mkdir -p ../data;
cd ../data;

# Download the FASTQ file through ScienceDB

## decompression
tar -zxvf sixty_six_samples.tar.gz;
```

## Pipelines
## 1. Install LongBow in your environment
Please follow the instruction in `longbow2.2.0/README.md`
To be notice, the longbow code is not provided in this repository.

### 2. Test LongBow on our own basecalled data
#### 2.1 Run LongBow on our own basecalled data
```bash
bash run_own_called_longbow.sh;
```

#### 2.2 Summarize our own basecalled results
```bash
bash analysis_own_called_result.py;
```

### 3. Run LongBow on human ONT SRA data
#### 3.1 Download human ONT SRA data top 10,000 sequence
```bash
bash download_all_sra_ont.sh;
```

#### 3.2 Run LongBow on human ONT SRA data
```bash
bash run_sra_ont_longbow.sh;
```

#### 3.3 Summarize human ONT SRA results
```
bash analysis_sra_ont.sh;
```


## Result descriptions
1. LongBow test results on our own basecalled data is  `../results/own_called.csv`;
2. LongBow test results on ONT SRA data is in `../results/sra_ont_results.csv`.


## Repeat our results
To repeat our results, please install the aforementioned conda environment and download the shared data, then run
```bash
bash ./run_all.sh;
```
