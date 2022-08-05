	
#Script to output variants that are supported only by <15% of the reads.

import os, sys, re
try:
	fn = sys.argv[1]
except IndexError as ie:
    raise SystemError("Error: Specify file name\n")

if not os.path.exists(fn):
    raise SystemError("Error: File does not exist\n")

read_depth=0

file = open(fn, "r")
file_all = file.readlines()
i=0

while(i < len(file_all)):
	line = file_all[i]

	if not line.startswith("#"):
		cur_line = line.split("\t")
		dp = cur_line[7]
		dp_val = re.findall(r'DP=(\d+)', dp)
		#print(dp_val)
		read_depth = read_depth + int(dp_val[0])
	i = i+1

#Calculate 15 percent of total reads.
read_lim = (float(read_depth) * 15/100)
i=0
cnt = 0

while(i < len(file_all)):
	line = file_all[i]
	if not line.startswith("#"):
		cur_line = line.split("\t")
		dp = cur_line[7]
		dp_val = re.findall(r'DP=(\d+)', dp)
		if(float(dp_val[0]) < read_lim):
			print(line)
			cnt = cnt +1
	i = i+1

# close the file after reading the lines.
file.close()

