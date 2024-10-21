#!/bin/bash

# build directory structure
for i in R9G4FAST R9G4HAC R9G6FAST R9G6HAC R9G6SUP R10D0FAST R10D0HAC R10D0SUP;do
        for j in R9G4 R9G6SUP R10;do
                mkdir -p ../results/"$i"_"$j";
        done
done

# change the shasta permissions
chmod +x ./shasta-Linux-0.11.1;
chmod +x ./calN50.js;


# Pipeline
## We enumerate all the configs for all the data.
# 1. run HG002 R9G4FAST shasta and evaluation
bash R9G4FAST_shasta_yak_NG50.sh;

# 2. run HG002 R9G4HAC shasta
#bash R9G4HAC_shasta_yak_NG50.sh;

# 3. run HG002 R9G6FAST shasta
#bash R9G6FAST_shasta_yak_NG50.sh;

# 4. run HG002 R9G6HAC shasta
#bash R9G6HAC_shasta_yak_NG50.sh;

# 5. run HG002 R9G6SUP shasta
#bash R9G6SUP_shasta_yak_NG50.sh;

# 6. run HG002 R10D0FAST shasta
#bash R10D0FAST_shasta_yak_NG50.sh;

# 7. run HG002 R10D0HAC shasta
#bash R10D0HAC_shasta_yak_NG50.sh;

# 8. run HG002 R10D0SUP shasta
#bash R10D0SUP_shasta_yak_NG50.sh;
