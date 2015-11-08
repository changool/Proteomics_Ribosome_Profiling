#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

inputfile1 = open (sys.argv[1], 'r')
outputfile = open (sys.argv[2], 'w')

dic = {}
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")):
     header = x.description
     pro = str(x.seq)
     dic[header] = pro
i = 0
for k,v in dic.iteritems():
     if i % 1000 == 0:
         print i
     outputfile.write('>' + k + '\n' + v + '\n')
     i += 1
   
