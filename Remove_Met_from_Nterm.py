#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio.Seq import Seq
from Bio import SeqIO

inputfile1 = open(sys.argv[1],'r')
outputfile = open(sys.argv[2],'w')


for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
    header = x.description
    proseq = str(x.seq)
    idonly = x.id
    description = header.replace(idonly.strip(),"")
    if ":" in description:
        des_ls = description.split(":")
        des_ls0 = des_ls[0]
        des_ls1 = des_ls[1]
    else:
        des_ls0 = description
        des_ls1 = ""
    new_header = idonly + "Met_Removed" + "| " + des_ls0 + "#Met_Removed:" + des_ls1
    new_seq = proseq[1:]
    result = ">" + header + "\n" + proseq + "\n" + ">" + new_header + "\n" + new_seq + "\n"
    outputfile.write(result)

