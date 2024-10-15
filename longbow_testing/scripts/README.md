# Description
This directory archives the testing pipeline to evaluate the LongBow performance. The test data containing two seperate categories : 

1. our own basecalled data using raw FAST5/POD5 data; 

2. human ONT sequencing data on SRA database till 01/09/2024.


# Execution environment
Use the LongBow environment
```bash
conda env create -f longbow.yaml;
```

# Pipelines
1. Test LongBow on our own basecalled data
1.1 Run LongBow and get `.json output`
`bash run_own_called_longbow.sh;`

1.2 Summarize the our own basecalled results
`python analysis_own_called_result.py -i ../results/own_called -o ../results/own_called.csv;`

2. Run LongBow on human ONT SRA data
2.1 Download human ONT SRA data top 10,000 sequence
`python download_all_sra_ont.py -t 16 -o ../results/sra_human -p ./sratoolkit/sratoolkit.3.0.7-ubuntu64/bin -i sra_list.txt;`

2.2 Run LongBow on human ONT SRA data
`bash run_sra_ont_longbow.sh;`

2.3 Summarize the human ONT SRA results
`python analysis_sra_ont.py -i ../results/sra_human -s ../data/sra_human_10Kreads -l sra_list.txt -o ../results/sra_ont_result.csv;`


# Result descriptions
1. LongBow test results on our own basecalled data is  `../results/own_called.csv`;


2. LongBow test results on ONT SRA data is in `../results/sra_ont_results.csv`.

