#!/bin/bash

subject=R9G4HAC
model=(r941_prom_fast_g303 r941_prom_high_g4011 r941_prom_fast_g507 r941_prom_hac_g507 r941_prom_sup_g507 r1041_e82_400bps_hac_v4.1.0 r1041_e82_400bps_sup_v4.1.0)
name=(R9G4FAST R9G4HAC R9G6FAST R9G6HAC R9G6SUP R10D0HAC R10D0SUP)

for idx in {0..6};do
	medaka_consensus -t 48 -d ../results/"$subject"/contigs.fasta -m ${model[$idx]} -b 50 -o ../results/"$subject"/"$subject"_${name[$idx]} -i ../../basecalling_alignment/results/HG002_R9G4HAC_q9.fastq;
done
