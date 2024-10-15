# Desciptions
This directory archives the pipelines for LongBow model training. Each model includes QV distribution and autocorrelation in `.csv` file. 
For autocorrelation, a leave-one-out test is also included to get the best lag.


# Execution environment
Use the LongBow environment for the following two pipelines
```bash
conda env create -f longbow.yaml;
```


# Pipelines
1. Calculate each model for every basecalling config for all the species
```bash
bash calculate_longbow_model_csv.sh
```
## Data for training
The description of each training data is located at `../data/Training_dataset_for_longbow.csv`


2. Conduct leave-one-out(LOO) test to determine the best lag for R9G4, R9G6, R9D0, R10G6, and R10D0
```bash
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R9G4_autocorrelation_lag_accuracy.txt --subject R9G4;
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R9G6_autocorrelation_lag_accuracy.txt --subject R9G6;
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R9D0_autocorrelation_lag_accuracy.txt --subject R9D0;
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R10G6_autocorrelation_lag_accuracy.txt --subject R10G6;
python autocorrelation_LOO_lag.py -i ../results/model -o ../results/R10D0_autocorrelation_lag_accuracy.txt --subject R10D0;

```

# Result description
1. The model for `LongBow` is located in `../results/model`, which consists of 90 csv files. These csv files are the exact model files for LongBow

2. The result of the LOO test is located in `../results`, 5 txt files record the accuracy verus different lag in different basecalling configurations.
