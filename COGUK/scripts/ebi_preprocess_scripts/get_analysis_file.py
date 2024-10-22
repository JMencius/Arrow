import argparse
import sys
import os


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "Input ENA analysis metadata txt", required = True, type = str)
parser.add_argument("-c", "--csv", help = "Intetsect csv file", required = True, type = str)
parser.add_argument("-o", "--output", help = "Output csv file", default = "", type = str)

args = parser.parse_args()
input_txt = os.path.abspath(args.input)
csvfile = os.path.abspath(args.csv)
output_csv = os.path.abspath(args.output)

# read csv file
COG = dict()
with open(csvfile, 'r') as f:
    linecount = 0
    for line in f:
        if linecount == 0:
            linecount += 1
            continue
        m = (line.strip()).split(',')
        COG[m[0]] = [m[1], m[2], m[3], m[4]]


analysis = dict()
with open(input_txt, 'r') as f:
    for line in f:
        m = line.split()
        if m:
            if m[-1] in COG:
                files = m[-2].split(';')
                fasta = ""
                for i in files:
                    if "fasta" in i:
                        fasta = i
                if fasta != "":
                    if m[-1] not in analysis:
                        analysis[m[-1]] = list()
                analysis[m[-1]].append(fasta)

double_file = dict()
for i in analysis:
    subject = analysis[i]
    if len(subject) == 2:
        if "climb" in subject[0] and "climb" not in subject[1]:
            double_file[i] = [subject[0], subject[1]]
        if "climb" not in subject[0] and "climb" in subject[1]:
            double_file[i] = [subject[1], subject[0]]

print(f"In total {len(double_file.keys())} groups have both NGS and ONT sequencing data and analysis file")

with open(output_csv, 'w') as f:
    f.write("id,ERR id,Download link,Device,Corresponding Illumina ERR id,ONT assembly, Illumina assembly\n")
    for i in double_file:
        f.write(f"{i},{COG[i][0]},{COG[i][1]},{COG[i][2]},{COG[i][3]},{double_file[i][0]},{double_file[i][1]}\n")

    print("ALL DONE")

