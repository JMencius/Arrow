# Description
This directory archives the pipeline we use to run flye to build an assembly draft.


# Execution environments
1. Set up the `conda` environment for running `flye` (version 2.9.3)
```bash
conda env create -f flye.yaml;
```

2. Set up the `conda` environment for running `yak`
```bash
conda env create -f yak.yaml;
```


# Pipelines
1. Assembly `Flye` draft for different HG002 basecalling configuration
```
bash flye_draft.sh
```

2. Calculate `Flye` draft QV
```
bash draft_QV_calculation.sh
```


# Results descriptions
For each directory in `../results`, such as `R10D0HAC`, is the output folder for `flye` *de novo* assembly.


In each folder, `yak.txt` holds the `yak` QV score of the unpolished `contigs.fasta`. 


# Repeat our results
To repeat our results, please 
1. Install the forementioned conda environment.

2. Run the scripts in `../../yak/scripts/run_all.sh` to create a `yak` k-mer hash table

3. Run `run_all.sh`
```
bash ./run_all.sh;
```

