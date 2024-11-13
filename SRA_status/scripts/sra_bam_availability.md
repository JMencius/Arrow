# BAM availability in SRA database
We use the [SRA Advanced Search Builder](https://www.ncbi.nlm.nih.gov/sra/advanced) in SRA database. <br>

## Search command
### BAM availability in all species
1. Search command to obtain the total number of ONT data in all species
```
(("oxford nanopore"[Platform]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date]) 
```

2. Search command to obtain the number of BAM file availability in all species
```
(("oxford nanopore"[Platform]) AND "filetype bam"[Properties]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date])
```

### BAM availability in species excluding severe acute respiratory syndrome-related coronavirus
Severe acute respiratory syndrome-related coronavirus(HCoV-SARS) NCBI Taxonomy ID is [694009](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=694009). 
1. Search command to obtain the total number of ONT data in species excluding HCoV-SARS
```
(("oxford nanopore"[Platform]) NOT Severe acute respiratory syndrome coronavirus 2[Organism]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date]) 
```

2. Search command to obtain the number of BAM available in species excluding HCoV-SARS
```
(("oxford nanopore"[Platform]) AND "filetype bam"[Properties]) NOT Severe acute respiratory syndrome coronavirus 2[Organism]) AND ("2010/01/01"[Publication Date] : "2024/01/09"[Publication Date])
```

## Pipeline
1. Conduct each search command.
2. Use `Send to`-`File`-`Format Accession List` to download the SRR list of each search.
3. Summarize the numbers of SRR run in each category.


## Note
Note: one may get a different exact number may change due to different search dates, some accession of the SRA will be deleted or added, causing slight changes in the total counts, but the proportion will remain comparable.
