#!/bin/bash

mkdir -p ../../ref;
# git clone https://github.com/artic-network/primer-schemes.git ../../ref;

wget -nc -P ../../ref https://github.com/artic-network/primer-schemes/archive/refs/heads/master.zip;

unzip ../../ref/master.zip -d ../../ref;
mv ../../ref/primer-schemes-master/* ../../ref/;
