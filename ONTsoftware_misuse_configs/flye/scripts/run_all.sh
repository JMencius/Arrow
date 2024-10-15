#!/bin/bash

## Pipeline
## 1. Assembly draft for different HG002 basecalling configuration
bash flye_draft.sh;

## 2. Calculate draft QV
bash draft_QV_calculation.sh;
