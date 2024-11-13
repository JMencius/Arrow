# Raw nanopore data(FAST5/POD5) availability in SRA database

## Search command
We use the [SRA Advanced Search Builder](https://www.ncbi.nlm.nih.gov/sra/advanced) in SRA database. <br>
1. Search command to obtain the number of SRA run with ONT raw data (**N<sub>raw</sub>**)
```
((("oxford nanopore"[Platform]) AND "filetype nanopore"[Properties]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date]) 
```


2. Search command to obtain the total number of ONT data (**N<sub>total</sub>**)
```
(("oxford nanopore"[Platform]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date]) 
```
The proportion of Raw nanopore data(FAST5/POD5) availability in SRA database is calculated as **N<sub>raw</sub>/N<sub>total</sub>**


## Pipeline
1. Execute each search command.
2. Use `Send to`-`File`-`Format Accession List` to download the SRR list in `.csv` format.
3. Summarize the numbers of SRR run in each category's csv file.


## Note
Note: one may get a different exact number of **N<sub>raw</sub>** or **N<sub>total</sub>**, due to different search dates. Some accession of the SRA will be deleted or added, causing slight changes in total counts, but the proportion will remain comparable. 
