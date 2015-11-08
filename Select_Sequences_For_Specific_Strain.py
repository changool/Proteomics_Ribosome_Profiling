#!/usr/bin/python
import sys
from Bio import SeqIO
import progress_counter
import re

inputfile1 = open (sys.argv[1], 'r') # input db
outputfile = open (sys.argv[2], 'w') # output db

for num1, x in enumerate(SeqIO.parse(inputfile1,"fasta")): # RefSeq fasta
    progress_counter.progress(inputfile1,num1,"fasta") # inputfile name, line number, fasta or nonfasta
    header = x.description
    seq = str(x.seq)
    strain = re.findall("\[(.*)\]",header)
    if "Saccharomyces cerevisiae" in strain[0]: # Define strain name
        outputfile.write('>' + header + "\n" + seq + "\n")




