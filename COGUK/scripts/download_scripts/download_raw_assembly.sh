#!/bin/bash

# loop download 
# 1. ont raw reads data
# 2. ont consensus sequence
# 3. ngs consensus seuqnece

input_file="../download_list.txt";

script_dir=$(dirname "$(realpath "$0")") 
script_base=$(dirname "$script_dir")
base=$(dirname "$script_base")


mkdir -p "$base"/data/ont_raw_reads/;
while read -r str1 str2 str3 str4;do
	ERR="$str1";
	ontraw="$str2"
	ontLink="$str3";
	ngsLink="$str4";

	echo "Processing $ERR";
	
	# create directories for storing results
	mkdir -p "$base"/data/ont_consensus/"$ERR";
	mkdir -p "$base"/data/ngs_consensus/"$ERR";

	wget -P "$base"/data/ont_raw_reads/ "$ontraw"
	wget -P "$base"/data/ont_consensus/"$ERR" "$ontLink";
	wget -P "$base"/data/ngs_consensus/"$ERR" "$ngsLink";


gzip -dk "$base"/data/ont_raw_reads/*.gz;
gzip -dk "$base"/data/ont_consensus/"$ERR"/*.gz;
gzip -dk "$base"/data/ngs_consensus/"$ERR"/*.gz;


done < "$input_file"

echo "ALL DONE"
