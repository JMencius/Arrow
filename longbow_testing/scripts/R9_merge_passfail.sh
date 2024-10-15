#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh;
conda activate fastcat;


work_dir=$(realpath ../data/test_data_basecalling);
target=$(realpath ../data/test_data_merge)

for idx in {22..66};do
	echo "$work_dir"/sample"$idx"_*;
	
	cd "$work_dir"/sample"$idx"_*/results;
        cd guppy4.5.4_fast;
        fastcat fail pass > merged.fastq;
        cp merged.fastq "$target"/sample"$idx"_R9G4FAST.fastq;

	cd "$work_dir"/sample"$idx"_*/results;
        cd guppy4.5.4_hac;
        fastcat fail pass > merged.fastq;
        cp merged.fastq "$target"/sample"$idx"_R9G4HAC.fastq;


	cd "$work_dir"/sample"$idx"_*/results;
	cd guppy6.4.6_fast;
	fastcat fail pass > merged.fastq;
	cp merged.fastq "$target"/sample"$idx"_R9G6FAST.fastq;
	
	cd "$work_dir"/sample"$idx"_*/results;
	cd guppy6.4.6_hac;
        fastcat fail pass > merged.fastq;
        cp merged.fastq "$target"/sample"$idx"_R9G6HAC.fastq;
	
	cd "$work_dir"/sample"$idx"_*/results;
	cd guppy6.4.6_sup;
        fastcat fail pass > merged.fastq;
        cp merged.fastq "$target"/sample"$idx"_R9G6SUP.fastq;

done
