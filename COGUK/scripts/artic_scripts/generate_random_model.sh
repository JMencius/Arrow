#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate python3-env;

# generate random model using seed = 100
python random_model.py ../err_id.txt ../ERR_list_models.txt;
