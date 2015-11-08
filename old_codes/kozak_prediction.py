#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
#import argparse

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

#shellinput = raw_input('Please type your input file name!\n')
shellinput1 = str(sys.argv[1])
#shellinput2 = str(sys.argv[2])
inputfile1 = open (shellinput1, 'r')
#inputfile2= open (shellinput2, 'r')
#shelloutput = raw_input('Please type your output file name for over100\n')
#shelloutput =str(sys.argv[2])
#shelloutput = str( 'over' + maxsizenumber + '.txt')
shelloutput = str(sys.argv[2])
#oversizelimit = open (shelloutput,'w')
outputfile = open (shelloutput,'w')
#import temfile

#pep = open ('peptide.txt', 'w')


for x in inputfile1:
   xs = x.strip()
   if xs[1] == "G":
        s1 = 0.03   
   if xs[1] == "C":
        s1 = 0.02   
   if xs[1] == "A":
        s1 = 0.01   
   if xs[2] == "C" or "G"  or "T":
        s2 = 0.005   
   if xs[3] == "C" or "G"  or "A":
        s3 = 0.04   
   if xs[4] == "A" or "G":
        s4 = 0.03   
   if xs[4] == "C" or "T":
        s4 = 0.04   
   if xs[5] == "C" or "A":
        s5 = 0.04   
   if xs[5] == "T":
        s5 = 0.005   
   if xs[6] == "C":
        s6 = 0.15   
   if xs[6] == "G":
        s6 = 0.12   
   if xs[6] == "A":
        s6 = 0.1   
   if xs[10] == "G":
        s10 = 0.1   
   if xs[10] == "A" or "T":
        s10 = 0.07   
   if xs[10] == "C":
        s10 = 0.035   
   kscore = s1*s2*s3*s4*s5*s6*s10
   mrna_kscore = xs + "|" + str(kscore) + "\n"
   outputfile.write(mrna_kscore)

