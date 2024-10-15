# Description
This directory archives the pipelines for medaka polishing and polished assembly qv evaluation.


# Environment
1. `Medaka` environment is provided in `medaka.yaml`. To recreate this environment run
`conda env create -f medaka.yaml;`

1. `Yak` environment is provided in `yak.yaml`. To recreate this environment run
`conda env create -f yak.yaml;`


# Pipeline
1. Run `Medaka` polishing for R9G4FAST, R9G4HAC, R9G6FAST, R9G6HAC, R9G6SUP, R10D0HAC, and R10D0SUP data
`bash run_medaka_polishing.sh;`

2. Run `yak` evaluation for polished data
`bash cal_poshlied_yakQV.sh;`

