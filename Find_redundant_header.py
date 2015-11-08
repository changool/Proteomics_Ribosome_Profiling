#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

inputfile1 = open (sys.argv[1], 'r')
outputfile = open (sys.argv[2], 'w')

ls = []
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")):
    header = x.description
    pro = str(x.seq)
    ls.append(header+"#"+pro)
    
for num1, y in enumerate(ls):
    if num1%1000 == 0:print num1
    a = ls.count(y)
    if a > 1:
        outputfile.write(y+'\n')

