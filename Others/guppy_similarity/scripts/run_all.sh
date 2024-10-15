#!/bin/bash

# Pipeline
# 1. Evaluate the sequence identity between HG002 R9 Guppy version
#bash HG002_R9_seq_identity.sh > ../results/HG002_R9_seq_identity.txt;

# 2. Evaluate the sequence identity between HG002 R10 4kHz models
#bash HG002_R10_4kHz_seq_identity.sh > ../results/HG002_R10_4kHz_seq_identity.txt;

# 3. Evaluate the sequence identity between HG002 R10 5kHz models
#bash HG002_R10_5kHz_seq_identity.sh > ../results/HG002_R10_5kHz_seq_identity.txt;

# 4. Evaluate the Bhattacharyya coeffient between HG002 R9 Guppy version
bash HG002_R9_QV_sim.sh > ../results/HG002_R9_qv_sim.txt

# 5. Evaluate the Bhattacharyya coeffient between HG002 R10 4kHz models
bash HG002_R10_4kHz_QV_sim.sh > ../results/HG002_R10_4kHz_qv_sim.txt

# 6. Evaluate the Bhattacharyya coeffient between HG002 R10 5kHz models
bash HG002_R10_5kHz_QV_sim.sh > ../results/HG002_R10_5kHz_qv_sim.txt

