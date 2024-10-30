#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate yak;

# R9G4FAST
yak qv -t 32 -p -K 3.2g -l 100k ../../yak/results/sr.yak ../results/R9G4FAST/30-contigger/contigs.fasta > ../results/R9G4FAST/R9G4FAST_draft_yak.txt;

# R9G4HAC
yak qv -t 32 -p -K 3.2g -l 100k ../../yak/results/sr.yak ../results/R9G4HAC/30-contigger/contigs.fasta > ../results/R9G4HAC/R9G4HAC_draft_yak.txt;

# R9G6FAST
yak qv -t 32 -p -K 3.2g -l 100k ../../yak/results/sr.yak ../results/R9G6FAST/30-contigger/contigs.fasta > ../results/R9G6FAST/R9G6FAST_draft_yak.txt;

# R9G6HAC
yak qv -t 32 -p -K 3.2g -l 100k ../../yak/results/sr.yak ../results/R9G6HAC/30-contigger/contigs.fasta > ../results/R9G6HAC/R9G6HAC_draft_yak.txt;

# R9G6SUP
yak qv -t 32 -p -K 3.2g -l 100k ../../yak/results/sr.yak ../results/R9G6SUP/30-contigger/contigs.fasta > ../results/R9G6SUP/R9G6SUP_draft_yak.txt;

# R10D0HAC
yak qv -t 32 -p -K 3.2g -l 100k ../../yak/results/sr.yak ../results/R10D0HAC/30-contigger/contigs.fasta > ../results/R10D0HAC/R10D0HAC_draft_yak.txt;

# R10D0SUP
#yak qv -t 32 -p -K 3.2g -l 100k ../../yak/results/sr.yak ../results/R10D0SUP/30-contigger/contigs.fasta > ../results/R10D0SUP/R10D0SUP_draft_yak.txt;
