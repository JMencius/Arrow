# Raw nanopore data(FAST5/POD5) availabilty in SRA database

## Search command
We use the [SRA Advanced Search Builder](https://www.ncbi.nlm.nih.gov/sra/advanced) in SRA database. <br>
Search command to obtain the number with ONT raw data (**N<sub>raw</sub>**)
```
((("oxford nanopore"[Platform]) AND "filetype nanopore"[Properties]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date]) 
```


Search command to obtain the total number of ONT data (**N<sub>total</sub>**)
```
(("oxford nanopore"[Platform]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date]) 
```
The proportion of Raw nanopore data(FAST5/POD5) availabilty in SRA database is calculated by **N<sub>raw</sub>/N<sub>total</sub>**


## Workflow
1. Conduct each search command.
2. Use `Send to`-`File`-`Format Accession List` to download the SRR list of each search in `.csv` format.
3. Summarize the numbers of SRR list in each categories.


## Results 
| Category | CSV file | Count |
|:---:|:---:|:---:|
| Total number of ONT data | `../results/SRA_ONT_ALL_accession_list.csv` | 683,884 |
| Raw nanopore data available | `../results/ONT_RAW_accession_list.csv` | 12,330 |



## Notice
<mark> Note: one may get different exact number of **N<sub>raw</sub>** or **N<sub>total</sub>**, due to different search date, some accession of the SRA will be deleted or added, so the exact number changes a little bit. </mark>
