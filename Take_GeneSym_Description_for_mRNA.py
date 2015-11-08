#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import argparse

#parser=argparse.ArgumentParser(description='python *.py [Accession2Gene] [ProteinDatabase] [InPutmRNAAcce] [Outputfile]')

#args = parser.parse_args()

# python *.py [gene2accession] [ProteinDatabase] [InPutmRNAAcce] [Outputfile]

shellinput1 = str(sys.argv[1])
shellinput2 = str(sys.argv[2])
shellinput3 = str(sys.argv[3])
inputfile1 = open (shellinput1, 'r')
inputfile2 = open (shellinput2, 'r')
inputfile3 = open (shellinput3, 'r')
shelloutput = str(sys.argv[4])
outputfile = open (shelloutput,'w')

dic1 = {}
for num1, x in enumerate(inputfile1): # accession to gene symbol
     xsplit = x.split("\t")
     rnaacc = xsplit[3].strip()
     rnaacclist= rnaacc.split(".")
#     rnagi  = xsplit[4].strip()
     proacc = xsplit[5].strip()
     proacclist = proacc.split(".")
#     progi  = xsplit[6].strip()
#     genesym= xsplit[15].strip()
     dic1[rnaacclist[0]] = proacclist[0]

dic2 = {}
for num2, y in enumerate(SeqIO.parse(inputfile2,"fasta")): # Protein database
     header = y.description
     pro = str(y.seq)

     headerlist = header.split(" ")
     idlist = headerlist[0].split("|")
     proacc1 = idlist[3]
     proacc1list = proacc1.split(".")
     dic2[proacc1list[0]] = header
     dic2len = len(dic2)

for num3, z in enumerate(inputfile3): # Input file
     if num3%1000 == 0:
        print num3
     zstrip = z.strip()
     outputfile.write(zstrip)
     for k1,v1 in dic1.iteritems():
        if k1 == zstrip:
           i = 0
           for k2,v2 in dic2.iteritems():
              i += 1
              if k2 == v1:
                 result = "@" + v2     
                 outputfile.write(result)
                 break
           if i == dic2len:
              continue
           else:
              break
     newline = "\n"
     outputfile.write(newline)
