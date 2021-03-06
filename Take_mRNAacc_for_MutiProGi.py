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
     xsplit = x.split("\t")
     rnaacc = xsplit[3].strip()
     rnaacclist= rnaacc.split(".")
#     rnagi  = xsplit[4].strip()
     proacc = xsplit[5].strip()
     proacclist = proacc.split(".")
     progi  = xsplit[6].strip()
     genesym= xsplit[15].strip()
     dic1[progi] = rnaacclist[0]

for num3, z in enumerate(inputfile2): # Multiple Gi separated by ;
     if num3%100 == 0:
        print num3
     z_sp = z.strip().split(';')
     for zzz in z_sp:
        if '_' not in zzz:
           zzz_ls = zzz.strip().split(' ')
           z_gi = zzz_ls[0]
           break
     z_ls = z_gi.split('.')
     inputinfo = z_ls[0].strip()
     outputfile.write(inputinfo)
     for k1,v1 in dic1.iteritems():
        if k1 == inputinfo:
           result = '\t' + k1 + '\t' + v1
           outputfile.write(result)
           break
     outputfile.write("\n")
