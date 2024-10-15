import argparse
import os
import time
import subprocess


def process_SRA_dir(dirname : str) -> list:
    # find the fast5 file
    store = []
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if len(file) > 5 and file[-6 :] == ".fast5":
                fast5file = os.path.join(root, file)
                store.append(hexdump(fast5file))

    result = ["", "", "", "", "", "", "", ""]
    for i in store:
        for j in range(len(i)):
            if len(i[j]) > len(result[j]):
                result[j] = i[j]
    # if no fast5 found return None
    if result != ["", "", "", "", "", "", "", ""]:
        print(result)
        return result
    else:
        workaround = ["", "", "", "", "", "", "", ",".join(fileformat(dirname))]
        print(workaround)
        return workaround
        

def fileformat(folder : str) -> set:
    extensions = set()
    for root, dirs, files in os.walk(folder):
        for filename in files:
            _, extension = os.path.splitext(filename)
            if extension == "gz":
                if filename.split('.')[-2] == "tar":
                    extensions.add("tar.gz")
                    continue
            extensions.add(extension)
    return extensions



def hexdump(fast5file : str) -> list:
    hexdump_out = subprocess.run(f"hexdump -C {fast5file}", shell = True, capture_output = True, text = True)
    return process_hexdump(hexdump_out.stdout)


def process_hexdump(hexdumptxt : str) -> list:
    # results for experiment_type, flowcell_type, sequencing_kit, time_stamp
    labels2find = ["experiment_type", "flowcell_type", "flow_cell_product_code", "sequencing_kit", "time_stamp", "exp_start_time"]
    result = ["", "", "", "", "", "", "", ""]
    # get the decode result from hexdump
    translate = str()
    # chopp according to line
    m = hexdumptxt.split("\n")
    for line in m:
        element = line.split()
        if len(element) >= 4:
            decode = element[-1]
            if decode[0] == '|' and decode[-1] == '|':
                for j in decode[1 : -1]:
                    if j == '.':
                        translate += ' '
                    else:
                        translate += j

    chopped_translate : list = translate.split()
    for c in range(len(labels2find)):
        label = labels2find[c]
        if label in chopped_translate:
            pos = chopped_translate.index(label)
            
            if pos + 1 < len(chopped_translate):
                result[c] = chopped_translate[pos + 1]
    
    match_year = [str(i) for i in range(2010, 2017)]
    for k in chopped_translate:
        for m in match_year:
            if m in k:
                result[6] = k
                break

        #print(c)
        #print(result)

    return result

def output2txt(result_list : list, outfile : str) -> None:
    with open(outfile, 'w') as f:
        for r in result_list:
            if len(r[1][1]) > len(r[1][2]):
                f.write(str(r[0]) + '\t' + str(r[1][0]) + '\t' + str(r[1][1]) + '\t' + str(r[1][3]) + '\t' + str(r[1][4]) + '\t' + str(r[1][5]) + '\t' + str(r[1][6]) + '\t' + str(r[1][7]) + '\n')
            elif len(r[1][2]) > len(r[1][1]):
                f.write(str(r[0]) + '\t' + str(r[1][0]) + '\t' + str(r[1][2]) + '\t' + str(r[1][3]) + '\t' + str(r[1][4]) + '\t' + str(r[1][5])+ '\t' + str(r[1][6]) + '\t' + str(r[1][7]) + '\n')
            else:
                f.write(str(r[0]) + '\t' + str(r[1][0]) + '\t' + str(r[1][1]) + '\t' + str(r[1][3]) + '\t' + str(r[1][4]) + '\t' + str(r[1][5]) + '\t' + str(r[1][6]) + '\t' + str(r[1][7]) + '\n')
    print("Written to outfile.")



if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Path to the input fast5 folders", required = True, type = str)
    parser.add_argument("-o", "--output", help = "Output tsv file name", required = True, type = str)
    args = parser.parse_args()
    input_dir = os.path.abspath(args.input)
    output_file = os.path.abspath(args.output)
    
    os.chdir(input_dir)
    sub_dir = [entry for entry in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, entry))]
    
    #print(sub_dir[:10])   
    # mask for test
    #sub_dir = ["SRR9821955"]

    results = list()
    finished_count = 0
    for i in sub_dir:
        print(i)
        temp = process_SRA_dir(i)
        #print(results)
        if temp:
            results.append((i, process_SRA_dir(i)))
        
        finished_count += 1
        print(f"{finished_count} / {len(sub_dir)} DONE.")

    output2txt(results, output_file)

    end_time = time.time()
    print(f"Total processing time : {end_time - start_time} seconds")


