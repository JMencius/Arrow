# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:59:58 2023

@author: Mencius
"""

from faster_get_qscore import get_qscore
import math
import os
import sys
import argparse
import time
from dictances import bhattacharyya



def cal_bhattacharyya_coefficient(distri1 : dict, distri2 : dict) -> float:

    bhattacharyya_coefficient = math.e ** (-1 * bhattacharyya(distri1, distri2))
    return bhattacharyya_coefficient


def normalize(in_list : list) -> list:
    s = sum(in_list)
    assert s != 0, "Q score list sum is 0."
    normalized_list = [i/s for i in in_list]
    return normalized_list



if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--ref", help = "Reference fastq for input", required = True, type = str)
    parser.add_argument("-q", "--query", help = "Query fastq for input", required = True, type = str)
    parser.add_argument("-t", "--threads", help = "Number of parallel threads", default = 12, type = int)

    args = parser.parse_args()
    ref = os.path.abspath(args.ref)
    query = os.path.abspath(args.query)
    threads = int(args.threads)

    ref_qscore = (get_qscore(ref, threads, 0, False))[0]
    query_qscore = (get_qscore(query, threads, 0, False))[0]
    
    norm_ref = normalize(ref_qscore)
    ref_dict = {(i + 1) : norm_ref[i] for i in range(90)}
    norm_query = normalize(query_qscore)
    query_dict = {(i + 1) : norm_query[i] for i in range(90)}

    print(f"Bhattachaya similarity between {ref} and {query} is {cal_bhattacharyya_coefficient(ref_dict, query_dict)}")


    end_time = time.time()
    # print(f"Running time is {end_time - start_time} seconds.")
    

