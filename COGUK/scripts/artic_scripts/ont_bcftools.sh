#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate minimap2;

script_dir=$(dirname "$(realpath "$0")")
script_base=$(dirname "$script_dir")
base=$(dirname "$script_base")

# align to reference genome
for i in "$base"/data/ont_consensus/ERR*;do
	ERR=$(basename "$i")
	cd "$base"/data/ont_consensus/"$ERR"
	minimap2 -ax asm5 "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta *.fasta| samtools sort - > sorted.bam;
	samtools index sorted.bam;
done


conda activate bcftools;

# consensus2vcf
for i in "$base"/data/ont_consensus/ERR*;do
	ERR=$(basename "$i")
	cd "$base"/data/ont_consensus/"$ERR";
	bcftools mpileup -B -m 1 -f "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta sorted.bam -O b|bcftools call -O v -o "$ERR"_ont.vcf -mv --ploidy 1;
done

