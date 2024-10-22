#!/bin/bash

script_dir=$(dirname "$(realpath "$0")")
base=$(dirname "$script_dir")

for i in ../data/sra_human_10Kreads/*.fastq; do
	echo "$i";
	name=$(basename "$i")
	python ../../longbow_code/longbow2.2.0/longbow.py -t 48 -i "$i" -b -o "$base"/results/sra_human/"$i".json;
done
