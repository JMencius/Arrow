#!/bin/bash


conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate flye;


# build draft for different HG002 basecalling configuration
## R9 Guppy4 data
#For ONT R9 `Guppy4` basecalled data (`FAST` and `HAC` mode)
flye --nano-raw ../../basecalled_data/HG002_R9G4FAST_q8.fastq -t 112 -g 3.1g -o ../results/R9G4FAST --asm-coverage 50;
flye --nano-raw ../../basecalled_data/HG002_R9G4HAC_q9.fastq -t 112 -g 3.1g -o ../results/R9G4HAC --asm-coverage 50;

## R9 Guppy6 data
#For ONT R9 `Guppy6` basecalled data in `FAST` mode we use
flye --nano-raw ../../basecalled_data/HG002_R9G6FAST_q8.fastq -t 112 -g 3.1g -o ../results/R9G6FAST --asm-coverage 50;

#For R9 `Guppy6` basecalled data in `HAC` and `SUP` mode we use
flye --nano-hq ../../basecalled_data/HG002_R9G6HAC_q9.fastq -t 112 -g 3.1g -o ../results/R9G6HAC --asm-coverage 50;
flye --nano-hq ../../basecalled_data/HG002_R9G6SUP_q10.fastq -t 112 -g 3.1g -o ../results/R9G6SUP --asm-coverage 50;

## R10 Dorado0 data
#For ONT R10 `Dorado0` basecalled data (Q20 data) in `HAC` and `SUP` mode we use
flye --nano-hq ../../basecalled_data/HG002_R10D0HAC_q9.fastq --read-error 0.03 -t 112 -g 3.1g -o ../results/R10D0HAC --asm-coverage 50;
flye --nano-hq ../../basecalled_data/HG002_R10D0SUP_q10.fastq --read-error 0.03 -t 112 -g 3.1g -o ../results/R10D0SUP --asm-coverage 50;
