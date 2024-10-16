#!/bin/bash

# build the directory structure
mkdir -p ../data/downsample;
mkdir -p ../results;


# activate seqtk running env
conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate seqtk;


# downsampleing
for readcount in 1000000 100000 10000 1000 100 10;do
	seqtk sample -s 42 ../data/COLO829_R10D0FAST_whole/COLO829_R10D0FAST_all.fastq "$readcount" > ../data/downsample/COLO829_dorado_"$readcount".fastq;
	seqtk sample -s 42 ../data/COLO829_R10G6FAST_whole/COLO829_R10G6FAST_all.fastq "$readcount" > ../data/downsample/COLO829_guppy_"$readcount".fastq;
done




