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
#inputfile2 = open(sys.argv[2], 'r')
outputfile = open(sys.argv[2],'w')

def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]


for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
    header = x.description
    headerlist = header.split(" ")
    acce = headerlist[0].replace("hg19_refGene_","")
    accelist = acce.split("_")
    nmnr = accelist[0].strip()
    if "NR" not in nmnr:
	    mrnaseq = str(x.seq).strip()
	    for num1, char in enumerate(mrnaseq):
	       if char == char.upper():
		  upperpos = num1
		  break
            if len(mrnaseq[:upperpos])%3 == 0:
               orf = mrnaseq[0:]

            if len(mrnaseq[:upperpos])%3 == 1:
               orf = mrnaseq[1:]

            if len(mrnaseq[:upperpos])%3 == 2:
               orf = mrnaseq[2:]


	    if num%200 == 0:
	       print num
	    
	    if len(orf)%3 == 0:
	       orfcut = orf
	    elif len(orf)%3 == 1:
	       orfcut = orf + "NN"
	    elif len(orf)%3 == 2:
	       orfcut = orf + "N"

            codon = split(orfcut,3)
            orfcutrep = ''
            for z in codon:
               if z.upper() == "CGG":
                   z = "ATG"
	           orfcutrep = orfcutrep + z
               else:
                   orfcutrep = orfcutrep + z


	    seq_trans = str(Seq(orfcutrep).translate().strip())
	    seq_split = seq_trans.split("*")
	    firstorf = max(seq_split,key=len)
	    if len(firstorf) >= 6: # Take peptides longer than 6 aa 
	       result = ">" + acce + "_CGG" + "|" + "ORF_" +  header + "\n" + firstorf + "\n"
	       outputfile.write(result)



