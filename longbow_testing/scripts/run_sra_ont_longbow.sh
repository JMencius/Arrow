$!/bin/bash
cd ../data/sra_human_10Kreads;
for i in *.fastq; do
	echo "$i";
	python ../../longbow_code/longbow2.0.4/longbow.py -t 48 -i "$i" -b -o ../results/sra_human/"$i".json;
done
