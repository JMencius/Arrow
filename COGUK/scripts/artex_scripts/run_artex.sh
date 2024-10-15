#!/bin/bash

# run artex pipeline on LongBow+artic pipeline result
bash artex_on_longbow.sh;

# unfiy vcf file using bcftools
bash artex_convert_vcf.sh;

# evaluat3e artex pipeline using hap.py
bash artex_hap.sh;


