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
1. Assemble `Flye` draft for different HG002 basecalling configuration
```
bash flye_draft.sh
```

2. Calculate `Flye` draft QV
```
bash draft_QV_calculation.sh
```

# Flye parameters
Flye has different parameters for different ONT data. The following lists the parameter we used to assemble the draft.
| Flowcell | Basecaller | Basecalling mode | Flye parameter |
|:---:|:---:|:---:|:---:|
| R9 | Guppy4.2.2 | FAST | --nano-raw |
| R9 | Guppy4.2.2 | HAC | --nano-raw |
| R9 | Guppy6.3.8 | FAST | --nano-raw |
| R9 | Guppy6.3.8 | HAC | --nano-hq |
| R9 | Guppy6.3.8 | SUP | --nano-hq |
| R10 | Dorado 0.4.3 | HAC | --nano-hq --read-error 0.03 |
| R10 | Dorado 0.4.3 | SUP | --nano-hq --read-error 0.03 |


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
<mark> Note that, you may not get exact yak QV score as ours. This is because some steps in Flye is not deterministic, as discuss in Flye issue <https://github.com/mikolmogorov/Flye/issues/298>, but we expect the results to be comparable. </mark>
