# SRA status

## Descriptions
This directory contains 4 independent pipelines for

1. Raw nanopore data(FAST5/POD5) availabilty in SRA database

Please refer to `raw_ONTdata_search.md`

2. BAM availablity in SRA database

Please refer to `sra_bam_availability.md`


3. Basecaller version and flowcell version mentioned in SRA database metadata

We use a multi-threaded Python script to analyze the entire metadat set of SRA. 

Specifically, this script first filtered the total SRA Runs based on two conditions: 

- the publication date of the SRA Run falls within the range of “2010/01/01” to “2024/01/09”,
- the sequencing platform is Oxford Nanopore. Multiple regular expressions were then employed to identify keywords related to flowcell or basecaller configuration information within the XML files of the filtered SRA Runs. 


4. Random downsampling 100 SRA run for label checking

Plase refer to `SRA_random_100sample.md`

## Execution environments
1. Bash Scripts
The scripts are compatible with most modern Linux distributions that include Bash shell.

2. Python Scripts
These scripts require Python 3.7 or higher.


## Reproduce results
1. To reproduce our results for `pipeline 1` and `pipeline 2`, use SRA advance search in
```
https://www.ncbi.nlm.nih.gov/sra/advanced
```
Follow the setting in `raw_ONTdata_search.md` and `sra_bam_availability.md`.


2. To reproduce our results for `pipeline 3` and random downsampling part of `pipeline 4`, run `run_all.sh`
```
bash run_all.sh;
```
