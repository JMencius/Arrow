#!/bin/bash

# build directory structure
for i in R9G4FAST R9G4HAC R9G6FAST R9G6HAC R9G6SUP R10D0HAC R10D0SUP;do
	for j in R9G4FAST R9G4HAC R9G6FAST R9G6HAC R9G6SUP R10D0HAC R10D0SUP;do
		mkdir -p ../results/"$i"/"$i"_"$j";
	done
done


# medaka polishing for R9G4FAST
bash R9G4FAST_medaka.sh;

# medaka polishing for R9G4HAC
bash R9G4HAC_medaka.sh;

# medaka polishing for R9G6FAST
bash R9G6FAST_medaka.sh;

# medaka polishing for R9G6HAC
bash R9G6HAC_medaka.sh;

# medaka polishing for R9G6SUP
bash R9G6SUP_medaka.sh;

# medaka polishing for R10D0HAC
bash R10D0HAC_medaka.sh;

# medaka polishing for R10D0SUP
bash R10D0SUP_medaka.sh;
