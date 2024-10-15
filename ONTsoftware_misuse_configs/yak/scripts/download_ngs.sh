#!/bin/bash

# retrive the ~30X PCR-free Illumina 150bp sequencing file from human pangenome
wget -P ../data https://s3-us-west-2.amazonaws.com/human-pangenomics/NHGRI_UCSC_panel/HG002/hpp_HG002_NA24385_son_v1/ILMN/downsampled/HG002_HiSeq30x_subsampled_R1.fastq.gz;
wget -P ../data https://s3-us-west-2.amazonaws.com/human-pangenomics/NHGRI_UCSC_panel/HG002/hpp_HG002_NA24385_son_v1/ILMN/downsampled/HG002_HiSeq30x_subsampled_R2.fastq.gz;

# Decompress the files
cd ../data;
gzip -dk HG002_HiSeq30x_subsampled_R1.fastq.gz;
gzip -dk HG002_HiSeq30x_subsampled_R2.fastq.gz;

