	
#Script to find the genotype of the largest INDEL from VCF file.

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
max_len_orig = 0

while(i < len(file_all)):
	line = file_all[i]
	if not line.startswith("#"):
		cur_line = line.split("\t")
		ref_al = cur_line[3] #Extract the reference allele
		alt_al = cur_line[4] #Alternate allele
		max_len = abs(len(ref_al) - len(alt_al)) #Calculate absolute value of difference in length of ref and alt allele
		if(max_len > max_len_orig):
			max_len_orig = max_len
			long_var = cur_line
			var_type = cur_line[9]
			gen_info = var_type.split(",")
			gen_type = gen_info[0].split(":")
	i = i+1
#print(long_var)
print("Genotype of longest indel is", gen_type[0])

# close the file after reading the lines.
file.close()

