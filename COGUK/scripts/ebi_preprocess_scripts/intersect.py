import argparse
import sys
import os


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "Input ENA metadata txt", required = True, type = str)
parser.add_argument("-o", "--output", help = "Output csv file", default = "", type = str)

args = parser.parse_args()
input_txt = os.path.abspath(args.input)
output_csv = os.path.abspath(args.output)


illumina = dict()
with open(input_txt, 'r') as f:
    for line in f:
        if "Illumina" in line:
            m = line.split()
            illumina[m[-1]] = m[3]

print("Intersecting NGS and ONT data")

count = 0
intersect = list()
with open(input_txt, 'r') as f:
    for line in f:
        device = ""
        if "PromethION" in line:
            device = "PromethION"
        if "GridION" in line:
            device = "GridION"
        if "MinION" in line:
            device = "MinION"
        
        if device != "":
            m = line.split()
            if m[-1] in illumina:
                count += 1
                download_link = m[-3]
                intersect.append([m[-1], m[3], m[-3], device, illumina[m[-1]]])



with open(output_csv, 'w') as file:
    file.write("id,ERR id,Download link,Device,Corresponding Illumina ERR id\n")
    for i in intersect:
        file.write(','.join(i))
        file.write('\n')


