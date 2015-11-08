#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq

inputfile1 = open (sys.argv[1], 'r')
outputfile = open (sys.argv[2], 'w')


for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")):
    acc = x.id
    rnaseq = str(x.seq)
    length = len(rnaseq)
    outputfile.write(acc+'\t'+str(length)+'\n')
