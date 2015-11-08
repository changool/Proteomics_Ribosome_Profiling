#!/usr/bin/python
import numpy
import sys, getopt
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from collections import Counter
inputfile01 = open(sys.argv[1], 'r')
#	inputfile02 = open(sys.argv[2], 'r')
#	outputfile = open(sys.argv[2],'w')
ii = 0
iii = 0
app = []
for num, x in enumerate(SeqIO.parse(inputfile01,"fasta")):
   dic = {}
   p = str(x.seq)
   pep = p.strip()
   i = 0   
   while i <= len(pep)-1:
      dic[i] = 0
      i += 1

#Trypsin 	      
      
   pep01 = pep.replace("KP","XP")
   pep02 = pep01.replace("RP","YP")
   pep_rep03 = pep02.replace("K","K|")
   pep_rep04 = pep_rep03.replace("R","R|")
   if pep_rep04[-1] == "|":
       pep_rep04= pep_rep04[:-2]
   pep_enz01 = pep_rep04.split("|")
   for y01 in pep_enz01:
      pep_len01 = len(y01)     
      if pep_len01 >= 6 and pep_len01 <= 40:
	 ii += 1
	 if "C" in y01:
	    iii += 1
print "cystein containig peptide is ", 100*iii/ii ,"%"
#		 pep_pos01 = pep02.find(y01)
#		 for key,value in dic.iteritems():
#		     if key >= pep_pos01 and key <= pep_pos01 + pep_len01 -1:
#			  dic[key] += 1



