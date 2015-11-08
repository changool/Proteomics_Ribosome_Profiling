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

shellinput1 = str(sys.argv[1])
shellinput2 = str(sys.argv[2])
inputfile1 = open (shellinput1, 'r')
inputfile2 = open (shellinput2, 'r')
shelloutput = str(sys.argv[3])
outputfile = open (shelloutput,'w')

dic ={}
for y in SeqIO.parse(inputfile1,"fasta"):
   header1 = y.description
   pro1 = str(y.seq)
   dic[header1] = pro1

for num, x in enumerate(SeqIO.parse(inputfile2,"fasta")):
     if num%1000 == 0:
        print num
     header = x.description
     pro = str(x.seq)

     for h,s in dic.iteritems():
       
       if pro in s:
          result = ">" + h + "\n" + s + "\n"
          outputfile.write(result)
#          dic.pop(h,"")
   
