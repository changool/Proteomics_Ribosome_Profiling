#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
#import argparse

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

#shellinput = raw_input('Please type your input file name!\n')
shellinput1 = str(sys.argv[1])
#shellinput2 = str(sys.argv[2])
inputfile1 = open(shellinput1, 'r')
#inputfile2 = open (shellinput2, 'r')
#shelloutput = raw_input('Please type your output file name for over100\n')
#shelloutput =str(sys.argv[2])
#maxsize = input('please type the AA length cutoff \n')
#maxsizenumber = str(maxsize)
#shelloutput = str( 'over' + maxsizenumber + '.txt')
shelloutput = str(sys.argv[2])
#oversizelimit = open (shelloutput,'w')
outputfile = open(shelloutput,'w')
#import temfile
app = []
for x in SeqIO.parse(inputfile1,"fasta"):
   pep = str(x.seq)
   peps = pep.strip()
   pepslen =len(peps)
   print x.id
   print x.seq
   covlen = 0
   while pepslen > 5 and peps.count("K") > 0:
      pos = peps.find("K")

      peps = peps[pos+1:]
      pepslen = len(peps)    
#      print peps
      if pos > 5 and pos <41:
           covlen += pos + 1
   coverage = 100*covlen/(len(pep)+1)
   app.append(coverage)
   print coverage
avecov = sum(app)/len(app)
print "average coverage is " + str(avecov) + " percent"
