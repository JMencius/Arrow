# Raw nanopore data(FAST5/POD5) availabilty in SRA database

## Search command
We use the [SRA Advanced Search Builder](https://www.ncbi.nlm.nih.gov/sra/advanced) in SRA database. <br>
1. Search command to obtain the number with ONT raw data (**N<sub>raw</sub>**)
```
((("oxford nanopore"[Platform]) AND "filetype nanopore"[Properties]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date]) 
```


2. Search command to obtain the total number of ONT data (**N<sub>total</sub>**)
```
(("oxford nanopore"[Platform]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date]) 
```
    The proportion of Raw nanopore data(FAST5/POD5) availability in SRA database is calculated by **N<sub>raw</sub>/N<sub>total</sub>**


## Pipeline
1. Conduct each search command.
2. Use `Send to`-`File`-`Format Accession List` to download the SRR list of each search in `.csv` format.
3. Summarize the numbers of SRR list in each category.


## Note
<mark> Note: one may get different exact number of **N<sub>raw</sub>** or **N<sub>total</sub>**, due to different search date, some accession of the SRA will be deleted or added, causing slight changes in total counts, but the proportion will remain comparable. </mark>
