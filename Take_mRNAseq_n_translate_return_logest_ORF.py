#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
#import re
#import argparse
#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')
#args = parser.parse_args()
#shellinput = raw_input('Please type your input file name!\n')


inputfile1 = open(sys.argv[1],'r')
outputfile = open(sys.argv[2],'w')

#def split(str, num):
#    return [ str[start:start+num] for start in range(0, len(str), num) ]


#for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
#    header = x.description
#    headerlist = header.split(" ")
#    acce = headerlist[0].replace("hg19_refGene_","")
#    accelist = acce.split("_")
#    nmnr = accelist[0].strip()
#    if "NR" not in nmnr:
#	    mrnaseq = str(x.seq).strip()
#	    for num1, char in enumerate(mrnaseq):
#	       if char == char.upper():
#		  upperpos = num1
#		  break
#            if len(mrnaseq[:upperpos])%3 == 0:
#               orf = mrnaseq[0:]
#
#            if len(mrnaseq[:upperpos])%3 == 1:
#               orf = mrnaseq[1:]
#
#            if len(mrnaseq[:upperpos])%3 == 2:
#               orf = mrnaseq[2:]
#
#
#	    if num%200 == 0:
#	       print num
#	    
#	    if len(orf)%3 == 0:
#	       orfcut = orf
#	    elif len(orf)%3 == 1:
#	       orfcut = orf + "NN"
#	    elif len(orf)%3 == 2:
#	       orfcut = orf + "N"
#
#	    seq_trans = str(Seq(orfcut).translate().strip())
#	    seq_split = seq_trans.split("*")
#	    firstorf = max(seq_split,key=len)
#	    if len(firstorf) >= 6: # Take peptides longer than 6 aa 
#	       result = ">" + acce + "|" + "ORF_" +  header + "\n" + firstorf + "\n"
#	       outputfile.write(result)

for num, x in enumerate(inputfile1):
            mrnaseq = x.strip()

	    if num%200 == 0:
	       print num
	    
	    if len(mrnaseq)%3 == 0:
	       orfcut = mrnaseq
	    elif len(mrnaseq)%3 == 1:
	       orfcut = mrnaseq + "NN"
	    elif len(mrnaseq)%3 == 2:
	       orfcut = mrnaseq + "N"

	    seq_trans1 = str(Seq(orfcut).translate().strip())
	    seq_trans2 = str(Seq(orfcut[1:-2]).translate().strip())
	    seq_trans3 = str(Seq(orfcut[2:-1]).translate().strip())
	    combined_seq_trans = seq_trans1 + '*' + seq_trans2 + '*' + seq_trans3
	    seq_split = combined_seq_trans.split("*")
	    longestorf = max(seq_split,key=len)
	    if len(longestorf) >= 6: # Take peptides longer than 6 aa 
	       result = longestorf + "\n"
	       outputfile.write(result)

