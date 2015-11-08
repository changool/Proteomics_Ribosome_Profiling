#!/usr/bin/python
import numpy
import sys, getopt
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from collections import Counter
def main(argv):
	#inputfile = ''
	#outputfile = ''
	try:
	   opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
	   print 'test.py -i <inputfile> -o <outputfile>'
	   sys.exit(2)
	for opt, arg in opts:
	   if opt == '-h':
	      print 'test.py -i <inputfile> -o <outputfile>'
	      sys.exit()
	   elif opt in ("-i", "--ifile"):
	      inputfile = arg
	   elif opt in ("-o", "--ofile"):
	      outputfile = arg
#   print 'Input file is "', inputfile
#   print 'Output file is "', outputfile


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
           descrip = x.description
           olf = "olfactory receptor"
           if olf in descrip:
                result = ">" + descrip + "\n" + str(x.seq)+ "\n"
                outputfile01.write(result)

if __name__ == "__main__":
   main(sys.argv[1:])
