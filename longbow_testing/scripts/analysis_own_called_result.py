import argparse
import os


def parse_json(json_file : str) -> tuple:
    m = json_file.split('.')[0]
    sample, truth = m.split('_')
    with open(json_file) as f:
        flowcell = ""
        software = ""
        version = ""
        mode = ""
        for line in f:
            if "Flowcell" in line:
                if "R9" in line:
                    flowcell = "R9"
                else:
                    flowcell = "R10"
            if "Software" in line:
                if "guppy" in line:
                    software = 'G'
                else:
                    software = 'D'
            if "Version" in line:
                if "2" in line:
                    version = '2'
                if "3or4" in line:
                    version = '4'
                if "5or6" in line:
                    version = '6'
                if '0' in line:
                    version = '0'
            if "Mode" in line:
                if "FAST" in line:
                    mode = "FAST"
                if "HAC" in line:
                    mode = "HAC"
                if "SUP" in line:
                    mode = "SUP"
    prediction = flowcell + software + version + mode
    
    return (sample, truth, prediction)



parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "Input json directory", required = True, type = str)
parser.add_argument("-o", "--output", help = "Output csv file", required = True, type = str)

args = parser.parse_args()

json_dir = os.path.abspath(args.input)
output = os.path.abspath(args.output)

os.chdir(json_dir)

results = []
for file in os.listdir(json_dir):
    temp = parse_json(file)
    results.append(temp)

print(len(results))
print(json_dir)
print(output)


group_count = 66
align = ("R10D0FAST", "R10D0HAC", "R10D0SUP", "R10G6FAST", "R10G6HAC", "R10G6SUP",
         "R9D0FAST", "R9D0HAC", "R9D0SUP", "R9G2", "R9G4FAST", "R9G4HAC", "R9G6FAST", "R9G6HAC", "R9G6SUP")

with open(output, 'w') as f:
    f.write('Sample,Truth,Prediction,Comment\n')
    for i in range(1, group_count + 1):
        for group in align:
            for r in results:
                if r[0] == f"sample{i}" and r[1] == group:
                    if r[1] == r[2]:
                        f.write(f"{r[0]},{r[1]},{r[2]},correct\n")
                    else:
                        f.write(f"{r[0]},{r[1]},{r[2]},wrong\n")

    print("Output DONE")



