import os
import argparse
import time
import subprocess
import threading
from multiprocessing import Pool



def read_list(filename : str) -> list:
    # Read the input txt file and store the links into a list
    linecount = 0
    url_list = list()
    usable_count = 0

    with open(filename, 'r') as f:
        for line in f:
            if linecount == 0:
                linecount += 1
                continue
            m = line.split()
            # Skip if download link does not exist
            if len(m) != 2:
                print("[Warning]Invalid line {linecount} pattern not matched, skipped")
                print(line)
                continue
            
            pick_url = None
            line_usable = 0
            flag = 0
            for i in m[1].split(';'):
                if (".h5" in i) or (".zip" in i) or (".tar" in i) or (".gz" in i) or (".tgz" in i):
                    pick_url = i
                    SRR_index = pick_url.split('/')[-2]
                    url_list.append((SRR_index, pick_url))
                    pick_url = None
                    usable_count += 1
                    line_usable += 1
                    flag = 1
                else:
                    for j in [f".fast5.{c}" for c in range(10)]:
                        if j in i:
                            pick_url = i
                            SRR_index = pick_url.split('/')[-2]
                            url_list.append((SRR_index, pick_url))
                            pick_url = None
                            usable_count += 1
                            line_usable += 1
                            flag = 1
                if flag == 1:
                    break
                            

            
            if line_usable == 0:
                print("[Warning]Invalid line {linecount} no downloadable link, skipped")
                print(line)
                
            linecount += 1
    
    print(f"Data summary : Total : {linecount - 1}, Usable : {usable_count}, ratio : {usable_count / (linecount - 1)}")
    return url_list



def get_compressed_mode(url : str) -> str:
    for i in [f".fast5.{i}" for i in range(10)]:
        if i in url:
            return "fast5"

    if ".h5" in url:
        return "fast5"
    elif "tar.gz" in url:
        return "tar.gz"
    else:
        if ".zip.tar" in url:
            return "ziptar"

        if ".tar" in url:
            return "tar"

        if ".gz" in url:
            return "gz"

        if ".tgz" in url:
            return "tgz"

        if ".zip" in url:
            return "zip"
    
    return None



def partial_download(url : str, target_folder : str) -> int:
    # Partially download to the target_folder
    final_status = 0
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)
        try:
            # Download with subprocess.Popen according to the compress mode
            compress_mode = get_compressed_mode(url)
            if compress_mode == "tar.gz" or compress_mode == "tgz" or compress_mode == "gz":
                with subprocess.Popen(f"curl --range 0-3145728 {url} | tar zxf -", shell = True, cwd = target_folder, text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE) as proc:
                    proc.communicate()
            elif compress_mode == "ziptar":
                with subprocess.Popen(f"curl --range 0-3145728 {url} | tar xf - | unzip -q -", shell = True, cwd = target_folder, text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE) as proc:
                    proc.communicate()
            elif compress_mode == "tar":
                with subprocess.Popen(f"curl --range 0-3145728 {url} | tar xf -", shell = True, cwd = target_folder, text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE) as proc:
                    proc.communicate()
            elif compress_mode == "fast5":
                with subprocess.Popen(f"curl --range 0-3145728 {url} --output {target_folder}.fast5", shell = True, cwd = target_folder, text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE) as proc:
                    proc.communicate()
            elif compress_mode == "zip":
                 with subprocess.Popen(f"curl --range 0-3145728 {url} | unzip -q -", shell = True, cwd = target_folder, text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE) as proc:
                    proc.communicate()

        except Exception as e:
            print(f"An error occurred during download {target_folder}: {e}")

        print(f"Download for {target_folder} completed")
        final_status = 1

    else:
        print("Directory algready exist")
    
    return final_status


if __name__ == "__main__":
    start_time = time.time()
    # parse parameter
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Path to the input txt file", required = True, type = str)
    parser.add_argument("-w", "--working", help = "Working diretory", required = True, type = str)
    parser.add_argument("-t", "--threads", help = "Parallel threads [default : 6]", default = 6, type = int)

    
    args = parser.parse_args()
    input_file = os.path.abspath(args.input)
    work_dir = os.path.abspath(args.working)
    threads = int(args.threads)
    

    # read the download list and target dir
    download_list = read_list(input_file)
    ## print(download_list[:10])

    # change diretory to working dir
    os.chdir(work_dir)

    # Start partial download in working dir
    sucessful_download = 0
    
    # multiprocessing
    with Pool(threads) as p:
        output = p.starmap(partial_download, [(i[1], i[0]) for i in download_list])

    for item in output:
        sucessful_download += item

    print(f"Final Summary : Success download : {sucessful_download} of total : {len(download_list)}")
    end_time = time.time()
    print(f"Total download time : {end_time - start_time} seconds")
    

