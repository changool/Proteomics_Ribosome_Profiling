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

for num, x in enumerate(SeqIO.parse(inputfile1,'fasta')):
            header = x.description
            mrnaseq = str(x.seq)

	    if num%200 == 0:
	       print num
	    
	    if len(mrnaseq)%3 == 0:
	       orfcut = mrnaseq
	    elif len(mrnaseq)%3 == 1:
	       orfcut = mrnaseq + "NN"
	    elif len(mrnaseq)%3 == 2:
	       orfcut = mrnaseq + "N"

	    seq_trans1 = str(Seq(orfcut).translate().strip())
	    seq_trans2 = str(Seq(orfcut[1:-2]).translate().strip())
	    seq_trans3 = str(Seq(orfcut[2:-1]).translate().strip())
	    combined_seq_trans = seq_trans1 + '*' + seq_trans2 + '*' + seq_trans3
	    seq_split = combined_seq_trans.split("*")
	    longestorf = max(seq_split,key=len)
	    if len(longestorf) >= 6: # Take peptides longer than 6 aa 
	       result = '>' + header + '\n' + longestorf + "\n"
	       outputfile.write(result)

