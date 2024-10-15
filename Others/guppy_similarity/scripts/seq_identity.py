# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:59:58 2023

@author: Mencius
"""
import os
import sys
import argparse
import time
import mappy as mp
import pyfastx
from multiprocessing import Pool



def extract_read_from_fastq(filename : str) -> dict:
    read_dict= dict()
    for name, seq, qual in pyfastx.Fastq(filename, build_index = False):
        read_name = name.split()[0]
        clean_seq = seq.strip()
        read_dict[read_name] = clean_seq

    return read_dict


            
def cal_identity(r1 : str, r2 : str) -> tuple:
    a = mp.Aligner(seq = r1, preset = "map-ont", n_threads = 1)
    align = a.map(r2)
    for hit in align:
        return (int(hit.mlen), int(hit.blen))



if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--ref", help = "Reference fastq for input", required = True, type = str)
    parser.add_argument("-q", "--query", help = "Query fastq for input", required = True, type = str)
    parser.add_argument("-t", "--threads", help = "Number of parallel threads", default = 12, type = int)

    args = parser.parse_args()
    ref = os.path.abspath(args.ref)
    query = os.path.abspath(args.query)
    threads = int(args.threads)

    fastq1 = extract_read_from_fastq(ref)
    fastq2 = extract_read_from_fastq(query)

    ##print(f"There are {len(fastq1.keys())} reads in the first FASTQ")
    ##print(f"There are {len(fastq2.keys())} reads in the second FASTQ")
    
    # find in common reads 
    common_keys = list()
    for key in fastq1:
        if key in fastq2:
            common_keys.append(key)

    ##print(f"There are {len(common_keys)} in common.")


    cores = threads
    with Pool(cores) as p:
        identity = p.starmap(cal_identity, [(fastq1[i], fastq2[i]) for i in common_keys])

    sum_base = 0
    match_base = 0
    for i in identity:
        if i != None:
            match_base += i[0]
            sum_base += i[1]

    avg_identity = match_base / sum_base
    print(f"Average pairwise sequence identity for {args.ref} and {args.query} is {avg_identity}")

    end_time = time.time()
    ##print(f"Running time is {end_time - start_time} seconds.")
    

