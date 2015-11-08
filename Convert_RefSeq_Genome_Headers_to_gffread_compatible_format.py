#!/usr/bin/python
import sys
from Bio import SeqIO


# python *.py [gene2accession] [InPutmRNAAcce] [Outputfile]

inputfile1 = open (sys.argv[1], 'r')
outputfile = open (sys.argv[2], 'w')

for num, z in enumerate(SeqIO.parse(inputfile1,'fasta')): # Input file
     if num%1000 == 0:
        print num
     hd = z.id
     seq = str(z.seq)
     hd_ls = hd.split('|')
     acc = hd_ls[3]
     outputfile.write('>'+acc+'\n'+seq+'\n')