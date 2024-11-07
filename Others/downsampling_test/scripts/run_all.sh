#!/bin/bash

# 1. Build the directory structure
mkdir -p ../results;

# 1. We randomly downsampled it to 1,000,000 reads, 100,000 reads, 10,000 reads, 1,000 reads, 100 reads, and 10 reads respectively by using seqtk
bash downsample.sh;

# 2. Calculate the Q score distribution of the whole data and downsampled reads
bash cal_wholedata_qdistribution.sh;
bash cal_downsample_qdistribution.sh;


# 3. Calculate the Q score autocorrelation of the whole and downsampled reads
bash cal_wholedata_autocorr.sh;
bash cal_downsample_autocorr.sh;
