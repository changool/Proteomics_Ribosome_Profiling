#!/usr/bin/python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from collections import Counter
import sys
	#shellinput = raw_input('Please type your input file name!\n')
#	inputfile2 = str(sys.argv[2])
inputfile1 = open(sys.argv[1], 'r')
#	inputfile02 = open(inputfile2, 'r')
	#shelloutput = raw_input('Please type your output file name for over100\n')
	#shelloutput =str(sys.argv[2])
	#maxsize = input('please type the AA length cutoff \n')
	#maxsizenumber = str(maxsize)
	#shelloutput = str( 'over' + maxsizenumber + '.txt')
outputfile = open(sys.argv[2], 'w')
#	outputfile2 = str(sys.argv[3])
#	outputfile02 = open(outputfile2,'w')
	#import temfile
#for n, x in enumerate(SeqIO.parse(inputfile01,"fasta")):
#   continue
#print n+1 

for n, x in enumerate(inputfile1):
   if n >= 33427:
      result = x.strip() + "\n"
      outputfile.write(result)

