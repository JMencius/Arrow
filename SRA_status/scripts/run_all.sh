#!/bin/bash

# SRA status

## build directory structure
mkdir -p ../data;
mkdir -p ../results;

## 1. Basecaller version and flowcell version mentioned in SRA database metadata

bash download_extract_SRA_XML.sh;
bash analysis_SRA_XML.sh;

## 2. Random downsample 100 SRA run for label checking
conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate python3-env;
python random_select_SRARUN.py -i ../data/SraAccList_NOCOVID_20240109.csv -o ../results/Sampled_1000_srarun.txt;

