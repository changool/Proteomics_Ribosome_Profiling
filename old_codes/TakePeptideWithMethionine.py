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


for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
    header = x.description
    mrnaseq = str(x.seq).strip()
    for num1, char in enumerate(mrnaseq):
       if char == char.upper():
          upperpos = num1
          break
    utr = mrnaseq[:upperpos]
    if num%200 == 0:
       print num
    
    if len(utr)%3 == 0:
       utrcut = utr
    elif len(utr)%3 == 1:
       utrcut = utr[1:]
    elif len(utr)%3 == 2:
       utrcut = utr[2:]
    
    seq_trans = str(Seq(utrcut).translate().strip())
    seq_split = seq_trans.split("*")
    
    lastuorf = seq_split[len(seq_split) -1]
    result = ">" + "last_uORF" + "|" + header + "\n" + lastuorf + "\n"
    outputfile.write(result)
