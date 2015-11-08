#!/usr/bin/python

import sys
#import pdb
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


inputfile1 = open (sys.argv[1], 'r')
inputfile2 = open (sys.argv[2], 'r')
outputfile = open (sys.argv[3], 'w')

dic = {}
for num, y in enumerate(SeqIO.parse(inputfile1,"fasta")):
     header = y.id
     pro = str(y.seq)
     dic[header] = pro

for num, x in enumerate(inputfile2): # peptide list
     if num%1000 == 0:
        print num
     
     xstrip = x.strip()
     outputfile.write(xstrip)
     for k,v in dic.iteritems():

        if xstrip in v:

           result = "|" + k
           outputfile.write(result)
           break
     newline = "\n"
     outputfile.write(newline)
    
