#!/bin/bash


base=../data/HG002_R10_4kHz

groups=(fast352 hac352 sup352 fast400 hac400 sup400 fast410 hac410 sup410)

for i in "${groups[@]}";do
	for j in "${groups[@]}";do
		python seq_bha_sim.py -t 48 -r "$base"/"$i"/all.fastq -q "$base"/"$j"/all.fastq;
	done
done
