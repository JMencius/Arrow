#!/bin/bash


base=../data/HG002_R10_5kHz

groups=(fast420 hac420 sup420 fast430 hac430 sup430 fast500 hac500 sup500)

for i in "${groups[@]}";do
	for j in "${groups[@]}";do
		python seq_bha_sim.py -t 48 -r "$base"/"$i"/all.fastq -q "$base"/"$j"/all.fastq;
	done
done
