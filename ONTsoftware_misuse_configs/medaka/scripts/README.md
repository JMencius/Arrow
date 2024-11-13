# Medaka
## Description
This directory archives the pipelines for `Medaka` polishing and `Yak` based polished assembly QV evaluation.


## Execution environments
1. `Medaka` environment is provided in `medaka.yaml`. To recreate this environment run
```bash
conda env create -f medaka.yaml;
```

2. `Yak` environment is provided in `yak.yaml`. To recreate this environment run
```bash
conda env create -f yak.yaml;
```


## Pipeline
1. Make sure you have run the pipeline in `../../flye/scripts/README.md` and `../../yak/scripts/README.md`.

To run Flye assembly follow the instruction in [here](../../flye/scripts/README.md).

The genome draft used for `Medaka` polishing is based on `Flye` assembled contigs.. The evaluation is performed using yak with short-read NGS data.


3. Run `Medaka` polishing for R9G4FAST, R9G4HAC, R9G6FAST, R9G6HAC, R9G6SUP, R10D0HAC, and R10D0SUP data
`bash run_medaka_polishing.sh;`


4. Run `yak` evaluation for polished data
`bash cal_polished_yakQV.sh;`

## Medaka models
The correct Medaka models for different flowcell and basecaller versions of HG002 data is listed below.
| Flowcell | Basecaller | Mode | Correct Medaka config |
|:---:|:---:|:---:|:---:|
| R9 | Guppy4.2.2 | FAST | r941_prom_fast_g303 |
| R9 | Guppy4.2.2 | HAC | r941_prom_high_g4011 |
| R9 | Guppy6.3.8 | FAST | r941_prom_fast_g507 |
| R9 | Guppy6.3.8 | HAC | r941_prom_hac_g507 |
| R9 | Guppy6.3.8 | SUP | r941_prom_sup_g507 |
| R10 | Dorado0.4.3 | HAC | r1041_e82_400bps_hac_v4.1.0 |
| R10 | Dorado0.4.3 | SUP | r1041_e82_400bps_sup_v4.1.0 |

## Result descriptions
1. Naming pattern
   For example, `R9G4FAST_R9G4HAC` means R9G4FAST basecalled FASTQ data using Medaka model for R9G4HAC.
3. Polished QV shift will be in `./QVshift.csv`, the description of each column is as follow:

| Column index | Column name | Column description |
|:---:|:---:|:---:|
| 1 | basecalled | The basecalling configuration for the input FASTQ | 
| 2 | polished contig | Medaka model used for genome polishing |
| 3 | draft QV | Yak QV score of the flye-assembled draft |
| 4 | polished QV | Yak QV score of the polished contig |
| 5 | QV shift | $ \text{QV shift} = \text{Polished QV} - \text{Draft QV} $ |



## Repeat our results
To repeat our results, please install the aforementioned conda environment first and  make sure you have run the pipeline in `../../flye/scripts/README.md` and `../../yak/scripts/README.md`, then run
```
bash ./run_all.sh;
```
Note that, Medaka is relatively slow. We finished all 49 groups of polishing with 32 cores and an Nvidia RTX A5000 in 3 weeks.
