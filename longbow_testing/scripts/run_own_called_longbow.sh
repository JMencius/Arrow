$!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;


cd ../data/test_data_assemble;
for i in *.fastq; do
	echo "$i";
	python ../../longbow_code/longbow2.0.4/longbow.py -t 48 -i "$i" -b -o ../results/own_called/"$i".json;
done
