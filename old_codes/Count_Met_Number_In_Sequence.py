#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
#import re
#import argparse
#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')
#args = parser.parse_args()
#shellinput = raw_input('Please type your input file name!\n')
shellinput1 = str(sys.argv[1])
#shellinput2 = str(sys.argv[2])
inputfile1 = open(shellinput1,'r')
#inputfile2 = open(shellinput2, 'r')
shelloutput = str(sys.argv[2])
outputfile = open(shelloutput,'w')

i = 0
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
    header = x.description
    seq = str(x.seq)
    seqlen = len(seq)
    nterm = seq[:seqlen - 6]
    m = nterm.count("M")
   
    if m >= 1:
       result = seq + "\n"
       outputfile.write(result)


       i += 1   
    print num
    print i

