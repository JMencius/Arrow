import os
import sys
from multiprocessing import Pool
import math
import argparse


def process_chunck(filename : str, coreindex : int) -> tuple:
    global qscore_cutoff
    base_level_result = dict()

    linecount = 1
    with open(filename, 'r') as file:
        for line in file:
            if (linecount % 4) == 0:
                if (linecount // 4) % threads == coreindex:
                    # 去掉空格和换行符
                    m = line.strip()
                    read_score_sum = 0
                    count = 0
                    temp_base = dict()
                    for asci in m:
                        count += 1
                        score = ord(asci) - 33
                        temp_base[score] = temp_base.get(score, 0) + 1
                        converted = 10 ** (score/-10)
                        read_score_sum += converted
                        read_score = -10 * math.log(read_score_sum / count, 10)
                        
                    if read_score > qscore_cutoff:    
                        for i in temp_base:
                            base_level_result[i] = base_level_result.get(i, 0) + temp_base[i]
                                
            linecount += 1

    # 使用multiprocessing时使用return直接返回结果
    return base_level_result



def process_dict(in_dict : dict) -> list:
    a = list(in_dict.items())
    a.sort(key = lambda K : K[0])
    all_sum = sum(i[1] for i in a)
    return([i[1] / all_sum for i in a])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Path to the input fastq file, including the fastq file name", required = True, type = str)
    parser.add_argument("-o", "--output", help = "Output directory or tsv file name", required = True, type = str)
    parser.add_argument("-q", "--qscore", help = "qscore cutoff [DEFAULT:not cutoff]", default = -1, type = int)
    parser.add_argument("-t", "--threads", help = "Number of threads", default = 12, type = int)


    # print version info
    if "--version" in sys.argv[1 : ] or "-v" in sys.argv[1 : ]:
        print(f"Faster count Q score based on Python 3.7+")
        sys.exit(0)
    
    args = parser.parse_args()
    qscore_cutoff = int(args.qscore)
    threads = args.threads
    fastqfile = str(args.input)
    outputfile = str(args.output)

    
    with Pool(threads) as p:
        output = p.starmap(process_chunck, [(fastqfile, coreindex) for coreindex in range(threads)])

    final_base_level = {i : 0 for i in range(0, 94)}
    for i in output:
        for k in i:
            final_base_level[k] += i[k]

    sorted_base_list = process_dict(final_base_level)

    
    with open(outputfile, 'w') as f:
        f.write(','.join(['Q' + str(i) for i in range(0, 94)]))
        f.write('\n')
        f.write(','.join([str(i) for i in sorted_base_list]))




