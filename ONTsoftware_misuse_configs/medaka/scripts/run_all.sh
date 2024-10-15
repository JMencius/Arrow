#!/bin/bash


# Pipeline
# 1. Run `Medaka` polishing for R9G4FAST, R9G4HAC, R9G6FAST, R9G6HAC, R9G6SUP, R10D0HAC, and R10D0SUP data
bash run_medaka_polishing.sh;

# 2. Run `yak` evaluation for polished data
bash cal_poshlied_yakQV.sh;

