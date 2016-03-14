#!/usr/bin/python
import sys
from Bio import SeqIO

inputfile1 = open (sys.argv[1], 'r')#fasta file
inputfile2 = open (sys.argv[2], 'r')#input file
outputfile = open (sys.argv[3], 'w')

ls1 = []
for x in SeqIO.parse(inputfile1,'fasta'): # fasta file
     seq = str(x.seq)
     ls1.append(seq)
conc_ls1 = '#'.join(ls1)
for n, pep in enumerate(inputfile2): # Input file
     if n%1000 == 0:
        print n
     if pep.strip() in conc_ls1:
         outputfile.write(pep.strip() +'\t' +'match to db' + '\n')
     else:
         outputfile.write(pep.strip() + '\n')