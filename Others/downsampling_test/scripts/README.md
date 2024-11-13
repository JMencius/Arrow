# Description
This directory archives the pipeline for data downsampling.

The purpose of testing downsampling is to check the effect of downsampling to the two main properties of LongBow, Q score distribution and Q score autocorrelation.


# Execution environments
1. The downsampling process utilize `seqtk` version 1.3-r106. To recreate the environment, run
```bash
conda env create -f seqtk.yaml;
```

2. Python Scripts for Q score and autocorrelation
Just use the same conda environment of `LongBow`
```bash
conda env create -f ont-longbow.yaml;
```

# Data
We selected a high-coverage ONT sequencing dataset of human melanoma fibroblasts (COLO829) from the ONT Open Data project (s3://ont-open-data/colo829_2023.04/) to evaluate the efficacy of downsampling. This dataset contains 13,760,388 reads from its original POD5 files. The whole dataset is basecalled with `Guppy 6.4.6 FAST` and `Dorado 0.4.1 FAST` to generate the whole data.


Please download the two whole basecalled FASTQ file we shared through ScienceDB link to the ../data directory and decompress it before running the following pipeline.

You can follow the instruction in [here](../../../ScienceDB/README.md) to download the data we shared. The data is in <https://www.scidb.cn/en/detail?dataSetId=b9eca82475a64772a67ec9b7dac2beb3>, please download the `HG002_R9_guppy_similarity.tar.gz` file.
```bash
mkdir -p ../data;
cd ../data

## Download the FASTQ file through ScienceDB

# Decompress the FASTQ file
gzip -d COLO829_R10D0FAST_all.fastq.gz;
gzip -d COLO829_R10G6FAST_all.fastq.gz

```




# Pipeline
1. We randomly downsampled it to 1,000,000 reads, 100,000 reads, 10,000 reads, 1,000 reads, 100 reads, and 10 reads respectively by using `seqtk`
```
bash downsample.sh;
```

2. Calculate the Q score distribution of the whole data and downsampled reads
```bash
bash cal_wholedata_qdistribution.sh;
bash cal_downsample_qdistribution.sh;
```

3. Calculate the autocorrelation of the whole and downsampled reads
```bash
bash cal_wholedata_autocorr.sh;
bash cal_downsample_autocorr.sh;
```

# Repeat our results
To repeat our results, please install the aforementioned conda environment first and run
```
bash ./run_all.sh;
```

