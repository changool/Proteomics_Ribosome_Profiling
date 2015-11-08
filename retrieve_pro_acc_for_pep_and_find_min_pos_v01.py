#!/usr/bin/python

import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

inputfile1 = open (sys.argv[1], 'r') # protein database in fasta format
inputfile2 = open (sys.argv[2], 'r') # peptide list
outputfile = open (sys.argv[3], 'w')

dic = {}
print "1st dictionary generation"
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")):
    header = x.description
    seq = str(x.seq)
    x_ls = header.split("|")
#    gi = x_ls[1]
    acc = x_ls[3].split('.')
    acc0 = acc[0]
    lenth = len(seq)
    gi_len = acc0
    dic[seq] = acc0

templist = []
print "Working on peptide list"
for num1, y in enumerate(inputfile2):
    if num1%100==0:
        print num1
    y_st = y.strip()     
    tempstr = ""
    for k,v in dic.iteritems():
        if y_st in k:
            seq_pos = str(k.find(y_st) + 1)
            m1posAA = k[int(seq_pos)-2]
            firstposAA = k[int(seq_pos)-1]
            if int(seq_pos) <= 2:
                if m1posAA == "M" or firstposAA == "M":
                    atgclass = "ATG_start"
                else:
                    atgclass = "nonATG_start"
            else:
                if m1posAA == "M" or firstposAA == "M":
                    atgclass = "ATG_down"
                else:
                    atgclass = "nonATG_down"   
            result = m1posAA + "|" + y_st + "|" + v + "|" + seq_pos + "|" + atgclass + ";"
            tempstr = tempstr + result
    if len(tempstr) == 0:
        tempstr = "X" + "|" + y_st + "|" + "no_match" + "|" + '?' + "|" + "UTR" + ';'
    templist.append(tempstr)

print "Assorting min and max position"
for xx in templist:
    xx_st = xx.strip()
#    print xx_st
    xx_ls = xx_st.split(";")

    dic1 = {}
    dic2 = {}
    for yy in xx_ls:
        if len(yy) > 0:
           yy_split = yy.split("|")
           acc2=yy_split[1].strip()
           pos = yy_split[2].strip()
           if "NP_" in acc2:
              dic1[yy.strip()] = pos
           else:
              dic2[yy.strip()] = pos
    if len(dic1) == 0:
        if 'XP_' in dic2.keys()[0]:
            min_result = min(dic2,key=dic2.get) + "\n"        
            outputfile.write(min_result)
        else:
            outputfile.write(xx_ls[0] + '\n')
    else:
        min_result = min(dic1,key=dic1.get) + "\n"
#        min_result = min(dic1,key=dic1.get) + ";"
#        max_result = max(dic1,key=dic1.get) + "\n"
        outputfile.write(min_result)
#        outputfile.write(max_result)