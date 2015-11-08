#!/usr/bin/python

import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

inputfile1 = open(sys.argv[1],'r')
outputfile = open(sys.argv[2],'w')

app = []
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #protein sequence containing fasta file
    if num%1000 == 0:
        print num
    header = x.description
    headerls = header.split("|")
    if len(headerls) >= 4:
        gi = headerls[1]
        des = headerls[4]
        acce_ls = headerls[3].split(".")
        acce = acce_ls[0]
        pro = str(x.seq)
        for num1, y in enumerate(pro):
            if num1 > 100: # Down to 100 AA
                break
            if y == 'M':
                if len(pro) >= num1+1+50:
                    mseq = pro[num1:num1+50]
                else:
                    mseq = pro[num1:len(pro)-1]
                
                if len(mseq) >= 6:
                    result = ">"+gi+'_'+ str(num1+1)+"|"+'ref'+"|"+acce+"_"+str(num1+1)+"|"+ des + '@' + mseq
                    app.append(result)

    else:
        gi = headerls[1]
        des = headerls[2]
        pro = str(x.seq)
        for num1, y in enumerate(pro):
            if num1 > 100: # Down to 100 AA
                break
            if y == 'M':
                if len(pro) >= num1+1+50:
                    mseq = pro[num1:num1+50]
                else:
                    mseq = pro[num1:len(pro)-1]
                
                if len(mseq) >= 6:
                    result = ">"+gi+'_'+ str(num1+1)+"|"+ des + '@' + mseq
                    app.append(result)

for num2, yy in enumerate(app):
    if num2%1000 == 0:
        print num2
    yy_ls = yy.split('@')
    header1 = yy_ls[0]
    seq1 = yy_ls[1]
    AA_pos = seq1.find('R') # Sequence to the first 'R'
    newseq = seq1[:AA_pos+1]
    if len(newseq) >= 6:
        result1 = header1 + '\n' + newseq + '\n'
        outputfile.write(result1)


