#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate singularity-env;

ref=../../ref/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.gz

for i in $(ls ../../results/alignment);do
    echo "${i}";
    for j in r941_prom_hac_g238 r941_prom_hac_g360+g422 r941_prom_sup_g5014 r1041_e82_400bps_hac_v410 r1041_e82_400bps_sup_v410;do
        echo "${j}";
        outdir=../../results/variant_calling/${i}_${j}
        mkdir -p ${outdir};
        singularity exec \
            ../../image/clair3.sif \
            /opt/bin/run_clair3.sh \
            --bam_fn=../../results/alignment/${i}/align_to_hg38.all.bam \
            --ref_fn=${ref} \
            --threads=40 \
            --platform="ont" \
            --model_path=${j} \
            --output=${outdir};
    done
done
