# Description
This directory archive the use of `yak`<https://github.com/lh3/yak>. We use `yak` to build the k-mer reference hash table for paired end data. This reference is used to evaluate the assembly QV score of `flye`, `shasta` or `medaka`.


# Execution environment
Set up the conda environment for running `yak`
```
conda env create -f yak.yaml;
```

# Pipeline
1. Download short reads data
Use `wget` to download PCR-free NGS sequencing data of HG002 and unzip it
`bash download_ngs.sh;`

2. Build k-mer refernce hash table
`bash build_yak.sh;`


# Results description
`../results/sr.yak`
Yak generated k-mer hash table from PCR-free NGS sequencing data of HG002, which will be used for `yak qv` calculation.



# Repeat our results
To repeat our results, please install the forementioned conda environment first and run
```
bash ./run_all.sh;
```
