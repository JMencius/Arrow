# Descriptions
This diectory archives the pipeline for sequence identity and QV score similarity between Guppy versions.

We use the dataset HG002 sequenced with R9.4.1 flowcell (https://labs.epi2me.io/gm24385_2021.05) to evaluate the sequence identity and QV score similarity.


# Execution environments
1. To recreate the Python virtual environment for sequence identity, run the following command.
`conda env create -f mappy.yaml;`

2. To recreate the Python virtual environment for QV similarity analysis, just use the longbow environment.
`conda env create -f ont-longbow.yaml;`

# Pipelines
1. Evaluate the sequence identity between HG002 R9 Guppy version
`bash HG002_R9_seq_identity.sh > ../results/HG002_R9_seq_identity.txt;`

2. Evaluate the Bhattacharyya coeffient between HG002 R9 Guppy version
`bash HG002_R9_QV_sim.sh > ../results/HG002_R9_qv_sim.txt`


