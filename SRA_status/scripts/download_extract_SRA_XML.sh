#!/bin/bash

# Download all the XML metadata from SRA ftp server
wget -P ../data ftp://ftp.ncbi.nlm.nih.gov/sra/reports/Metadata/NCBI_SRA_Metadata_Full_20240120.tar.gz;

# Decompress the SRA xml metadata into a directory
## To be notice, there will be millions of SRA directory, so the decompression will be very slow
mkdir -p ../data/xml;
tar -C ../data/xml/ -zxf NCBI_SRA_Metadata_Full_20240120.tar.gz;

