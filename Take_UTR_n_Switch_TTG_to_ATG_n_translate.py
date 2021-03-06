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
	    utr = mrnaseq[:upperpos + 15] # Take down to 5 aa downstream of start site
	    if num%200 == 0:
	       print num
	    
	    if len(utr)%3 == 0:
	       utrcut = utr
	    elif len(utr)%3 == 1:
	       utrcut = utr[1:]
	    elif len(utr)%3 == 2:
	       utrcut = utr[2:]

            codon = split(utrcut,3)
            utrcutrep = ''
            for z in codon:
               if z.upper() == "TTG":
                   z = "ATG"
	           utrcutrep = utrcutrep + z
               else:
                   utrcutrep = utrcutrep + z


	    seq_trans = str(Seq(utrcutrep).translate().strip())
	    seq_split = seq_trans.split("*")
	    lastuorf = seq_split[len(seq_split) - 1]
	    if len(lastuorf) >= 6: # Take peptides longer than 6 aa 
	       result = ">" + acce + "|" + "last_uORF_" +  header + "\n" + lastuorf + "\n"
	       outputfile.write(result)



