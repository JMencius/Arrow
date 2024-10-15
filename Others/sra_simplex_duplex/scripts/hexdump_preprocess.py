import os
import sys
import argparse
import time
import subprocess
import threading

need = set([".tar", ".gz", ".tgz", ".zip"])

def preprocess(dirname : str) -> None:
    flag = 0
    for root, dirs, files in os.walk(dirname):
        for file in files:
            prefix, file_extension = os.path.splitext(file)
            if file_extension in need:
                if True:
                    nfile = os.path.join(root, file)
                    out = os.path.join(root, prefix + '.fast5')
                    if file_extension == ".tar":
                        try:
                            command = f"tar -xf {nfile} -O > {out}"
                            subprocess.run(command, shell = True, check=True)
                            flag = 1
                        except:
                            pass

                    elif file_extension == ".tar":
                        try:
                            command = f"tar -zxf {nfile} -O > {out}"
                            subprocess.run(command, shell = True, check = True)
                            flag = 1
                        except:
                            pass


                    elif file_extension == ".gz":
                        try:
                            command = f'gzip -d {nfile} -c > {out}'
                            subprocess.run(command, shell = True, check=True)
                            flag = 1
                        except:
                            pass

                    elif file_extension == ".zip":
                        try:
                            command = f"unzip -p {nfile} > {out}"
                            subprocess.run(command, shell = True, check=True)
                            flag = 1
                        except:
                            pass
    
    if flag == 1:
        print(f"{dirname} completed, decompressed")
    else:
        print(f"{dirname} checked, nothing to do")
    


if __name__ == "__main__":
    start_time = time.time()
    # parse parameter
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--working", help = "Working diretory", required = True, type = str)

    
    args = parser.parse_args()
    work_dir = os.path.abspath(args.working)
    
    
    os.chdir(work_dir)
    for dir in os.listdir(work_dir):
        preprocess(os.path.join(work_dir, dir))


    end_time = time.time()
    print(f"Total download time : {end_time - start_time} seconds")
    

