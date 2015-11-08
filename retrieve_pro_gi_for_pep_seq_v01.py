#!/usr/bin/python

import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

inputfile1 = open (sys.argv[1], 'r') # protein database in fasta format
inputfile2 = open (sys.argv[2], 'r') # peptide list
outputfile = open (sys.argv[3], 'w')

dic = {}
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")):
    header = x.description
    seq = str(x.seq)
    x_ls = header.split("|")
    gi = x_ls[1]
    acc = x_ls[3]
    lenth = len(seq)
    gi_len = gi + "|" + lenth
    dic[seq] = gi_len

for y in inputfile2:
    y_strip = y.strip()     
    newline = "\n"

    for k,v in dic.iteritems():
        if y_strip in k:
            seq_pos = str(k.find(y_strip) + 1)
            gi_len1 = v.split("|")
            gi1 = gi_len1[0]
            len1 = gi_len1[1]
            result = y_strip + "|" + v + "|" + seq_pos + ";"
            outputfile.write(result)
    outputfile.write(newline)