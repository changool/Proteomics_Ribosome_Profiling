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

dic1 = {}
for num1, x in enumerate(inputfile1): # accession to gene symbol
   try:
     xsplit = x.split("\t")
     if xsplit[0] == "9606":# human only
        rnaacc = xsplit[3].strip()
        rnaacclist= rnaacc.split(".")
    #     rnagi  = xsplit[4].strip()
        proacc = xsplit[5].strip()
        proacclist = proacc.split(".")
        progi  = xsplit[6].strip()
        genesym= xsplit[15].strip()
        dic1[progi] = rnaacclist[0]
   except:
       pass
for num3, z in enumerate(inputfile2): # Input file
     if num3%100 == 0:
        print num3
     z_ls = z.split('.')
     inputinfo = z_ls[0].strip()
     outputfile.write(inputinfo)
     v1 = dic1.get(inputinfo)

     if v1 != None:
           result = '\t' + inputinfo + '\t' + v1
           outputfile.write(result)

     outputfile.write("\n")
