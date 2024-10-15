# Descriptions
This diectory archives the pipeline for data downsampling.

The purpose of testing downsampling is to check the effect of downsampling to the two main properties of LongBow, Q score disribution and Q score autocorrelation.

# Execution environments
1. The downsampling process utilize `seqtk` 1.3-r106. To recreate the environment, run
```bash
conda env create -f seqtk.yaml;
```

2. Python Scripts for Q score and autocorrelation
These scripts require Python 3.7 or higher.


# Data
We selected a high-coverage ONT sequencing dataset of human melanoma fibroblasts (COLO829) from the ONT Open Data project (s3://ont-open-data/colo829_2023.04/) to evaluate the efficacy of downsampling. This dataset contains 13,760,388 reads from its original POD5 files.

The whole dataset is basecalled with `Guppy 6.4.6 FAST` and `Dorado 0.4.1 FAST` to generate the whole data.


# Pipeline
1. We randomly downsampled it to 1,000,000 reads, 100,000 reads, 10,000 reads, 1,000 reads, 100 reads, and 10 reads respectively by using `seqtk`
`bash downsample.sh;`

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
