#!/bin/bash

# Pipeline

# build directory structure
mkdir -p ../results;

# 1. Download short reads data
bash download_ngs.sh;

# 2. Build k-mer refernce hash table
bash build_yak.sh;
