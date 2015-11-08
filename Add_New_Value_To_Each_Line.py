#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
#import argparse
#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')
#args = parser.parse_args()
#shellinput = raw_input('Please type your input file name!\n')



inputfile1 = open (sys.argv[1], 'r')
#inputfile2 = open (sys.argv[2], 'r')
outputfile = open (sys.argv[2], 'w')



#def split(str, num):
#    return [ str[start:start+num] for start in range(0, len(str), num) ]
#for totallines, zzz in enumerate(SeqIO.parse(inputfile1,"fasta")):
#   continue
#inputfile1.seek(0)
for num, x in enumerate(inputfile1): #RNAacce|Position of Nucleotide on mRNA|Nucleotide|AA|Chr|Coor|Strand|RiboSeq ReadNo|
   x_ls = x.strip().split("\t")

   result = x_ls[0] + "\t" +  x_ls[1] + "\t" +  x_ls[2] + "\t" +  x_ls[3] + "\t" +  x_ls[4] + "\t" +  x_ls[5] + "\t" +  x_ls[6] + "\t" +  x_ls[7] + "\t" + "0" + "\n"
   outputfile.write(result)
