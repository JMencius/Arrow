#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;

script_dir=$(dirname "$(realpath "$0")")
script_base=$(dirname "$script_dir")
base=$(dirname "$script_base")


conda activate bcftools
# convert to consensus sequence
for i in "$base"/results/ERR*;do
 	ERR=$(basename "$i")
    	cd "$base"/results/"$ERR"/artex;
	tabix "$ERR"_longbow.artex.vcf.gz;
	bcftools consensus -f "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta "$ERR"_longbow.artex.vcf.gz -o "$ERR"_artex_consensus.fasta
done


conda activate minimap2
# align to reference genome
for i in "$base"/results/ERR*;do
	ERR=$(basename "$i")
	cd "$base"/results/"$ERR"/artex
	minimap2 -ax asm5 "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta "$ERR"_artex_consensus.fasta| samtools sort - > "$ERR"_artex_consensus_sorted.bam;
	samtools index "$ERR"_artex_consensus_sorted.bam;
done


conda activate bcftools;

# consensus2vcf
for i in "$base"/results/ERR*;do
	ERR=$(basename "$i")
    	cd "$base"/results/"$ERR"/artex;
	bcftools mpileup -B -m 1 -f "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta "$ERR"_artex_consensus_sorted.bam -O b|bcftools call -O v -o "$ERR"_artex_cleaned_consensus.vcf -mv --ploidy 1;
done

