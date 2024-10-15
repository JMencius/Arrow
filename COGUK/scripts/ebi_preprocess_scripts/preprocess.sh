#!/bin/bash

# find COG-UK sample id with both NGS and ONT sequencing
python intersect.py -i ../../data/ebi_metadata/filereport_read_run_PRJEB37886_tsv.txt -o ../../data/ebi_metadata/nCoV2019_ONT_illumina.csv;

# label the analysis file of the COG-UK sample
python get_analysis_file.py -i ../../data/ebi_metadata/filereport_analysis_PRJEB37886_tsv.txt -c ../../data/ebi_metadata/nCoV2019_ONT_illumina.csv -o ../../data/ebi_metadata/nCoV2019_final_select.csv;

# export download list to txt
python export_txt.py ../../data/ebi_metadata/nCoV2019_final_select.csv ../download_list.txt;

