#!/bin/bash

# download sratoolkit to current directory
## You can change the sratoolkit according to your platform in https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit
wget -nc https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.0.7/sratoolkit.3.0.7-ubuntu64.tar.gz;

# extract sratoolkit
tar -zxvf sratoolkit.3.0.7-ubuntu64.tar.gz;

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;

# donwload sra human ont data top 10K reads
python download_all_sra_ont.py -t 16 -o ../data/sra_human_10Kreads -p ./sratoolkit.3.0.7-ubuntu64/bin -i sra_list.txt;
