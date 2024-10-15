#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate minimap2;

script_dir=$(dirname "$(realpath "$0")")
script_base=$(dirname "$script_dir")
base=$(diranme "$script_base")

# align to reference genome
for i in "$base"/results/ERR*;do
	ERR=$(basename "$i")
	cd "$base"/results/"$ERR"/random
	minimap2 -ax asm5 "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta "$ERR"_longbow.random.fasta| samtools sort - > "$ERR"_random_consensus_sorted.bam;
	samtools index "$ERR"_random_consensus_sorted.bam;
done


conda activate bcftools;

# consensus2vcf
for i in "$base"/results/ERR*;do
	ERR=$(basename "$i")
    cd "$base"/results/"$ERR"/random;
	bcftools mpileup -B -m 1 -f "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta "$ERR"_random_consensus_sorted.bam -O b|bcftools call -O v -o "$ERR"_random_consensus.vcf -mv --ploidy 1;
done

