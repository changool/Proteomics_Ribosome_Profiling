#!/usr/bin/python
import sys
from Bio import SeqIO

inputfile1 = open (sys.argv[1], 'r')
inputfile2 = open (sys.argv[2], 'r')
outputfile = open (sys.argv[3], 'w')

dic1 = {}
for num1, x in enumerate(SeqIO.parse(inputfile1,"fasta")): # fasta
    header = x.description
    header_ls = header.split("|")
    if len(header_ls) >= 5:
        gi = header_ls[1].strip()
        des = header_ls[4].strip()
        dic1[gi] = des

for num3, z in enumerate(inputfile2): # Input file
     if num3%1000 == 0:
        print num3
     z_ls = z.split('.')
     inputinfo = z_ls[0].strip()
     outputfile.write(inputinfo)
     v1 = dic1.get(inputinfo)
     if v1 != None:
           result = '\t' + v1
           outputfile.write(result)
         
     outputfile.write("\n")
