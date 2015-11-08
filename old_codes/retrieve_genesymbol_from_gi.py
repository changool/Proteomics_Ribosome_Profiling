#!/usr/bin/python
# This code takes database composed of gi|protein_length|protein_sequence and give gi accession, protein length and peptide posiiton in protein to the peptides
# argv1: database composed of gi|protein_length|protein_sequence
# argv2: peptide list
# argv3: output file
from Bio import SeqIO
import sys
import fnmatch
import string
import datetime, time
#import argparse

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

#shellinput = raw_input('Please type your input file name!\n')
shellinput = str(sys.argv[1]) # database composed of gi, length, and protein sequence
shellinput1 = str(sys.argv[2]) # peptide list
read1 = open (shellinput, 'r') 
read2= open (shellinput1, 'r') 
#shelloutput = raw_input('Please type your output file name for over100\n')
#shelloutput =str(sys.argv[2])
#maxsize = input('please type the AA length cutoff \n')
#maxsizenumber = str(maxsize)
#shelloutput = str( 'over' + maxsizenumber + '.txt')
shelloutput = str(sys.argv[3]) # output file
#oversizelimit = open (shelloutput,'w')
outputfile = open (shelloutput,'w')
#shelloutput1 = str(sys.argv[4])
#outputfile1 = open (shelloutput1,'w')
#import tempfile
#f = tempfile.NamedTemporaryFile()
#pep = open ('peptide.txt', 'w')
#length = open ('peptide_len.txt', 'w')
#result = open ('output.txt', 'w')
#rightsize = 0
#small = 0
#big = 0
#total = 0
#bigger_than_sizelimit = 0




dic = {}
for x in SeqIO.parse(read1,"fasta") :
    header = x.description
    seqID = x.id
    seqID_sp = seqID.split("|")
    gi = seqID_sp[1]
    dic[gi] = header

for num, y in enumerate(read2):
    y_strip = y.strip()     
    for k,v in dic.iteritems():
        if y_strip == k:
            result = k + "|" + v + "\n" 
            print result
            outputfile.write(result)

