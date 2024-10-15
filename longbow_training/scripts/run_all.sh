#!/bin/bash

# Pipeline
# 1. Calculate each model for every basecalling config for all the species
bash calculate_longbow_model_csv.sh


# 2. Conduct leave-one-out test to determine the best lag for R9G4, R9G6, R9D0, R10G6, and R10D0
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R9G4_autocorrelation_lag_accuracy.txt --subject R9G4;
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R9G6_autocorrelation_lag_accuracy.txt --subject R9G6;
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R9D0_autocorrelation_lag_accuracy.txt --subject R9D0;
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R10G6_autocorrelation_lag_accuracy.txt --subject R10G6;
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R10D0_autocorrelation_lag_accuracy.txt --subject R10D0;
