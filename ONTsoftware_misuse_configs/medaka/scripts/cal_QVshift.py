import os
import argparse


def txt2QV(filename : str) -> float:
    with open(filename, 'r') as f:
        for line in f:
            m = line.split()
            if len(m) == 3:
                if m[0] == "QV":
                    return float(m[2])




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--draft", help = "Flye draft directory", required = True, type = str)
    parser.add_argument("-p", "--polish", help = "Medaka polished directory", required = True, type = str)
    parser.add_argument("-o", "--output", help = "Output csv file", required = True, type = str)

    args = parser.parse_args()
    draft = os.path.abspath(args.draft)
    polish = os.path.abspath(args.polish)
    output = os.path.abspath(args.output)

    # get draft QV
    draftQV = dict()
    os.chdir(draft)
    for dir in os.listdir():
        subject = os.path.join(dir, "yak.txt")
        draftQV[dir] = txt2QV(subject)
    print(draftQV)


    # get polished QV
    polishedQV = dict()
    os.chdir(polish)
    for dir in os.listdir():
        if dir not in polishedQV:
            polishedQV[dir] = dict()
        os.chdir(os.path.join(polish, dir))
        for secdir in os.listdir():
            if os.path.isdir(secdir) and '_' in secdir:
                subject = os.path.join(secdir, f"{secdir}.yak.txt")
                polishedQV[dir][secdir] = txt2QV(subject)

    print(polishedQV)

    # write to output
    groups = ["R9G4FAST", "R9G4HAC", "R9G6FAST", "R9G6HAC", "R9G6SUP", "R10D0HAC", "R10D0SUP"]
    with open(output, 'w') as f:
        f.write("basecalled,polished config,draft QV,polished QV,QV shift\n")
        for i in groups:
            for t in groups:
                for j in polishedQV[i]:
                    config = j.split('_')[-1]
                    if t == config:
                        f.write(f"{i},{config},{draftQV[i]},{polishedQV[i][j]},{polishedQV[i][j] - draftQV[i]}\n")

        print("Outout completed, ALL DONE")










