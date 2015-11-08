#!/usr/bin/python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from collections import Counter
import sys
	#shellinput = raw_input('Please type your input file name!\n')
inputfile1 = str(sys.argv[1])
#	inputfile2 = str(sys.argv[2])
inputfile01 = open(inputfile1, 'r')
#	inputfile02 = open(inputfile2, 'r')
	#shelloutput = raw_input('Please type your output file name for over100\n')
	#shelloutput =str(sys.argv[2])
	#maxsize = input('please type the AA length cutoff \n')
	#maxsizenumber = str(maxsize)
	#shelloutput = str( 'over' + maxsizenumber + '.txt')
#outputfile1 = str(sys.argv[2])
#outputfile01 = open(outputfile1,'w')
#	outputfile2 = str(sys.argv[3])
#	outputfile02 = open(outputfile2,'w')
	#import temfile
#for n, x in enumerate(SeqIO.parse(inputfile01,"fasta")):
#   continue
#print n+1 

for n, x in enumerate(inputfile01):
     continue
print n+1
