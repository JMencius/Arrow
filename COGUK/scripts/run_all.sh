#!/bin/bash

# Preprocess
cd ./ebi_preprocess_scripts;
bash preprocess.sh;
cd ..;

# Download data
cd ./download_scripts;
bash download_all.sh;
cd ..;

# LongBow config prediction
cd ./longbow_pred_script;
bash ./run_longbow.sh;
cd ..;

# Run Artic
cd ./artic_scripts;
bash ./run_artic.sh;
cd ..

# Run Artex
cd ./artex_scripts;
bash ./run_artex.sh;
cd ..

# Run post analysis
cd ./post_analysis;
bash ./post_analysis.sh;
cd ..


