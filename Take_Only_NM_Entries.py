#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq

inputfile1 = open (sys.argv[1], 'r')
outputfile = open (sys.argv[2], 'w')


for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")):
    header = x.description
    rnaseq = str(x.seq)
    if "NR_" in header:
        outputfile.write(">"+header+'\n'+rnaseq+'\n')
