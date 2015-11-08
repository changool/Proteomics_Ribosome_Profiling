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
inputfile1 = open (shellinput1, 'r')
#inputfile2 = open (shellinput2, 'r')
#shelloutput = raw_input('Please type your output file name for over100\n')
#shelloutput =str(sys.argv[2])
#maxsize = input('please type the AA length cutoff \n')
#maxsizenumber = str(maxsize)
#shelloutput = str( 'over' + maxsizenumber + '.txt')
shelloutput = str(sys.argv[2])
#oversizelimit = open (shelloutput,'w')
outputfile = open (shelloutput,'w')
#import temfile

for n, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #peptide containing file

	header = x.description
        pep = str(x.seq)
        if len(pep) > 23:
           result = ">"+ header + "\n" + pep + "\n"
           outputfile.write(result)

