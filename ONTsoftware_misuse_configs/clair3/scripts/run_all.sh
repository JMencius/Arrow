#!/bin/bash

# Prepare reference
cd ./prepare;
bash ./prepare.sh;
cd ..;

# Alignment
cd ./alignment;
bash ./alignment.sh;
cd ..;

# Variant calling
cd ./variant_calling;
bash ./clair3.sh;
cd ..;


# Benchmarking
cd ./benchmark;
bash ./benchmark.sh;
cd ..;
