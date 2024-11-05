import os


def read_err_list(filename: str) -> list:
    err_list = list()
    with open(filename, 'r') as f:
        for line in f:
            m = line.strip()
            if m:
                err_list.append(m)

    return err_list



def parse_vcf(filename: str) -> set:
    mutants = set()
    filename = os.path.abspath(filename)
    with open(filename, 'r') as f:
        for line in f:
            # skip empty line and annotation line
            if line and line[0] != '#':
                m = line.split()

                if len(m) >= 8:
                    mutation = m[3] + m[1] + m[4]
                    mutants.add(mutation)

    return mutants

def find_interesting(ontc: set, ngsc: set, longbow: set, artex: set, err_id: str) -> None:
    a = set()
    for i in ngsc:
        if i not in longbow:
            if i in artex:
                a.add(i)
                print(i, err_id)

    return a


def extract_digit(instr: str) -> int:
    digit = ""
    for i in instr:
        if i.isdigit():
            digit = digit + i
    return int(digit)


if __name__ == "__main__":
    err_list = read_err_list("../err_id.txt")
    count = 0
    s = dict()
    for i in err_list:
        ontc = parse_vcf(f"../../data/ont_consensus/{i}/{i}_ont.vcf")
        ngsc = parse_vcf(f"../../data/ngs_consensus/{i}/{i}_ngs.vcf")
        longbow = parse_vcf(f"../../results/{i}/longbow/{i}_longbow_consensus.vcf")
        artex = parse_vcf(f"../../results/{i}/artex/{i}_artex_cleaned_consensus.vcf")
        
        a = find_interesting(ontc, ngsc, longbow, artex, i)
        for i in a:
            s[i] = s.get(i, 0) + 1

    s_list = list(s.items())
    s_list.sort(key = lambda K : extract_digit(K[0]))
    print(s_list)
    print('\n')
    with open("extra_varaint.txt", 'w') as f:
        f.write("Extra variant,count\n")
        for i in s_list:
            f.write(f"{i[0]},{i[1]}\n")

    print("ALL DONE")














