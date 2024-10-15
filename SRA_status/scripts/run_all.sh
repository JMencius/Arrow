#!/bin/bash

# SRA status

## 1. Basecaller version and flowcell version mentioned in SRA database metadata

bash download_extract_SRA_XML.sh;
bash analysis_SRA_XML.sh;

## 2. Random downsample 100 SRA run for label checking
python random_select_SRARUN.py -i ../data/SraAccList_NOCOVID_20240109.csv -o ../results/Sampled_1000_srarun.txt;

