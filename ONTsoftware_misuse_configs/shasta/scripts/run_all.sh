#!/bin/bash

# Pipeline
#We enumerate all the configs for all the data.
#1. run HG002 R9G4FAST shasta and evaluation
bash R9G4FAST_shasta_yak_NG50.sh;

#2. run HG002 R9G4HAC shasta
bash R9G4HAC_shasta_yak_NG50.sh;

#3. run HG002 R9G6FAST shasta
bash R9G6FAST_shasta_yak_NG50.sh;

#4. run HG002 R9G6HAC shasta
bash R9G6HAC_shasta_yak_NG50.sh;

#5. run R9G6SUP shasta
bash R9G6SUP_shasta_yak_NG50.sh;

#6. run R10D0FAST shasta
bash R10D0FAST_shasta_yak_NG50.sh;

#7. run R10D0HAC shasta
bash R10D0HAC_shasta_yak_NG50.sh;

#8. run R10D0SUP shasta
bash R10D0SUP_shasta_yak_NG50.sh;
