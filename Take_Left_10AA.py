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
inputfile1 = open(sys.argv[1],'r')
outputfile = open(sys.argv[2],'w')


for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
#    header = x.description
    seq = str(x.seq)
    result = seq[:11] + '\n'
    outputfile.write(result)
