#!/bin/bash

for readcount in 1000000 100000 10000 1000 100 10;do
	seqtk sample -s 42 ../data/all_pod5_dorado0.4.1_fast/all.fastq "$readcount" > ../downsample/COLO829_dorado_"$readcount".fastq;
	seqtk sample -s 42 ../data/all_pod5_guppy6.4.6_fast/all.fastq "$readcount" > ../downsample/COLO829_guppy_"$readcount".fastq;
done




