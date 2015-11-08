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
shellinput1 = str(sys.argv[1])
shellinput2 = str(sys.argv[2])
inputfile1 = open (shellinput1, 'r')
inputfile2 = open (shellinput2, 'r')
#shelloutput = raw_input('Please type your output file name for over100\n')
#shelloutput =str(sys.argv[2])
#maxsize = input('please type the AA length cutoff \n')
#maxsizenumber = str(maxsize)
#shelloutput = str( 'over' + maxsizenumber + '.txt')
shelloutput = str(sys.argv[3])
#oversizelimit = open (shelloutput,'w')
outputfile = open (shelloutput,'w')
#import temfile

def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]


entireseq = inputfile1.read()
#pdb.set_trace()
for num, x in enumerate(SeqIO.parse(inputfile2,"fasta")):
     if num%1000 == 0:
        print num
     header = x.description
     pro = str(x.seq)
     pro20 = split(pro,20)
     nterm = ''
     for y in pro20:
       
       if y not in entireseq or len(y) < 20:
          nterm = nterm + y
       else:
          break 
     if len(nterm) >= 10:

        result = ">"+header+"\n"+nterm+"\n"
        outputfile.write(result)
    
