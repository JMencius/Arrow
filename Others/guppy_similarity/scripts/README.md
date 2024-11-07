# Descriptions
This directory archives the pipeline for sequence identity and QV score similarity between Guppy versions.

We use the downsampled dataset HG002 sequenced with R9.4.1 flowcell (https://labs.epi2me.io/gm24385_2021.05) to evaluate the sequence identity and QV score similarity.


# Execution environments
1. To recreate the Python virtual environment for sequence identity, run the following command.
```bash
conda env create -f mappy.yaml;
```

2. To recreate the Python virtual environment for QV similarity analysis, just use the longbow environment.
```bash
conda env create -f ont-longbow.yaml;
```

# Data
Please download the `HG002_R9_guppy_similarity.tar.gz` file we shared through ScienceDB link to the `../data` directory and decompress it before running the following pipelines.
The files contained the basecalled FASTQ of HG002 data.

You can follow the instruction in [here](../../ScienceDB/README.md) to download the data we shared.
```bash
mkdir -p ../data;
cd ../data;
## Download the FASTQ file through FTP link in the ScienceDB
## decompression
tar -zxvf HG002_R9_guppy_similarity.tar.gz;
```


# Pipelines
1. Evaluate the sequence identity between HG002 R9 Guppy version
```bash
bash HG002_R9_seq_identity.sh
```

2. Evaluate the Bhattacharyya coefficient between HG002 R9 Guppy version
```bash
bash HG002_R9_QV_sim.sh > ../results/HG002_R9_qv_sim.txt
```


# Repeat our results
To repeat our results, please install the aforementioned conda environment first and run
```
bash ./run_all.sh;
```

