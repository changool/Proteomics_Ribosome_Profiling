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
#        x_split = x_strip.split("|")
        no = x_split[0].strip()
#        ch = x_split[1].strip()
#        st = x_split[2].strip()
#        ed = x_split[3].strip()
        chsted = x_split[1].strip()
#        chsted = ch +"|"+ st +"|"+ ed
        dic[chsted] = no
        
for y in inputfile2:
   num = y.strip()
   for key,value in dic.iteritems():

        if num.strip() == value.strip():
	  result = value.strip()+"|" +key.strip()+";"
	  print result
	  outputfile.write(result)
   newline = '\n'
   outputfile.write(newline)
 
