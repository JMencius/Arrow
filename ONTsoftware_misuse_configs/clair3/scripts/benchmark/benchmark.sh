#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate happy;

truth=../../ref/HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz
conf_bed=../../ref/HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed
ref=../../ref/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.gz

for i in ../../results/clair3/*;do
    echo "${i}";
    base=$(basename ${i})
    mkdir -p ../../results/benchmark/${base}
    query=${i}/merge_output.vcf.gz
    hap.py \
        ${truth} ${query} \
        -o ../../results/benchmark/${base}/${base} \
        -r ${ref} \
        -f ${conf_bed} \
        --threads 40;
done
    