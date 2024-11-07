# Shasta
## Descriptions 
This directory archives the pipeline which we benchmark shasta *de novo* assembly with different config.


## Execution environments
1. For `Shasta`, we download the `Shasta` binary executable from GitHub <https://github.com/paoloshasta/shasta/releases> version 0.11.0
```bash
wget https://github.com/paoloshasta/shasta/releases/download/0.11.0/shasta-Linux-0.11.0;
```

2. For `yak`, we set up the `conda` environment as follow:
```bash
conda env create -f yak.yaml;
```

3. For `calN50`, we download the release from github <https://github.com/lh3/calN50>, to recreate our running virtual environment run:
```bash
conda env create -f caln50.yaml;
```


## Pipelines
1. Make sure you have run the pipeline in ../../yak/scripts/README.md. The evaluation is based on yak using short-read NGS data.

2. Build directory structure and add execution permissions
```bash
# build directory structure
for i in R9G4FAST R9G4HAC R9G6FAST R9G6HAC R9G6SUP R10D0FAST R10D0HAC R10D0SUP;do for j in R9G4 R9G6SUP R10;do mkdir -p ../results/"$i"_"$j"; done; done;

# change the shasta permissions
chmod +x ./shasta-Linux-0.11.1;
chmod +x ./calN50.js;
```

3. Enumerate all the Shasta configs for all the data and use `calN50` to calculate `NG50`, use `yak` to calculate `yak QV score`.
```bash
bash R9G4FAST_shasta_yak_NG50.sh;
bash R9G4HAC_shasta_yak_NG50.sh;
bash R9G6FAST_shasta_yak_NG50.sh;
bash R9G6HAC_shasta_yak_NG50.sh;
bash R9G6SUP_shasta_yak_NG50.sh;
bash R10D0FAST_shasta_yak_NG50.sh;
bash R10D0HAC_shasta_yak_NG50.sh;
bash R10D0SUP_shasta_yak_NG50.sh;
```

## Shasta parameters
The correct Shasta parameters for different flowcell and basecaller versions of HG002 data is listed below.
| Flowcell type | Basecaller | Basecalling model | Shasta parameter `--config` |
|:---:|:---|:---:|:---:|
| R9 | Guppy4.2.2 | FAST | Not available |
| R9 | Guppy4.2.2 | HAC | Nanopore-Sep2020 |
| R9 | Guppy6.3.8 | FAST | Not available |
| R9 | Guppy6.3.8 | HAC | Not available |
| R9 | Guppy6.3.8 | SUP | Nanopore-May2022 |
| R10 | Dorado0.4.3 | FAST | Not available |
| R10 | Dorado0.4.3 | HAC | Not available |
| R10 | Dorado0.4.3 | SUP | Nanopore-R10-Fast-Nov2022 |


## Results descriptions
1. Naming pattern 
For example: `R10D0FAST_R9G4` means `R10D0FAST` basecalled FASTQ data using `shasta` config for `R9G4` data.

2. NG50
`calN50_result.txt` holds the `NG50` result in line start with
 ```
NL      50
```
For example:
```
NL      50      12529106        66
```

4. Yak QV score
`yak.txt` holds the `Yak QV score` result in the last line of the file
For example:
```
QV      28.775  29.115
```
We record the second value (29.115), which is the `adjusted_quality_value` reported by `Yak`.


## Repeat our results
To repeat our results, please install the aforementioned conda environment first and run
```
bash ./run_all.sh;
```

<mark>Shasta is a memory-intensive program. Please ensure you have at least 1 TB of physical RAM to successfully repeat our results.</mark>
