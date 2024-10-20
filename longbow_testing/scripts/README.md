# Description
This directory archives the testing pipeline to evaluate the `LongBow` performance. The test data containing two seperate categories: 

1. Our own basecalled data using raw FAST5/POD5 data; 

2. Top `10,000` sequence of human ONT sequencing data on SRA database until `2024-Jan-9`.


# Execution environment
Use the `LongBow` conda environment
```bash
conda env create -f longbow.yaml;
```


# Pipelines
## 1. Test LongBow on our own basecalled data
### 1.1 Run LongBow on our own basecalled data
```bash
bash run_own_called_longbow.sh;
```

### 1.2 Summarize the our own basecalled results
```bash
bash analysis_own_called_result.py;
```

## 2. Run LongBow on human ONT SRA data
### 2.1 Download human ONT SRA data top 10,000 sequence
```bash
bash download_all_sra_ont.sh;
```

### 2.2 Run LongBow on human ONT SRA data
```bash
bash run_sra_ont_longbow.sh;
```

### 2.3 Summarize the human ONT SRA results
```
bash analysis_sra_ont.sh;
```


# Result descriptions
1. LongBow test results on our own basecalled data is  `../results/own_called.csv`;


2. LongBow test results on ONT SRA data is in `../results/sra_ont_results.csv`.


# Repeat our results
To repeat our results, please install the forementioned conda environment first and run
```bash
bash ./run_all.sh;
```
