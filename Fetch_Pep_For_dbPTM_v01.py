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

oneper = progress_counter.linenum(inputfile1,'nonfasta')
for num1, x in enumerate(inputfile1): 
    progress_counter.progress(num1,oneper)
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
            
            pro_left = pro_seq[:pos-1]
            pro_left_rev = pro_left[::-1]
            pro_right = pro_seq[pos:]
            
            pep_left = ''
            for num2, xx in enumerate(pro_left_rev):
                if xx == 'K' or xx == 'R':
                    if pro_left_rev[num2-1] != 'P':
                        pep_left = pep_left
                        break
                    else:
                        pep_left = xx + pep_left
                        continue               
                else:
                    pep_left = xx + pep_left
            
            pep_right = ''
            for num3, xxx in enumerate(pro_right):
                if xxx == 'K' or xxx == 'R':
                    if len(pro_right) == num3 + 1:
                        pep_right = pep_right + xxx
                        break
                    elif pro_right[num3 + 1] != 'P':
                        pep_right = pep_right + xxx
                        break        
                    else:
                        pep_right = pep_right + xxx
                        continue
                
                else:
                    pep_right = pep_right + xxx        
                    
            pep_tryp = pep_left + residue.lower() + pep_right
            result = x.strip() + '\t' + pep40 + '\t' + pep_tryp + '\n'
            outputfile.write(result)