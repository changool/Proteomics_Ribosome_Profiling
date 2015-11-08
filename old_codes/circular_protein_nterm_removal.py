#!/usr/bin/python
import numpy
import sys, getopt
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from collections import Counter

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
outputfile1 = str(sys.argv[2])
outputfile01 = open(outputfile1,'w')
#	outputfile2 = str(sys.argv[3])
#	outputfile02 = open(outputfile2,'w')
	#import temfile
app = []
for num, x in enumerate(SeqIO.parse(inputfile01,"fasta")):
#	   dic = {}
	   p = str(x.seq)
	   pep = p.strip()
           header = x.description
           nterm0 = pep[:10]
           cterm = pep[-10:]
           cn0 = cterm + nterm0
           nterm1 = pep[1:11]
           cterm = pep[-10:]
           cn1 = cterm + nterm1
           nterm2 = pep[2:12]
           cterm = pep[-10:]
           cn2 = cterm + nterm2
           nterm3 = pep[3:13]
           cterm = pep[-10:]
           cn3 = cterm + nterm3
           nterm4 = pep[4:14]
           cterm = pep[-10:]
           cn4 = cterm + nterm4
           nterm5 = pep[5:15]
           cterm = pep[-10:]
           cn5 = cterm + nterm5
           nterm6 = pep[6:16]
           cterm = pep[-10:]
           cn6 = cterm + nterm6
           nterm7 = pep[7:17]
           cterm = pep[-10:]
           cn7 = cterm + nterm7
           nterm8 = pep[8:18]
           cterm = pep[-10:]
           cn8 = cterm + nterm8
           nterm9 = pep[9:19]
           cterm = pep[-10:]
           cn9 = cterm + nterm9
           nterm10 = pep[10:20]
           cterm = pep[-10:]
           cn10 = cterm + nterm10

           result = ">" + header + "_0" + "\n" + cn0  + "\n" +  ">" + header + "_1" + "\n" + cn1  + "\n" + ">" + header + "_2" + "\n" + cn2  + "\n" + ">" + header + "_3" + "\n" + cn3  + "\n" + ">" + header + "_4" + "\n" + cn4  + "\n" + ">" + header + "_5" + "\n" + cn5  + "\n" + ">" + header + "_6" + "\n" + cn6  + "\n" + ">" + header + "_7" + "\n" + cn7  + "\n" + ">" + header + "_8" + "\n" + cn8  + "\n" + ">" + header + "_9" + "\n" + cn9  + "\n" + ">" + header + "_10" + "\n" + cn10  + "\n" 










           outputfile01.write(result)


