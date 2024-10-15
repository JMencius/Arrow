import argparse
import os

def read_list(filename: str) -> list:
    to_process = list()
    with open(filename, 'r') as f:
        for line in f:
            m = line.strip()
            if m:
                to_process.append(m)

    return to_process

def parse_hap(filename: str, mode: str) -> tuple:
    TP, FP, FN = 0, 0, 0
    with open(filename, 'r') as f:
        for line in f:
            m = line.split(',')
            if m[1] == "PASS" and mode in line:
                TP = int(m[3])
                FP = int(m[6])
                FN = int(m[4])
    return (TP, FP, FN)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", help = "ERR list", required = True, type = str)
    parser.add_argument("-d", "--dir", help = "Directory contains hap.py results", required = True, type = str)
    parser.add_argument("-o", "--output", help = "Output csv file", required = True, type = str)
    parser.add_argument("-m", "--mode", help = "Mode for evluation, option : [SNP, INDEL]", required = True, type = str)
    parser.add_argument("-p", "--prefix", help = "prefix for hap file", required = True, type = str)

    args = parser.parse_args()
    
    ERR_list = os.path.abspath(args.list)
    work_dir = os.path.abspath(args.dir)
    output_file = os.path.abspath(args.output)
    mode = str(args.mode)
    prefix = str(args.prefix)

    # check parameters
    if mode not in {"SNP", "INDEL"}:
        raise ValueError(r"-m or --model must be either SNP or INDEL")
    
    os.chdir(work_dir)

    to_process = read_list(ERR_list)    
    
    TP, FP, FN = 0, 0, 0
    for err_id in to_process:
        ##print(err_id)
        subject = f"{err_id}_{prefix}.summary.csv"
        t = parse_hap(subject, mode)
        TP += t[0]
        FP += t[1]
        FN += t[2]

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    F1 = 2 * precision * recall / (precision + recall)
    print(f"Total F1 score is : {F1}")

    with open(output_file, 'w') as of:
        of.write("sample,mode,TP,FP,FN,precision,recall,F1\n")
        of.write(f"{prefix},{mode},{TP},{FP},{FN},{precision},{recall},{F1}\n")











