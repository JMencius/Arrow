#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate python3-env;

# Analysis the whole SRA xml
python read_all_SRA_xml.py -i ../data/SRA_XML/xml -t 24 -a /public/share/mzj22/ONT_ML/SRA_status/data/SRA_XML/xml/SRA_Accessions -q ../results/SRA_ONT_ALL_accession_list.csv -o ../results/SRA_ONT_ALL_accession_label_results.csv
