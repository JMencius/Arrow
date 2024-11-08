#!/bin/bash

# build directory structure
mkdir -p ../results;

# activate yak env
conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate yak;

# build yak reference hash table using NGS sequencing data
yak count -b 37 -t 32 -o ../results/sr.yak <(cat ../data/HG002_HiSeq30x_subsampled_R1.fastq) <(cat ../data/HG002_HiSeq30x_subsampled_R2.fastq);
