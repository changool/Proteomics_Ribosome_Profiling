#!/usr/bin/python
import sys
from Bio import SeqIO

# python *.py [gene2accession] [InPutmRNAAcce] [Outputfile]

inputfile1 = open (sys.argv[1], 'r') # HGNC gene symbols
inputfile2 = open (sys.argv[2], 'r') # Gene symboles to to be replaced to official gene symbols
outputfile = open (sys.argv[3], 'w')

gene_symbol = []
official_gene_symbol = []
official_to_alternative = {}
for x in inputfile1:
   x_sp = x.strip()
   gene_symbol.append(x_sp)
   
for xx in gene_symbol:
    xx_ls = xx.split("|")
    official_gene_symbol.append(xx_ls[0])
    official_to_alternative[xx_ls[0]] = xx

for num, y in enumerate(inputfile2):
    if num%1000==0:print num
    checker = 0
    y_st = y.strip()
    outputfile.write(y_st + '#')
    if y_st in official_gene_symbol:
        outputfile.write(y_st+ '#official_symbol')
    else:
        for k,v in official_to_alternative.iteritems():
            if y_st in v.split('|'):
                outputfile.write(k + '#replaced')
                checker = checker + 1
                break
        if checker == 0:
            outputfile.write(y_st+ '#not_in_HGNC_db')
    outputfile.write('\n')