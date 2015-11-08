#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
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
dic = {}
for x in inputfile1:
        
        x_strip = x.strip()
        x_split = x_strip.split(";")
        header = x_split[0].strip()
        seq = x_split[1].strip()
        dic[header] = seq
        
for y in inputfile2:
   nterm = y.strip()
   j = 0
   for key,value in dic.iteritems():
        
        if nterm in value and value.index(nterm)==0:
           j += 1
     	   result = nterm +"#"+ key + "|"+ value + ";"
	   print result
	   outputfile.write(result)
   if j > 0:
        newline = '\n'
        outputfile.write(newline)
 
