#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
import re
import collections

inputfile1 = open (sys.argv[1], 'r')
inputfile2 = open (sys.argv[2], 'r')
outputfile = open (sys.argv[3], 'w')

newtable = []
gilist = []
for num3, z in enumerate(inputfile1): # input table: this process is for pTy
  if 'Checked' not in z:

     z_ls = z.split('\t')
     ph = z_ls[12].strip()
     ph_ls = ph.split(';')
     dic1 = {}
     score = 0
     gi_ls = z_ls[9].split(';')
     firstgi = gi_ls[0].strip()
     gilist.append(firstgi)
     if len(ph_ls) > 0:
        for zz in ph_ls:
            zz_ls = zz.split(':')
            if len(zz_ls) < 2:
                continue
            site = zz_ls[0].strip()
            site1 = re.findall('.(.*)\(',site)
            residue = site[0]
            prob = zz_ls[1].strip()
            dic1[site1[0]] = prob
        
        #for k,v in dic1.iteritems():
        #    newv = str(float(v) + score)
        #    dic1[k] = newv
        if len(dic1) > 0:
            maxsite = max(dic1,key=dic1.get)
            newprob = dic1.get(maxsite)
            if newprob >= 75:   
                newrowlist = (z_ls[2],z_ls[8],firstgi,maxsite,str(newprob))
                newrow = '\t'.join(newrowlist)
                newtable.append(newrow)

uniquegilist = list(set(gilist))

dic2 = {}
for fasta in SeqIO.parse(inputfile2,"fasta"):# fasta file
    header = fasta.id
    header_ls = header.split("|")
    gi = header_ls[1]
    seq = str(fasta.seq)
    des = fasta.description
    des_ls = des.split('#')
    if len(des_ls) >= 2:
        genesym = des_ls[1]
    else:
        genesym = ''
    dic2[gi] = seq.strip() + "#"+genesym

headlist = ('gi','Gene Symbol','Site Position','Peptide','Summed PSM')
head = "\t".join(headlist) + '\n'    
outputfile.write(head)
for x in uniquegilist:
    dic3 = {}
    pro_genesym = dic2.get(x)
    pro_genesym_ls = pro_genesym.split('#')
    pro = pro_genesym_ls[0]
    genesym = pro_genesym_ls[1]
    if pro == None:
        print 'protein seq for',x, 'is empty'
        exit()

    for numx, xxx in enumerate(pro):
        dic3[numx+1] = 0

    for xx in newtable:
        xx_ls = xx.split('\t')
        pep1 = xx_ls[0]
        psm = xx_ls[1]
        gi1 = xx_ls[2]
        site1 = xx_ls[3]
        if gi1 == x:
            peppos = pro.find(pep1)
            phossite1 = int(peppos) + int(site1)
            oldpsm = dic3.get(phossite1)

            dic3[phossite1] = int(oldpsm) + int(psm)
    od = collections.OrderedDict(sorted(dic3.items()))

    for k2,v2 in od.iteritems():
        if v2 > 0:
            if int(k2) <= 11:
                pep10 = pro[:int(k2)+10]
            elif int(k2) + 12 > len(pro):
                pep10 = pro[int(k2)-11:]
            else:
                pep10 = pro[int(k2)-11:int(k2)+10]
            resultlist = (x,genesym,str(k2),pep10,str(v2))
            result = "\t".join(resultlist) + '\n'
            outputfile.write(result)
    


