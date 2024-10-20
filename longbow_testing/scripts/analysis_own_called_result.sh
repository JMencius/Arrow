#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;

# read json file output by longbow and summarize results
python analysis_own_called_result.py -i ../results/own_called -o ../results/own_called.csv;

