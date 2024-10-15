import os
import sys
from multiprocessing import Pool
import math
import pyfastx 
import numpy as np
from statsmodels.tsa.stattools import acf
import argparse



def process_chunck(filename : str, coreindex : int, threads : int) -> list:
    itemcount = 1
    prophet = {chr(i + 33) : i for i in range(0, 94)}
    prophet_score = {chr(i + 33) : 10**(i / -10) for i in range(0, 94)}
    # [readqv_count + baseqv + autocorrelation]
    readqv_split = [[0] + [0 for j in range(0, 94)] + [[0, 0] for k in range(100)] for i in range(93)]

    for name, seq, qual in pyfastx.Fastq(filename, build_index = False):
        if itemcount % threads == coreindex:
            m = qual.strip()
            read_score_sum = 0
            count = 0
            temp_base = dict()
            base_qv = list()
            for asci in m:
                count += 1
                score = prophet[asci]
                read_score_sum += prophet_score[asci]
                base_qv.append(score)
                temp_base[score] = temp_base.get(score, 0) + 1

                    
            read_score = -10 * math.log(read_score_sum / count, 10)    
            read_qv = int(read_score)
            # add readqv to readqv column
            if read_qv >= 1:
                subject = readqv_split[read_qv - 1]
                #print(subject[0])
                #print(type(subject[0]))
                subject[0] += 1
            
                # add baseqv to baseqv columns
                for t in temp_base:
                    if 0 <= t <= 93:
                        subject[t + 1] += temp_base[t]
            
                # calculation autocorrelation
                max_lag = 100
                if count > max_lag:
                    base_qv = np.array(base_qv)
                    autocor_value = acf(base_qv, nlags = max_lag)[1 : ]

                    # add autocorrelation to autocorrelation columns
                    for i in range(max_lag):
                        subject[i + 95][0] += autocor_value[i] * (count - i - 1)
                        subject[i + 95][1] += (count - i - 1)
                                
        itemcount += 1

    return readqv_split



def combine_result(inlist : list) -> dict:
    combined = [[0] + [0 for j in range(0, 94)] + [[0, 0] for k in range(100)] for i in range(93)]
    for sfile in inlist:
        for l in sfile:
            for readqv in range(93):
                for i in range(95):
                    combined[readqv][i] += l[readqv][i]
                for i in range(95, 195):
                    combined[readqv][i][0] += l[readqv][i][0]
                    combined[readqv][i][1] += l[readqv][i][1]
    return combined



def write_csv(output_list : list, output : str) -> None:
    cleaned_list = list()
    # clean output list to str and combine str
    for l in output_list:
        temp = list()
        for i in range(95):
            temp.append(str(l[i]))
        for i in range(95, 195):
            temp.append(str(l[i][0]) + '|' + str(l[i][1]))
        cleaned_list.append(temp)


    with open(output, 'w') as f:
        f.write(','.join(["readqv", "count"] + ['Q' + str(i) for i in range(0, 94)] + ['A' + str(i) for i in range(1, 101)]) + '\n')
        readqv = 1
        for l in cleaned_list:
            f.write(f"{readqv},")
            f.write(','.join(l))
            f.write('\n')
            readqv += 1
        global fastqs
        print(f"Output model for {fastqs} successful!")



if __name__ == "__main__":
    version = ('1', '0')
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--passfile", help = "Fastq file of pass/all", required = True, type = str)
    parser.add_argument("-f", "--failfile", help = "Fastq file of fail", default = "", type = str)
    parser.add_argument("-t", "--threads", help = "Number of parallel threads", default = 24, type = int)
    parser.add_argument("-o", "--output", help = "Output model csv name", default = "", type = str)
    parser.add_argument("-v", "--version", help = "Print software version info", action = "store_true")

    # print version info
    if "--version" in sys.argv[1 : ] or "-v" in sys.argv[1 : ]:
        print(f"Get property for LongBow training set version {'.'.join(version)} based on Python 3.7+")
        sys.exit(0)
    
    args = parser.parse_args()
    threads = args.threads
    output_name = os.path.abspath(args.output)
    if args.failfile:
        fastqs = [os.path.abspath(args.passfile), os.path.abspath(args.failfile)]
    else:
        fastqs = [os.path.abspath(args.passfile)]
    
    result = list()
    for fastqfile in fastqs:
        with Pool(threads) as p:
            output = p.starmap(process_chunck, [(fastqfile, coreindex, threads) for coreindex in range(threads)])
            result.append(output)
    
    # combine results from all threads
    combined = combine_result(result)
    
    # output to csv
    write_csv(combined, output_name)

















    

