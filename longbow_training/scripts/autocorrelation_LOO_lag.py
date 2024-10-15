# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:47:52 2023

@author: Mencius
"""
import argparse
import os
import sys
import math



def read_model_autocorr(filename : str, encoding='utf-8') -> list:
    linecount = 0
    output = [[0, 0] for i in range(100)]
    with open(filename, 'r') as f:
        for line in f:
            if linecount == 0:
                linecount += 1   
                continue
            
            m = line.split(',')
            if len(m) == 192:
                for i in range(100):
                    temp = m[i + 92].split('|')
                    if temp[0] != 'nan':
                        output[i][0] += float(temp[0])
                        output[i][1] += int(temp[1])
    
    # normalize to percentage
    output = [i[0] / i[1] for i in output]
    
    return output



def cal_euclidean_distance(autocorr1 : list, autocorr2 : list) -> float:
    assert len(autocorr1) == len(autocorr2)
    return math.sqrt(sum([(autocorr1[i] - autocorr2[i])**2 for i in range(len(autocorr1))])) 



# the exact predict hac sup function from longbow code
def predict_hac_sup(subject : list, train_x, train_y, trim_lag : int, k = 3) -> int:
    edistance_list = list()
    for i in range(len(train_x)):
        clean_train_x = [float(j) for j in train_x[i]][: trim_lag]
        subject = subject[: trim_lag]
        dist = cal_euclidean_distance(subject, clean_train_x)
        edistance_list.append((list(train_y)[i], dist))

    edistance_list.sort(key = lambda s : s[1])
    top_k = edistance_list[ : k]
    label_k = [i[0] for i in top_k]
    # print(edistance_list)

    if len(set(label_k)) == len(label_k):
        return label_k[0]
    else:
        max_count_label = None
        max_count = 0
        for i in set(label_k):
            if label_k.count(i) > max_count:
                max_count = label_k.count(i)
                max_count_label = i
        return max_count_label




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Input model file path", required = True, type = str)
    parser.add_argument("-o", "--output", help = "Output txt filename", required = True, type = str)
    parser.add_argument("-s", "--subject", help = "Subject group for autocorrelation lag LOO test, must be within [R9G4, R9G6, R9D0, R10G6, R10D0]", required = True, type = str)
    
    args = parser.parse_args()
    model_path = os.path.abspath(args.input)
    output = os.path.abspath(args.output)
    subject = args.subject

    if subject not in ("R9G4", "R9G6", "R9D0", "R10G6", "R10D0"):
        print(f"-s, --subject must choose within R9G4, R9G6, R9D0, R10G6, R10D0")
        sys.exit(1)
    
    if subject == "R9G4":
        groups = ["R9G4FAST", "R9G4HAC"]
        label = {"R9G4FAST" : 0, "R9G4HAC" : 1}
    elif subject == "R9G6":
        groups = ["R9G6FAST", "R9G6HAC", "R9G6SUP"]
        label = {"R9G6FAST" : 0, "R9G6HAC" : 1, "R9G6SUP" : 2}
    elif subject == "R9D0":
        groups = ["R9D0FAST", "R9D0HAC", "R9D0SUP"]
        label = {"R9D0FAST" : 0, "R9D0HAC" : 1, "R9D0SUP" : 2}
    elif subject == "R10G6":
        groups = ["R10G6FAST", "R10G6HAC", "R10G6SUP"]
        label = {"R10G6FAST" : 0, "R10G6HAC" : 1, "R10G6SUP" : 2}
    elif subject == "R10D0":
        groups = ["R10D0FAST", "R10D0HAC", "R10D0SUP"]
        label = {"R10D0FAST" : 0, "R10D0HAC" : 1, "R10D0SUP" : 2}


    os.chdir(model_path)

    train_X = []
    train_Y = []
    # read model file
    for file in os.listdir():
        if ".csv" in file:
            for tag in groups:
                if tag in file:
                    train_X.append(read_model_autocorr(file))
                    train_Y.append(label[tag])
    

    accuracy_storage = list()
    for lag in range(1, 101):
        correct_times = 0
        trail_times = 0
        for leave_idx in range(len(train_X)):
            mod_train_X = train_X[:leave_idx] + train_X[leave_idx + 1:]
            mod_train_Y = train_Y[:leave_idx] + train_Y[leave_idx + 1:]
            pred = predict_hac_sup(train_X[leave_idx], mod_train_X, mod_train_Y, lag)
            #print(pred, leave_idx)
            if pred == train_Y[leave_idx]:
                correct_times += 1
            trail_times += 1
        accuracy_storage.append(correct_times / trail_times)
        # print(f"lag : {lag}  Accuracy : {correct_times / trail_times}")

    with open(output, 'w') as f:
        f.write("Lag" + '\t' + "Accuracy" + '\n')
        for i in range(len(accuracy_storage)):
            f.write(f"{i + 1}" + '\t' + f"{accuracy_storage[i]}" + '\n')

        print("LOO compeleted")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
