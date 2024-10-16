#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;

mkdir -p ../results/model;

# R10 samples
for sample in ecoli  fish  fruitfly  human  human_5kHz  thaliana; do	
	echo "$sample";
	RESULT_DIR="../data/R10_$sample";
	OUTPUT_DIR="../results/model";

	# R10 dorado model
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R10D0FAST.csv -p "$RESULT_DIR"/dorado0.4.1_fast/all.fastq;
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R10D0HAC.csv -p "$RESULT_DIR"/dorado0.4.1_hac/all.fastq;
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R10D0SUP.csv -p "$RESULT_DIR"/dorado0.4.1_sup/all.fastq;

	# R10 guppy model
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R10G6FAST.csv -p "$RESULT_DIR"/guppy6.4.6_fast/pass.fastq -f "$RESULT_DIR"/guppy6.4.6_fast/fail.fastq;
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R10G6HAC.csv -p "$RESULT_DIR"/guppy6.4.6_hac/pass.fastq -f "$RESULT_DIR"/guppy6.4.6_hac/fail.fastq;
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R10G6SUP.csv -p "$RESULT_DIR"/guppy6.4.6_sup/pass.fastq -f "$RESULT_DIR"/guppy6.4.6_sup/fail.fastq;
done


# R9 samples
for sample in ecoli  fruitfly  human  mouse  thaliana  yeast; do
	echo "$sample";
        RESULT_DIR="../data/R9_$sample";
	OUTPUT_DIR="../results/model";

	# R9 dorado model
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R9D0FAST.csv -p "$RESULT_DIR"/dorado0.4.1_fast/all.fastq;
        python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R9D0HAC.csv -p "$RESULT_DIR"/dorado0.4.1_hac/all.fastq;
        python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R9D0SUP.csv -p "$RESULT_DIR"/dorado0.4.1_sup/all.fastq;	

	# R9 Guppy2 model
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R9G2.csv -p "$RESULT_DIR"/guppy2.3.7/all.fastq; 

	# R9 Guppy4,6 model
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R9G4FAST.csv -p "$RESULT_DIR"/guppy4.5.4_fast/pass.fastq -f "$RESULT_DIR"/guppy4.5.4_fast/fail.fastq;
        python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R9G4HAC.csv -p "$RESULT_DIR"/guppy4.5.4_hac/pass.fastq -f "$RESULT_DIR"/guppy4.5.4_hac/fail.fastq;
	python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R9G6FAST.csv -p "$RESULT_DIR"/guppy6.4.6_fast/pass.fastq -f "$RESULT_DIR"/guppy6.4.6_fast/fail.fastq;
        python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R9G6HAC.csv -p "$RESULT_DIR"/guppy6.4.6_hac/pass.fastq -f "$RESULT_DIR"/guppy6.4.6_hac/fail.fastq;
        python get_QV_autocorrelation_model.py -t 32 -o "$OUTPUT_DIR"/"$sample"_R9G6SUP.csv -p "$RESULT_DIR"/guppy6.4.6_sup/pass.fastq -f "$RESULT_DIR"/guppy6.4.6_sup/fail.fastq;
done
