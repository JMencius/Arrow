import os
import random
import argparse


def read_SRA_run(filename : str) -> list():
    linecount = 0
    SRA_ONT_all = list()
    with open(filename, 'r') as f:
        for line in f:
            # skip header
            if linecount == 0:
                linecount += 1
                continue
            SRA_ONT_all.append(line.strip())

    return SRA_ONT_all


            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Path to the input whole SRA csv to be sampled", required = True, type = str)
    parser.add_argument("-o", "--output", help = "Path to the output SRA csv", required = True, type = str)    
    
    args = parser.parse_args()
    infile = os.path.abspath(args.input)
    outfile = os.path.abspath(args.output)

    all_sra_ont = read_SRA_run(infile)
    random.seed(100)
    sampled_sra_run = random.sample(all_sra_ont, 1000)
    
    # print(sampled_sra_run[:10])

    with open(outfile, 'w') as g:
        for i in sampled_sra_run:
            g.write(str(i) + '\n')

    print("Written to outfile. Completed")
