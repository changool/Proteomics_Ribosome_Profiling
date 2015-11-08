#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

inputfile1 = open(sys.argv[1],'r')
outputfile = open(sys.argv[2],'w')


for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
    header = x.description
    headerlist = header.split(" ")
#    acce = headerlist[0].replace("hg19_refGene_","") # This is for human database
    acce = headerlist[0].replace("mm10_refGene_","") # This is for mouse database
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
	    
	    seq_trans = str(Seq(utrcut).translate().strip())
	    seq_split = seq_trans.split("*")
	    lastuorf = seq_split[len(seq_split) - 1]
	    if len(lastuorf) >= 6: # Take peptides longer than 6 aa 
	       result = ">" + acce + "|" + "last_uORF_" +  header + "\n" + lastuorf + "\n"
	       outputfile.write(result)
