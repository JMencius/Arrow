import os
import sys
from multiprocessing import Pool
import math
import argparse
import numpy as np
from statsmodels.tsa.stattools import acf
import pyfastx


def process_chunck(filename : str, coreindex : int) -> dict:
    global qscore_cutoff
    
    lags = range(1, 101)
    autocorr_summary = {i : [0, 0] for i in lags}

    itemcount = 1
    for name, seq, qual in pyfastx.Fastq(filename, build_index = False):
        if True:
                if itemcount % threads == coreindex:
                    # 去掉空格和换行符
                    m = qual
                    read_score_sum = 0
                    count = 0
                    base_qv = list()
                    for asci in m:
                        count += 1
                        score = ord(asci) - 33
                        base_qv.append(score)
                        converted = 10 ** (score/-10)
                        read_score_sum += converted
                    
                    read_score = -10 * math.log(read_score_sum / count, 10)
                        
                    if read_score > qscore_cutoff:
                        max_lag = 100
                        if count > max_lag:
                            base_qv = np.array(base_qv)

                            autocor_value = acf(base_qv, nlags = 100)[1 : ]
                        
                            for i in range(max_lag):
                                autocorr_summary[i + 1][0] += autocor_value[i] * (count - i - 1)
                                autocorr_summary[i + 1][1] += (count - i - 1)
                            # print(autocor_value[0], count - i - 1, linecount)
        itemcount += 1

    return autocorr_summary



def process_dict(in_dict : dict) -> list:
    a = list(in_dict.items())
    a.sort(key = lambda K : K[0])
    return([i[1][0] / i[1][1] for i in a])



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Path to the input fastq file, including the fastq file name", required = True, type = str)
    parser.add_argument("-o", "--output", help = "Output directory and csv or txt output filename", required = True, type = str)
    parser.add_argument("-q", "--qscore", help = "qscore cutoff [DEFAULT : 0]", default = 0, type = int)
    parser.add_argument("-t", "--threads", help = "Number of threads [DEFAULT : 12]", default = 12, type = int)
    
    args = parser.parse_args()
    qscore_cutoff = int(args.qscore)
    threads = args.threads
    fastqfile = os.path.abspath(str(args.input))
    outputfile = os.path.abspath(str(args.output))

    
    with Pool(threads) as p:
        output = p.starmap(process_chunck, [(fastqfile, coreindex) for coreindex in range(threads)])
    
    # print(output)
    final_corr = {i : [0, 0] for i in range(1, 101)}
    for i in output:
        for k in i:
            final_corr[k][1] += i[k][1]
            final_corr[k][0] += i[k][0]

    sorted_corr_list = process_dict(final_corr)

    
    with open(outputfile, 'w') as f:
	    f.write(','.join(['A' + str(i) for i in range(1, 101)]))
	    f.write('\n')
	    f.write(','.join([str(i) for i in sorted_corr_list]))
    
