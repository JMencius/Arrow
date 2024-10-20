# Descriptions 
This directory archive the pipeline which we benchmark shasta *de novo* assembly with different config.


# Execution environments
1. For `shasta`, we download the shasta binary executable from shasta github <https://github.com/paoloshasta/shasta/releases> version 0.11.0
```bash
wget https://github.com/paoloshasta/shasta/releases/download/0.11.0/shasta-Linux-0.11.0;
```

2. For `yak`, we set up the `conda` environment as follow:
```bash
conda env create -f yak.yaml;
```

3. For `calN50`, we download the release from github <https://github.com/lh3/calN50>, the recreate the running virtual environmnet
```bash
conda env create -f caln50.yaml;
```


# Pipeline
We enumerate all the Shasta configs for all the data and use `calN50` to calculate `NG50`, use `yak` to calculate `yak QV score`.
```
bash R9G4FAST_shasta_yak_NG50.sh;
bash R9G4HAC_shasta_yak_NG50.sh;
bash R9G6FAST_shasta_yak_NG50.sh;
bash R9G6HAC_shasta_yak_NG50.sh;
bash R9G6SUP_shasta_yak_NG50.sh;
bash R10D0FAST_shasta_yak_NG50.sh;
bash R10D0HAC_shasta_yak_NG50.sh;
bash R10D0SUP_shasta_yak_NG50.sh;
```

# Results descriptions
1. Naming pattern 
For example: `R10D0FAST_R9G4` means `R10D0FAST` basecalled FASTQ data using `shasta` config for `R9G4` data.

2. NG50
`calN50_result.txt` holds the `NG50` result in line start with `NL      50`
For example:
`NL      50      12529106        66`

3. Yak QV score
`yak.txt` holds the `Yak QV score` result in the last line
For example:
`QV      28.775  29.115`
We record the second value (29.115), which is the `adjusted_quality_value` reported by `Yak`.


# Repeat our results
To repeat our results, please install the forementioned conda environment first and run
```
bash ./run_all.sh;
```

