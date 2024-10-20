# Description
This directory archives the pipelines for `Medaka` polishing and `Yak` based polished assembly QV evaluation.


# Execution environment
1. `Medaka` environment is provided in `medaka.yaml`. To recreate this environment run
```bash
conda env create -f medaka.yaml;
```

2. `Yak` environment is provided in `yak.yaml`. To recreate this environment run
```bash
conda env create -f yak.yaml;
```


# Pipeline
0. Make sure you have run the pipeline in `../../flye/scripts/README.md` and `../../yak/scripts/README.md`
The genome draft of `Medaka` polishing is based on `flye` contigs. The evaluation is based on `yak` using short-read NGS data.


1. Run `Medaka` polishing for R9G4FAST, R9G4HAC, R9G6FAST, R9G6HAC, R9G6SUP, R10D0HAC, and R10D0SUP data
`bash run_medaka_polishing.sh;`


2. Run `yak` evaluation for polished data
`bash cal_poshlied_yakQV.sh;`


# Repeat our results
To repeat our results, please install the forementioned conda environment first and run
```
bash ./run_all.sh;
```

