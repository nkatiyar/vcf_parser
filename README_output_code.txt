Ouput of scripts for second question.

1. Count the total number of variants, total number of heterozygous and total number of homozygous variants per chromosome.
Output is written in the file vcf_parser1_out.txt

2. Genotype of the largest indel in this sample.
python vcf_parser_part2.py test.vcf 
('Genotype of longest indel is', '0/1')

3. Output variants that are supported only by <15% of the reads.
python vcf_parser_part3.py test.vcf > vcf_parser_part3_out.txt
vcf_parser_part3_out.txt
