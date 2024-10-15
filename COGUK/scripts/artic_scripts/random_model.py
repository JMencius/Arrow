import random
import sys
import os

ERR_list = os.path.abspath(sys.argv[1])
output_txt = os.path.abspath(sys.argv[2])


ERR_id = list()
print("Parsing txt file")
with open(ERR_list, 'r') as f:
    for line in f:
        m = line.strip()
        if m:
            ERR_id.append(m)

count = len(ERR_id)


random.seed(100)

print("generating random seeds")
random_numbers = random.sample(range(1001), count)
## print(random_numbers)

medaka_parameters = ["r941_min_fast_g303", 
                     "r941_min_high_g360",
                     "r941_min_fast_g507",
                     "r941_min_hac_g507",
                     "r941_min_sup_g507",
                     "r1041_e82_400bps_fast_g632",
                     "r1041_e82_400bps_hac_g632",
                     "r1041_e82_400bps_sup_g615",
                     "r1041_e82_400bps_hac_v4.3.0",
                     "r1041_e82_400bps_sup_v4.3.0"]

record = list()
print("generating random models")
for s in random_numbers:
    random.seed(s)
    choice = random.choice(medaka_parameters)
    record.append(choice)

print("Output to txt file")
with open(output_txt, 'w') as g:
    for i in range(count):
        g.write(f"{ERR_id[i]} {random_numbers[i]} {record[i]}\n")

print("Output complete, ALL DONE")




