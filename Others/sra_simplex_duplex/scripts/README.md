# Descriptions
This folder archives the pipeline for checking simplex or duplex configurations in SRA ONT raw FAST5 data.


## Execution environments
1. Python Scripts for download and analysis
These scripts require Python 3.7 or higher and a Linux distribution with hexdump installed. You can verify hexdump installation by running the following command in Linux Bash:
```
hexdump --version;
```


## Pipeline
1. Partial Download of FAST5 Data
Due to the typically large size of FAST5 compressed files, only a portion of the data will be downloaded:
```
python partial_download.py -i DNA_raw_20240109.txt -w ../data > ../results/download_log.txt;
```


2. Preprocess and decompressing the download files
This step involves preprocessing the downloaded files:
```
python hexdump_preprocess.py -w ../data;
```


3. Analyzing FAST5 Files
This analysis extracts the flowcell type, sequencing kit, and experiment time, which are essential for determining whether the configuration is simplex or duplex:
```
python hexdump_check.py -i ../data -o ../results/sra_fast5_ano.txt > ../results/annotation.log;
```
