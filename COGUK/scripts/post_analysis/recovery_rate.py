import os

def read_txt(filename: str) -> list:
    outlist = list()
    with open(filename, 'r') as f:
        for line in f:
            m = line.split(',')
            outlist.append(m[0])

    return outlist



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

def find_interesting(inlist: list, ontc: set, ngsc: set, longbow: set, artex: set, err_id: str) -> dict:
    a = dict()
    for i in inlist:
        if i in ngsc:
            a[i] = [1, 0, 0]
            if i in longbow: 
                a[i][1] += 1
            if i in artex:
                a[i][2] += 1

    return a


def extract_digit(instr: str) -> int:
    digit = ""
    for i in instr:
        if i.isdigit():
            digit = digit + i
    return int(digit)


if __name__ == "__main__":
    err_list = read_err_list("../err_id.txt")
    in_list = read_txt("extra_varaint.txt")
    count = 0
    s = dict()
    for i in err_list:
        ontc = parse_vcf(f"../../data/ont_consensus/{i}/{i}_ont.vcf")
        ngsc = parse_vcf(f"../../data/ngs_consensus/{i}/{i}_ngs.vcf")
        longbow = parse_vcf(f"../../results/{i}/longbow/{i}_longbow_bcftools.vcf")
        artex = parse_vcf(f"../../results/{i}/artex/{i}_artex_cleaned_consensus.vcf")
        
        a = find_interesting(in_list, ontc, ngsc, longbow, artex, i)
        for i in a:
            if i not in s:
                s[i] = a[i]
            else:
                s[i][0] += a[i][0]
                s[i][1] += a[i][1]
                s[i][2] += a[i][2]

    # output to file
    linecount = 0
    with open("extra_varaint.txt", 'r') as f:
        with open("extra_variant_with_recovery.txt", 'w') as g:
            g.write("Extra variant,count,recover_rate_artic,recovery_rate_artex,recovery_count_artic,recover_count_artex,total_count\n")
            for line in f:
                if linecount == 0:
                    linecount += 1
                    continue
                m = (line.strip()).split(',')

                g.write(f"{m[0]},{m[1]},{s[m[0]][1] / s[m[0]][0]},{s[m[0]][2] / s[m[0]][0]},{s[m[0]][1]},{s[m[0]][2]},{s[m[0]][0]}\n")



    print("ALL DONE")
               











