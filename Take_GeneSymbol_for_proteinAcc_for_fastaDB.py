#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import argparse

# python *.py [gene2accession] [InPutmRNAAcce] [Outputfile]

inputfile1 = open (sys.argv[1], 'r')
inputfile2 = open (sys.argv[2], 'r')
outputfile = open (sys.argv[3], 'w')
outputfile1= open("S_cerevisiae_acc_gi_genesymbol.txt", 'w')

dic1 = {}
for num1, x in enumerate(inputfile1): # accession to gene symbol
   try:  
     xsplit = x.split("\t")
     rnaacc = xsplit[3].strip()
     rnaacclist= rnaacc.split(".")
#     rnagi  = xsplit[4].strip()
     proacc = xsplit[5].strip()
     proacclist = proacc.split(".")
     proacc1 = proacclist[0]
#     progi  = xsplit[6].strip()
     genesym= xsplit[15].strip()
     dic1[proacc1] = genesym
   except:
       pass

for num3, z in enumerate(SeqIO.parse(inputfile2,"fasta")): # Input file
     if num3%1000 == 0:
        print num3
     header = z.description
     h_ls = header.split('|')
     acc_ls = h_ls[3].split('.')
     acc = acc_ls[0]
     v1 = dic1.get(acc)
     if v1 != None:
         gene = v1
     else:
         gene = "_NONE_"
     newheader = header.replace(h_ls[3]+"| ",h_ls[3]+"|"+gene+"| "+gene+"#")
     outputfile.write(">"+newheader+"\n"+str(z.seq)+"\n")
     outputfile1.write(h_ls[1]+"|"+h_ls[3]+"|"+gene+"\n")
