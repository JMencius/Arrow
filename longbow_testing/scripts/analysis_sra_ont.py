import argparse
import os
import re



def parse_json(json_file : str) -> list:
    with open(json_file) as f:
        flowcell = ""
        software = ""
        version = ""
        mode = ""
        readqv = ""
        for line in f:
            if "Read QV cutoff" in line:
                m = line.split('"')
                readqv = m[-2]

            if "Flowcell" in line:
                if "R9" in line:
                    flowcell = "R9"
                else:
                    flowcell = "R10"
            if "Software" in line:
                if "guppy" in line:
                    software = 'guppy'
                else:
                    software = 'dorado'
            if "Version" in line:
                if "2" in line:
                    version = '2'
                if "3or4" in line:
                    version = '3or4'
                if "5or6" in line:
                    version = '5or6'
                if '0' in line:
                    version = '0'
            if "Mode" in line:
                if "FAST" in line:
                    mode = "FAST"
                if "HAC" in line:
                    mode = "HAC"
                if "SUP" in line:
                    mode = "SUP"
                if "NONE" in line:
                    mode = "NONE"
    prediction = '-'.join([flowcell, software, version, mode])
    
    return [prediction, readqv]




def read_sra_list(filename : str) -> list:
    out_list = list()
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip()
            if temp:
                out_list.append(temp)

    return out_list



def parse_logfile(filename : str) -> dict:
    out_dict = dict()
    with open(filename, 'r') as f:
        for line in f:
            srr = None
            match_fastq = re.search(r'/([^/]+)\.fastq', line)
            if match_fastq:
                srr = match_fastq.group(1)
            stdout = None
            match_stdout = re.search(r"stdout='(.+?)'", line)
            if match_stdout:
                stdout = match_stdout.group(1)
                stdout = stdout[ :-2]
            if srr and stdout:
                out_dict[srr] = stdout
    return out_dict



parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "Input json result directory", required = True, type = str)
parser.add_argument("-s", "--seq", help = "Input sra sequence directory", required = True, type = str)
parser.add_argument("-l", "--list", help = "Input sra list", required = True, type = str)
parser.add_argument("-g", "--log", help = "Stdout of LongBow running", required = True, type = str)
parser.add_argument("-o", "--output", help = "Output csv file", required = True, type = str)


args = parser.parse_args()

json_dir = os.path.abspath(args.input)
seq_dir = os.path.abspath(args.seq)
sra_list = os.path.abspath(args.list)
log_file = os.path.abspath(args.log)
output = os.path.abspath(args.output)

log = parse_logfile(log_file)

subject = read_sra_list(sra_list)

os.chdir(json_dir)

result = []
for i in subject:
    temp = []
    if f"{i}.json" in os.listdir(json_dir):
        m = parse_json(f"{i}.json")
        temp.append(m[0])
        temp.append(m[1])
        temp.append("")
    else:
        temp.append("")
        temp.append("")

        if f"{i}.fastq" not in os.listdir(seq_dir):
            temp.append("DOWNLOAD_FAIL")
        else:
            if i in log:
                temp.append(log[i])
            else:
                temp.append("RUN_FAIL")
    result.append(temp)
    


with open(output, 'w') as f:
    f.write("Sample,Prediction,ReadQV_cufoff,Note\n")
    for idx in range(len(subject)):
        f.write(','.join([subject[idx]] + result[idx]))
        f.write('\n')

    print("Output DONE")



