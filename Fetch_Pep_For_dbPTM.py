#!/usr/bin/python
import sys
from Bio import SeqIO
import re
import progress_counter

inputfile1 = open (sys.argv[1], 'r') # Database from dbPTM
inputfile2 = open (sys.argv[2], 'r') # Uniprort DB
outputfile = open (sys.argv[3], 'w') # output

dic ={}
for num2, y in enumerate(SeqIO.parse(inputfile2,'fasta')): # make dictionary for fasta file
    hd = y.id
    seq = str(y.seq)
    hd_ls = hd.split("|")
    acc1 = hd_ls[1].strip()
    dic[acc1] = seq

for num1, x in enumerate(inputfile1): 
    if num1%1000 == 0: print num1
#    progress_counter.progress(inputfile1,num1,'nonfasta')
    if num1 > 0:
        x_ls = x.split('\t')
        acc = x_ls[1].strip()
        pos = int(x_ls[2].strip())
        residue = x_ls[6].strip()
        pro_seq = dic.get(acc)
       
        if pro_seq != None:
            if pos < 21:
                pep40 = pro_seq[:(pos -1) + 21]
            elif len(pro_seq) - pos < 20:
                pep40 = pro_seq[(pos - 1) -20 : len(pro_seq) -1]
            else:
                pep40 = pro_seq[(pos-1) -20 : (pos -1) + 21]
            
            if residue == 'K':
                i = 1
                pep_right = 'K'
            elif residue == 'R':
                i = 1
                pep_right = 'R'
            else:
                i = 0
                pep_right = ''
            if pos + i >= len(pro_seq):
                try:
                    pep_right = pro_seq[pos -1]
                except:
                    pep_right = '__ERROR__'
            else:
                while (pro_seq[pos -1 + i] != 'K' and pro_seq[pos -1 + i] != 'R' and pos + i < len(pro_seq)):
                    pep_right = pep_right + pro_seq[pos -1 + i]
                    i += 1
                pep_right = pep_right + pro_seq[pos -1 + i]

            if pos == 1:
                pep_left = ''
            elif pos ==2:
                pep_left = pro_seq[pos-2]
            else:                        
                i = -1
                pep_left = ''
                try:
                    while (pro_seq[pos -1 + i] != 'K' and pro_seq[pos -1 + i] != 'R' and pos + i - 2 >= 0):
                        pep_left = pro_seq[pos -1 + i] + pep_left
                        i -= 1
                except:
                    pep_left = '__ERROR__'
            pep_tryp = pep_left + pep_right
            
        else:
            pep40 = 'No_protein_match'
            pep_tryp = ''
        result = x.strip() +'\t'+ pep40 +'\t'+ pep_tryp + '\n'
        outputfile.write(result)

        
