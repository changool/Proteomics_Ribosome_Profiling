#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
#import pdb
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
#import argparse

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

#shellinput = raw_input('Please type your input file name!\n')
inputfile1 = open (sys.argv[1], 'r')
inputfile2 = open (sys.argv[2], 'r')
outputfile = open (sys.argv[3], 'w')
#import temfile



entireseq = inputfile1.read() # RefSeq database

#for num, x in enumerate(SeqIO.parse(inputfile2,"fasta")):

for num, x in enumerate(inputfile2): # Peptide Sequence list
     x_up = x.upper()
     if num%1000 == 0:
        print num
     result1 = x_up.strip() + "|"
     outputfile.write(result1)    
 
     if x.strip() in entireseq:
        result2 = "Overlap with RefSeq"
        outputfile.write(result2)
     newline = "\n"
     outputfile.write(newline)
