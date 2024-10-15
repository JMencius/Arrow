#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate articlatest;

input_file="../ERR_list_models.txt";

script_dir=$(dirname "$(realpath "$0")") 
script_base=$(dirname "$script_dir")
base=$(dirname "$script_base")


while read -r str1 str2 str3;do
	fastq="$str1";
	random_model="$str3";
	longbow_model="r941_min_high_g360";
	default_model="r1041_e82_400bps_sup_v4.3.0"

	echo "Processing $fastq";
	
	# create directories for storing results
	mkdir -p "$base"/results/"$fastq"/longbow;
	mkdir -p "$base"/results/"$fastq"/random;
	mkdir -p "$base"/results/"$fastq"/default;
	
	# run longbow predicted medaka model on artic pipeline
	cd "$base"/results/"$fastq"/longbow;
	artic minion --medaka --medaka-model "$longbow_model" --threads 16 --scheme-directory "$base"/ref --read-file "$base"/data/ont_raw_reads/"$fastq".fastq nCoV-2019/V3 "$fastq"_longbow --no-longshot --skip-nanopolish;

	# run random medaka model on artic pipeline
	cd "$base"/results/"$fastq"/random;
        artic minion --medaka --medaka-model "$random_model" --threads 16 --scheme-directory "$base"/ref --read-file "$base"/data/ont_raw_reads/"$fastq".fastq nCoV-2019/V3 "$fastq"_random --no-longshot --skip-nanopolish;  
	
	# run medaka default model on artic pipeline
	cd "$base"/results/"$fastq"/default;
	artic minion --medaka --medaka-model "$default_model" --threads 16 --scheme-directory "$base"/ref --read-file "$base"/data/ont_raw_reads/"$fastq".fastq nCoV-2019/V3 "$fastq"_default --no-longshot --skip-nanopolish;

done < "$input_file"

echo "ALL DONE"
