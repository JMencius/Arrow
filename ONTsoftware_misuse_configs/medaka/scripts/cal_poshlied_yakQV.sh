#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate yak;


for subject in R9G4FAST R9G4HAC R9G6FAST R9G6HAC R9G6SUP R10D0HAC R10D0SUP;do
	for group in R9G4FAST R9G4HAC R9G6FAST R9G6HAC R9G6SUP R10D0HAC R10D0SUP;do
	echo "$subject"_"$group";
	yak qv -t 32 -p -K 3.2g -l 100k ../../yak/results/sr.yak ../results/"$subject"/"$subject"_"$group"/consensus.fasta > ../results/"$subject"/"$subject"_"$group"/"$subject"_"$group".yak.txt;
	done
done
