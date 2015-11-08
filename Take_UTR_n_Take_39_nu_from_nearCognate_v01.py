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

app = []
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
    if num%1000 == 0:
        print num
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
            utr1 = mrnaseq[:upperpos]
            utr2 = mrnaseq[1:upperpos]
            utr3 = mrnaseq[2:upperpos]

            codon1 = split(utr1,3)
            codon2 = split(utr2,3)
            codon3 = split(utr3,3)

            for nn2, z in enumerate(codon1):
               if z.upper() == "CTG" or z.upper() == "GTG" or z.upper() == "ACG": 
                  nu39 = codon1[nn2-2:nn2+11]

                  nu39seq = "".join(nu39)
                  if len(nu39seq) == 39:
                     app.append(nu39seq)


            for nn2, z in enumerate(codon2):
               if z.upper() == "CTG" or z.upper() == "GTG" or z.upper() == "ACG": 
                  nu39 = codon2[nn2-2:nn2+11]
    
                  nu39seq = "".join(nu39)
                  if len(nu39seq) == 39:
                     app.append(nu39seq)
 
                     
            for nn2, z in enumerate(codon3):
               if z.upper() == "CTG" or z.upper() == "GTG" or z.upper() == "ACG": 
                  nu39 = codon3[nn2-2:nn2+11]

                  nu39seq = "".join(nu39)
                  if len(nu39seq) == 39:
                     app.append(nu39seq)
                     
for nnn, zzz in enumerate(app):
    if nnn%200 == 0:

        outputfile.write(zzz + '\n')
                 

