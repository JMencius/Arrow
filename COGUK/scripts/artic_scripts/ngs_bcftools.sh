#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;


script_dir=$(dirname "$(realpath "$0")")
script_base=$(dirname "$script_dir")
base=$(dirname "$script_base")

# clean sequence

conda activate bioawk
for i in "$base"/data/ngs_consensus/ERR*;do
	ERR=$(basename "$i")
	bioawk -c fastx '{gsub(/[^ATGC]/, "N", $seq); print ">"$name"\n"$seq}' "$i"/*.fasta > "$i"/"$ERR"_ngs_consensus_cleaned.fasta;
done



conda activate minimap2
# align to reference genome
for i in "$base"/data/ngs_consensus/ERR*;do
	ERR=$(basename "$i")
	cd "$base"/data/ngs_consensus/"$ERR"
	minimap2 -ax asm5 "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta "$ERR"_ngs_consensus_cleaned.fasta| samtools sort - > sorted.bam;
	samtools index sorted.bam;
done


conda activate bcftools;

# consensus2vcf
for i in "$base"/data/ngs_consensus/ERR*;do
	ERR=$(basename "$i")
    	cd "$base"/data/ngs_consensus/"$ERR";
	bcftools mpileup -B -m 1 -f "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta sorted.bam -O b|bcftools call -O v -o "$ERR"_ngs.vcf -mv --ploidy 1;
done

