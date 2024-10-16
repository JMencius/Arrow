#!/bin/bash

# Pipeline
# build directory structure
mkdir -p ../results/seq_identity;
mkdir -p ../results/QV_similarity;

# 1. Evaluate the sequence identity between HG002 R9 Guppy versions
bash HG002_R9_seq_identity.sh;

# 2. Evaluate the Bhattacharyya coeffient between HG002 R9 Guppy versions
bash HG002_R9_QV_sim.sh;


