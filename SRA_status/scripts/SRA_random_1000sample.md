# Random selection of 1000 SRA run

## Prepare data
First we collect all the sra run while excluding COVID, due to its large proportion.
The search command in `SRA advanced serach` is
```
(("oxford nanopore"[Platform]) NOT Severe acute respiratory syndrome-related coronavirus[Organism]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date])
```
The export accession file from the following search is in ../data/SraAccList_NOCOVID_20240109.csv

## Random selection
```
python random_select_SRARUN.py -i ../data/SraAccList_NOCOVID_20240109.csv -o ../results/Sampled_1000_srarun.txt;
```

We manually evaluate the first 100 runs in `Sampled_1000_srarun.txt`.

