#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
import re
#import argparse
#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')
#args = parser.parse_args()
#shellinput = raw_input('Please type your input file name!\n')
inputfile1 = open (sys.argv[1], 'r')#gi|peptide sequence
inputfile2 = open (sys.argv[2], 'r')#fasta file for protein sequence
outputfile = open (sys.argv[3], 'w')

#def split(str, num):
#    return [ str[start:start+num] for start in range(0, len(str), num) ]
dic ={}
for y in SeqIO.parse(inputfile2,"fasta"):
   header = y.description
   pepseq = str(y.seq)
   header_ls = header.split("|")
   gi = header_ls[1].strip()
#   acc = header_ls[3].strip()
   dic[gi] = pepseq

for num, x in enumerate(inputfile1): 
           if num%100 == 0:
              print num

           x_ls = x.strip().split("|")
           gi_x = x_ls[0].strip()
           pep_x = x_ls[1].strip()
           for k,v in dic.iteritems():
              if k == gi_x:
                 peppos = v.find(pep_x)
                 if peppos == 0:
                    pepatm1 = '#'+ v[peppos:peppos + 10]
                    result = pep_x + "|" + pepatm1 + "|" + str(peppos + 1) + '\n'
                 else:
                    pepatm1 = v[peppos -1:peppos + 10]
                    result = pep_x + "|" + pepatm1 + "|" + str(peppos + 1) + '\n'
                 outputfile.write(result)
