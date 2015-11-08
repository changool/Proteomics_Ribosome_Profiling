#!/usr/bin/python
import sys
from Bio import SeqIO
import re
import collections

inputfile1 = open (sys.argv[1], 'r')# table from Proteome Discoverer 2.0
inputfile2 = open (sys.argv[2], 'r')# Protein fasta dabase
inputfile3 = open (sys.argv[3], 'r')# Phosphosite DB from phosphoplus (PROTEIN,ACC_ID,GENE,HU_CHR_LOC,MOD_RSD,SITE_GRP_ID,ORGANISM,MW_kD,DOMAIN,SITE_+/-7_AA,LT_LIT,MS_LIT,MS_CST,CST_CAT#)
outputfile = open (sys.argv[4], 'w')


table_type = 'PSM' # 'PSM' or 'Peptide'
sample_species = 'human' # 'human' or 'mouse' or 'rat'
newtable = []
gilist = []
print 'In the middle of reading PD table'
for num3, z in enumerate(inputfile1): # input table: this process is for pTy
     if 'Checked' in z:
         continue
     if table_type == 'PSM':   
        z_ls = z.split('\t')
        ph = z_ls[41].strip() # column for Phosphosite and probability ( 41 for PSM table, 12 for peptide table)
        ph_ls = ph.split(';')
        dic1 = {}
        score = 0
        gi_ls = z_ls[8].split(';') # list for gi(8 for PSM table, 9 for peptide talbe)
        firstgi = gi_ls[0].strip()
        gilist.append(firstgi)
        pep11 = z_ls[4].strip() # peptide sequence (4 for PSM table, 2 for peptide talbe)
        psm11 = str(1) #PSM number (for PSM table, use 1)
     elif table_type == 'Peptide':   
        z_ls = z.split('\t')
        ph = z_ls[12].strip() # column for Phosphosite and probability ( 41 for PSM table, 12 for peptide table)
        ph_ls = ph.split(';')
        dic1 = {}
        score = 0
        gi_ls = z_ls[9].split(';') # list for gi(8 for PSM table, 9 for peptide talbe)
        firstgi = gi_ls[0].strip()
        gilist.append(firstgi)
        pep11 = z_ls[2].strip() # peptide sequence (4 for PSM table, 2 for peptide talbe)
        psm11 = z_ls[8].strip() #PSM number for petpide table
     if len(ph_ls) > 0:
        probsum = 0
        for zz in ph_ls:
            zz_ls = zz.split(':')
            if len(zz_ls) < 2:
                continue
            prob = zz_ls[1].strip()
            probsum = probsum + float(prob)
        
        if probsum <= 110:
            for zz in ph_ls:
                zz_ls = zz.split(':')
                if len(zz_ls) < 2:
                    continue
                site = zz_ls[0].strip()
                site1 = re.findall('.(.*)\(',site)
                residue = site1[0]
                prob = float(zz_ls[1].strip())
                dic1[site1[0]] = prob
            
            if len(dic1) > 0:
                maxsite = max(dic1,key=dic1.get)
                newprob = dic1.get(maxsite)
                if float(newprob) >= 75:   
                    newrowlist = (pep11,psm11,firstgi,maxsite,str(newprob))
                    newrow = '\t'.join(newrowlist)
                    newtable.append(newrow)

        if probsum > 110:
            for zz in ph_ls:
                zz_ls = zz.split(':')
                if len(zz_ls) < 2:
                    continue
                site = zz_ls[0].strip()
                site1 = re.findall('.(.*)\(',site)
                residue = site1[0]
                prob = float(zz_ls[1].strip())
                if prob >= 75:   
                    newrowlist = (pep11,psm11,firstgi,residue,str(prob))
                    newrow = '\t'.join(newrowlist)
                    newtable.append(newrow)


uniquegilist = list(set(gilist))

print 'In the middle of reading fasta db'
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

print 'In the middle of reading Phosphosite db'
con_seq = '#'
for yyy in inputfile3:
    yyy_ls = yyy.split('\t')
    if len(yyy_ls) >= 10:
        if yyy_ls[6].strip() == sample_species:
            con_seq = con_seq +'#'+ yyy_ls[9].strip()
con_seq = con_seq + '#'

print 'In the middle of writing result'
headlist = ('gi','Gene Symbol','Site Position','Peptide(-10to+10)','Summed PSM','In Phosphosite DB?')
head = "\t".join(headlist) + '\n'    
outputfile.write(head)
for x in uniquegilist:
    dic3 = {}
    pro_genesym = dic2.get(str(x))
    if pro_genesym == None:
        print x,'does not have matching protein'
        continue
    pro_genesym_ls = pro_genesym.split('#')
    pro = pro_genesym_ls[0]
    genesym = pro_genesym_ls[1]
    if len(pro) < 10:
        print 'protein seq for',x, 'is empty'
        continue

    for numx, xxx in enumerate(pro):
        dic3[numx+1] = 0

    for xx in newtable:
        xx_ls = xx.split('\t')
        pep1 = xx_ls[0].upper()
        psm = xx_ls[1]
        gi1 = xx_ls[2]
        site1 = xx_ls[3]
        ratio = xx_ls[5]
        if gi1 == x:
            peppos = pro.find(pep1)
            phossite1 = int(peppos) + int(site1)
            oldpsm = dic3.get(phossite1)
            if oldpsm == None:
                oldpsm = 0
                print 'Phospho site in protein',phossite1,'is bigger than protein length',len(dic3)

            dic3[phossite1] = int(oldpsm) + int(psm)
    od = collections.OrderedDict(sorted(dic3.items()))

    for k2,v2 in od.iteritems():
        if v2 > 0:
            if k2-1 <= 7:
                pep10 = pro[:k2-1] + pro[k2-1].lower() + pro[k2:k2-1+8]
                pep10 = '_'*(15-len(pep10))+pep10
            elif k2-1 + 10 > len(pro):
                pep10 = pro[k2-1-7:k2-1] + pro[k2-1].lower() + pro[k2:]
                pep10 = pep10 + '_'*(15-len(pep10))
            else:
                pep10 = pro[k2-1-7:k2-1] + pro[k2-1].lower() + pro[k2:k2-1+8]
 
            if '#'+pep10+'#' in con_seq:
                foundornot = 'IN DB'
            else:
                foundornot = 'NOT IN DB'
            resultlist = (x,genesym,str(k2),pep10,str(v2),foundornot)
            result = "\t".join(resultlist) + '\n'
            outputfile.write(result)
    


