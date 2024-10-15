import os
import re
import xml.etree.ElementTree as ET
from multiprocessing import Pool
from datetime import datetime
import argparse


def scan_through(dirname : str) -> list:
    if dirname not in all_dir:
        return None
    if dirname == None:
        return None
    basecaller_version = 0
    flowcell_version = 0

    for filename in os.listdir(dirname):
        if os.path.isfile(os.path.join(dirname, filename)):
            if basecaller_version == 1 and flowcell_version == 1:
                break
            with open(os.path.join(dirname, filename)) as f:
                for line in f:
                    if basecaller_version != 1:
                        if albacore_pattern.search(line) or guppy_pattern.search(line) or dorado_pattern.search(line):
                            basecaller_version = 1

                    if flowcell_version != 1:
                        # if flowcell_pattern.search(line) or normal_kit_pattern.search(line) or special_kit_pattern.search(line):
                        #    flowcell_version = 1
                        if flowcell_pattern.search(line) or normal_kit_pattern.search(line) or special_kit_pattern.search(line):
                            # print(line)
                            flowcell_version = 1
    
    return [basecaller_version, flowcell_version]


def read_csv(filename : str) -> list:
    outlist = list()
    linecount = 0
    with open(filename, 'r') as f:
        for line in f:
            # skip header
            if linecount == 0:
                linecount += 1
                continue
            temp = line.strip()
            if temp:
                outlist.append(temp)

    return outlist


def map_SRA(accession_file : str, target : list) -> list:
    linecount = 0
    trans = list()
    accession_dict = dict()
    with open(accession_file, 'r') as f:
        for line in f:
            if linecount == 0:
                linecount += 1
                continue
            m = line.split()
            if len(m) > 3:
                accession_dict[m[0]] = m[1]

    for i in target:
        if i in accession_dict:
            trans.append(accession_dict[i])
        else:
            trans.append(None)
    
    assert len(trans) == len(target)
    return trans
                


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Path to the input xml directory", required = True, type = str)
    parser.add_argument("-q", "--query", help = "Target SRA accession file to query", required = True, type = str)
    parser.add_argument("-t", "--threads", help = "Number of parallel threads", default = 12, type = int)
    parser.add_argument("-a", "--accession", help = "Path to the input accession file", required = True, type = str)
    parser.add_argument("-o", "--output", help = "Path to the output csv file", required = True, type = str)


    args = parser.parse_args()
    xml_path = os.path.abspath(args.input)
    query = os.path.abspath(args.query)
    accession_file = os.path.abspath(args.accession)
    output_file = os.path.abspath(args.output)
    threads = args.threads


    os.chdir(xml_path)
    all_dir = set(os.listdir(xml_path))
    directory = os.getcwd()
    print(f"Current working directory is {directory}")

    
    albacore_pattern = re.compile(r'albacore\s*(?:v)?\d+(\.\d+)*', re.IGNORECASE)
    guppy_pattern = re.compile(r'guppy\s*(?:v)?\d+(\.\d+)*', re.IGNORECASE)
    dorado_pattern = re.compile(r'dorado\s*(?:v)?\d+(\.\d+)*', re.IGNORECASE)
    
    flowcell_pattern = re.compile(r"(\s[rR]10(\.|\s)|\s[rR]9(\.|\s)|\s[rR]7(\.|\s))")
    normal_kit_pattern = re.compile(r'^ (MIN|FLG|PRO|DCS|LRK|LSK|LWP|PCS|PSK|RAD|RAS|RLI|VBK|VSK|LWB|PBK|RAB|RLB|RPB|VMK|NBD|RBK|PTC|RLI)?-?\d{3} $', re.IGNORECASE)
    special_kit_pattern = re.compile(r" (MINSP6|MIN-SP6|CS9109|CS-9109|16S024|16S-024) ", re.IGNORECASE)
 
    
    target_dir = read_csv(query)
    
    print(f"Total target SRA run number : {len(target_dir)}")
    
    map_dir = map_SRA(accession_file, target_dir)
    

    with Pool(threads) as p:
        output = p.map(scan_through, [d for d in map_dir])
    
    
    yes_basecaller_version = 0
    yes_flowcell_version = 0
    both = 0
    for i in output:
        if i != None:
            yes_basecaller_version += i[0]
            yes_flowcell_version += i[1]
            if i[0] != 0 and i[1] != 0:
                both += 1
    print(f"Total SRA run : {len(target_dir)}")
    print(f"SRA run with basecaller version : {yes_basecaller_version}")
    print(f"SRA run with flowcell version : {yes_flowcell_version}")
    print(f"SRA run with basecaller version and flowcell version : {both}")

    print("\n")
    print("Writing to summary csv file")
    with open(output_file, 'w') as f:
        f.write("SRR id,basecaller version,flowcell version,both\n")
        for i in range(len(target_dir)):
            if output[i] == None:
                f.write(f"{target_dir[i]},0,0,0\n")
            else:
                if output[i][0] != 0 and output[i][1] != 0:
                    f.write(f"{target_dir[i]},1,1,1\n")
                else:
                    f.write(f"{target_dir[i]},{output[i][0]},{output[i][1]},0\n")
    print("ALL DONE")


    





