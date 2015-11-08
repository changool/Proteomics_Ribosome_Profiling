#!/usr/bin/python
import sys
from Bio import SeqIO
import re

inputfile1 = open (sys.argv[1], 'r') # input db

print 'Counting number of lines for input file'
num_lines = sum(1 for line in SeqIO.parse(inputfile1,'fasta'))#for fasta DB
#num_lines = sum(1 for line in inputfile1)#Other files
print num_lines


