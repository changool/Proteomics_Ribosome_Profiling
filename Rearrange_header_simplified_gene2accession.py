#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#python thisfile.py [gene2accession] [input fasta file] [output fasta file]

inputfile1 = open (sys.argv[1], 'r')#gene2accession_hs
inputfile2 = open (sys.argv[2], 'r')#input fasta
outputfile = open (sys.argv[3], 'w')

dic = {}
for num, y in enumerate(inputfile1): 
    y_ls = y.split("\t")
    rnaacc1 = y_ls[0].strip()
    genesym = y_ls[6].strip()
    dic[rnaacc1] = genesym

for num, x in enumerate(SeqIO.parse(inputfile2,"fasta")):
     if num%1000 == 0:
        print num
     header = x.description
     pro = str(x.seq)
     hs = header.split(" ")
     hs1 = hs[0].split("|")
     mrnaacc = hs1[2].replace('hg19_refGene_', '')
     for k,v in dic.iteritems():
        if k == mrnaacc:
           genesym1 = v
           break
     hs2 = mrnaacc + "|" + hs[0] + "|" + genesym1 + " " + mrnaacc + "#" + genesym1
     newheader = header.replace(hs[0],hs2)
#     mrnaacc = hs2[0].replace("hg19_refGene_","")
#     header1 = mrnaacc + "#" + hs[0] + "#" + hs[1] + "|" + hs[2]
     result = ">" + newheader + "\n" + pro + "\n"
     outputfile.write(result)
#     print header1
