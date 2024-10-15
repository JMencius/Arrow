import os
import sys


in_csv = os.path.abspath(sys.argv[1])

out_download_txt = os.path.abspath(sys.argv[2])


g = open(out_download_txt, 'w')

linecount = 0
with open(in_csv, 'r') as c:
	for line in c:
		# skip header
		if linecount == 0:
			linecount += 1
			continue
		m = (line.strip()).split(',')
		g.write(m[1] + ' ' + m[2] + ' ' + m[5] + ' ' + m[6] + '\n')
		linecount += 1


g.close()
print("ALL DONE")


