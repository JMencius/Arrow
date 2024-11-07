# SRA status

## Descriptions
This directory contains 4 independent pipelines for

1. Raw nanopore data(FAST5/POD5) availability in SRA database

    Please refer to [raw_ONTdata_search.md](./raw_ONTdata_search.md)

2. BAM availability in SRA database

    Please refer to [sra_bam_availability.md](./sra_bam_availability.md)


3. Basecaller version and flowcell version mentioned in SRA database metadata

    We use a multi-thread Python script to analyze the entire metadata set of SRA. 

    Specifically, this script first filtered the total SRA Runs based on two conditions: 

    - the publication date of the SRA Run falls within the range of “2010/01/01” to “2024/01/09”,
    - the sequencing platform is Oxford Nanopore. Multiple regular expressions were then employed to identify keywords related to flowcell or basecaller configuration information within the XML files of the filtered SRA Runs. 


4. Random downsampling SRA run

    Please refer to [SRA_random_1000sample.md](./SRA_random_1000sample.md)

## Execution environments
Python3 virtual environment
The Python scripts require Python 3.7 or higher. To recreate the same Python running environment use
```bash
conda env create -f python3-env.yaml;
```


## Reproduce results
1. To reproduce our results for `pipeline 1` and `pipeline 2`, please navigate to `SRA advance search` in
```
https://www.ncbi.nlm.nih.gov/sra/advanced
```
Follow the setting in `raw_ONTdata_search.md` and `sra_bam_availability.md`.


2. To reproduce our results for `pipeline 3` and random downsampling part of `pipeline 4`, run `run_all.sh`
```
bash run_all.sh;
```
