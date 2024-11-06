#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate minimap2;


refseq_hg38=../../ref/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.gz


for i in ../../../basecalled_fastq/*.fastq;do
    echo "$i";
    base=$(basename "$i".fastq)
    outdir=../../results/alignment/${base}
    mkdir -p ${outdir}
    minimap2 -t 128 -L -o ${outdir}/align_to_hg38.all.sam -ax map-ont ${refseq_hg38} ${i}
    samtools view -h -b -@ 128 ${outdir}/align_to_hg38.all.sam | \
    samtools sort -@ 128 -o ${outdir}/align_to_hg38.all.bam
    samtools index -@ 128 ${outdir}/align_to_hg38.all.bam
done
