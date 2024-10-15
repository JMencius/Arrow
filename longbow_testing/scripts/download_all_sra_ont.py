import os
import sys
from multiprocessing import Pool
import argparse
import subprocess


def download_sra_reads(srr : str, output : str, fastqdump_path : str) -> None:
    target_folder = output
    if not os.path.exists(f"{srr}.fastq"):
        try:
            result = subprocess.run(f"{fastqdump_path}/fastq-dump {srr} -N 1 -X 10000 -Q 33;", shell=True, cwd=target_folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check = True)

            print(f"{srr} download successful.")
        except Exception as e:
            print(f"An error occurred during download: {srr}")




def read_sra_id(srafile : str) -> list:
    sra_id = list()
    with open(srafile, 'r') as f:
        for line in f:
            m = line.strip()
            if m and (m not in sra_id):
                sra_id.append(m)

    return sra_id



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Input SRR file", required = True, type = str)
    parser.add_argument("-t", "--threads", help = "Parallel download threads", required = True, type = int)
    parser.add_argument("-o", "--output", help = "Output directory", required = True, type = str)
    parser.add_argument("-p", "--path", help = "Path to the executable fastq-dump", required = True, type = str)
    args = parser.parse_args()
    
    output_path = os.path.abspath(args.output)
    fastqdump_path = os.path.abspath(args.path)
    srafile = str(args.input)
    sra_id = read_sra_id(srafile)
    
    threads = int(args.threads)
    with Pool(threads) as p:
        result = p.starmap(download_sra_reads, [(i, output_path, fastqdump_path ) for i in sra_id])

    print("ALL DONE")
    
