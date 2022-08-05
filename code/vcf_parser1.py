	
#Script to calculate total number of variants, total number of heterozygous and total number of homozygous variants per chromosome.

import os, sys, re
try:
	fn = sys.argv[1]
except IndexError as ie:
    raise SystemError("Error: Specify file name\n")

if not os.path.exists(fn):
    raise SystemError("Error: File does not exist\n")

het_cnt=0
homo_cnt=0

file = open(fn, "r")
file_all = file.readlines()
i=0

while(i < len(file_all)):
	line = file_all[i]
	if(i==(len(file_all)-1)):
		break
	else:
		line1 = file_all[i+1]

		if not line.startswith("#"):
			cur_line = line.split("\t")
			chrom = cur_line[0]
			next_line = line1.split("\t")
			chrom1 = next_line[0]
			var_type = cur_line[9]
			gen_info = var_type.split(",")
			gen_type = gen_info[0].split(":")
			dp = cur_line[7]
			dp_val = re.findall(r'DP=(\d+)', dp)
			#Checking for zygosity
			if(gen_type[0] == "1/1"):
				var_type = "Homozygous"
				homo_cnt = homo_cnt + 1
			else:
				var_type = "Heterozygous"
				het_cnt = het_cnt + 1

			if(chrom != chrom1):
				print("Heterozygous variants for chromosome ", chrom, "=", het_cnt)
				print("Homozygous variants for chromosome ", chrom, "=", homo_cnt)
				total_cnt = het_cnt + homo_cnt
				print("Total variants for chromosome ", chrom, "=", total_cnt)
				het_cnt=0
				homo_cnt=0
	i = i+1

# close the file after reading the lines.
file.close()

