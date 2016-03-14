#!/usr/bin/python

import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
import re

inputfile1 = open (sys.argv[1], 'r') # protein database in fasta format
inputfile2 = open (sys.argv[2], 'r') # peptide list
inputfile3 = open (sys.argv[3], 'r') # gene to accessions
inputfile4 = open (sys.argv[4], 'r') # RNAseq database
outputfile = open (sys.argv[5], 'w')

dic = {}
print "Generating dictionary for protein accession and sequence"
#for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): # NCBI format
#    header = x.description
#    seq = str(x.seq)
#    x_ls = header.split("|")
##    gi = x_ls[1]
#    acc = x_ls[3].split('.')
#    acc0 = acc[0]
#    dic[seq] = acc0
#for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): # rff format
#    header = x.description
#    seq = str(x.seq)
#    x_ls = header.split(" ")
##    gi = x_ls[1]
#    acc = x_ls[0].split('.')
#    acc0 = acc[0]
#    dic[seq] = acc0
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): # rff format
    header = x.description
    seq = str(x.seq)
    x_ls = header.split("|")
#    gi = x_ls[1]
    acc = x_ls[0].split('.')
    acc0 = acc[0]
    acc0_ls = re.findall('^(\w\w_\d*)_frame?',acc0)
    acc00 = acc0_ls[0]
    dic[seq] = acc00

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
            if int(seq_pos) == 1:
                m1posAA = "-"
            else:
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
            result = m1posAA + "|" + y_st + "|" + v + "|" + seq_pos + "|" + atgclass + ";" # y_st is peptide, v is accession
            tempstr = tempstr + result
    if len(tempstr) == 0:
        tempstr = "-" + "|" + y_st + "|" + "no_match" + "|" + '-' + "|" + "UTR" + ';'
    templist.append(tempstr)

print "Assorting min and max position"
templist1 = []

for xx in templist: # This is for customized DB with mRNA accession for protein. This is for finding min position for NP entries
    xx_st = xx.strip()
#    print xx_st
    xx_ls = xx_st.split(";")

    dic1 = {}
    dic2 = {}
    for yy in xx_ls:
        if len(yy) > 0:
           yy_split = yy.split("|")
           acc2=yy_split[2].strip()
           pos = yy_split[3].strip()
           if "NM_" in acc2:
              dic1[yy.strip()] = pos
           else:
              dic2[yy.strip()] = pos
    if len(dic1) == 0:
        if 'XM_' in dic2.keys()[0]:
            min_result = min(dic2,key=dic2.get)        
            templist1.append(min_result)
        else:
            templist1.append(xx_ls[0])
    else:
        min_result = min(dic1,key=dic1.get)
        templist1.append(min_result)

print "Making dictionary for gene symbol to accessions"
dic3 = {}
for num2, xxx in enumerate(inputfile3): # accession to gene symbol This is for mRNA
     xxxsplit = xxx.split("\t")
     rnaacc = xxxsplit[3].strip()
     rnaacclist= rnaacc.split(".")
#     rnagi  = xxxsplit[4].strip()
     proacc = xxxsplit[5].strip()
     proacclist = proacc.split(".")
#     progi  = xxxsplit[6].strip()
     genesym= xxxsplit[15].strip()
#     dic1[proacclist[0]] = rnaacclist[0]
     dic3[proacclist[0]] = rnaacclist[0] + "|" + genesym

print "Addding mRNA accession and gene symbol"
templist2 = []
for num3, z in enumerate(templist1): # -1_pos_AA|pep_seq|pro_acc|pos|ATG_classification
     if num3%100 == 0:
        print num3
     z_ls = z.split('|')
     proacc00 = z_ls[2].strip()
     if proacc00 in dic3.keys():
         v1 = dic3.get(proacc00)
         templist2.append(z + "|" + v1)
     else:
         templist2.append(z + "|")

print "Making dictionary for mRNA accession and mRNA sequence"
dic4 = {}
#for x in SeqIO.parse(inputfile4,"fasta"): #rna sequence fast format database: Refseq format
#   header = x.description
#   mrnaseq = str(x.seq)
#   headersplit = header.split(" ")
##   mrnaacce = headersplit[3].split(".")
##   mrnaacce0 = mrnaacce[0].strip()
#   mrnaacce0 = headersplit[0].replace("hg19_refGene_","")
#   dic4[mrnaacce0] = mrnaseq
   
for q in SeqIO.parse(inputfile4,"fasta"): #rna sequence fast format database: rff format
   header = q.description
   mrnaseq = str(q.seq)
   headersplit = header.split(" ")
#   mrnaacce = headersplit[3].split(".")
#   mrnaacce0 = mrnaacce[0].strip()
#   mrnaacce0 = headersplit[0].replace("hg19_refGene_","")
   dic4[headersplit[0]] = mrnaseq

print "Finding right codons"
head = "-1_pos_AA" +'|'+ "pep_seq" + '|' + "pro_acc" + '|' + "pep_pos" + '|' + "ATG_classification" + "|" + 'mRNA accession' + "|" + "Gene Symbol" + "|" + 'mRNA accession' + "|" + 'peptide sequence' + "|" + 'peptide position in translated mRNA' + "|" + 'translated protein seq' + "|" + 'peptide seq from -3 to 10' + "|" + 'mRNA sequence' + "|" + 'mRNA sequence from -9 to 30' + "|" + 'mRNA seq from -9 to -7' + "|" +  'mRNA sequence from -6 to -4' + "|" + 'mRNA seq from -3 to -1' + "|" + 'mRNA seq from 1 to 3' + '\n'                    
outputfile.write(head)
for num10, y in enumerate(templist2): #-1_pos_AA|pep_seq|pro_acc|pos|ATG_classification|mRNA_acc|Gene_sym
    if num10%200 == 0:
       print num10
    y_strip = y.strip()
    y_split = y_strip.split("|")
    mrnaacce1 = y_split[5].split(".")
    mrnaacce2 = mrnaacce1[0].strip()
    pep = y_split[1].strip()
    result0 = y_strip + "|"
    outputfile.write(result0)
    
    for k,v in dic4.iteritems(): # mRNA_accession : mRNA_sequence
	k_strip = k.strip()
	
	if mrnaacce2 == k_strip:
	       seq1 = v[0:].strip()
	       seq2 = v[1:].strip() 
	       seq3 = v[2:].strip() 

	       if len(seq1)%3 == 0:
		   seq1_mod = seq1
	       elif len(seq1)%3 ==1:
		   seq1_mod = seq1 + "NN"
	       else:
		   seq1_mod = seq1 + "N"
	       
	       if len(seq2)%3 == 0:
		   seq2_mod = seq2  
	       elif len(seq2)%3 ==1:
		   seq2_mod = seq2 + "NN"
	       else:
		   seq2_mod = seq2 + "N"
	       
	       if len(seq3)%3 == 0:
		   seq3_mod = seq3  
	       elif len(seq3)%3 ==1:
		   seq3_mod = seq3 + "NN"
	       else:
		   seq3_mod = seq3 + "N"

	       seq1_per = Seq(seq1_mod)
	       seq2_per = Seq(seq2_mod)
	       seq3_per = Seq(seq3_mod)

	       seq1_trans = seq1_per.translate()
	       seq2_trans = seq2_per.translate()                       
	       seq3_trans = seq3_per.translate()
	       
    
	       seq1_trans_strip = str(seq1_trans.strip())
	       seq2_trans_strip = str(seq2_trans.strip())
	       seq3_trans_strip = str(seq3_trans.strip())
	       
	       seq1_rep = seq1_trans_strip.replace("*","^")
	       seq2_rep = seq2_trans_strip.replace("*","^")
	       seq3_rep = seq3_trans_strip.replace("*","^")
	       
	       result1 = k_strip + "|" + pep
               outputfile.write(result1)
	      

	       if pep in seq1_rep:                            
		    pep_pos = seq1_rep.find(pep)
		    pep_M3toP10 = seq1_rep[pep_pos-3:pep_pos+10]                                                    
		    seq_M9toP30 = seq1[(pep_pos-3)*3:(pep_pos+10)*3]

		    result =  "|" + str(pep_pos+1) + "|" + seq1_rep + "|" + pep_M3toP10 + "|" +  seq1 + "|" + seq_M9toP30 + "|" + seq_M9toP30[0:3] + "|" +  seq_M9toP30[3:6] + "|" + seq_M9toP30[6:9] + "|" + seq_M9toP30[9:12]                    
		    outputfile.write(result)

	       elif pep in seq2_rep:
		    pep_pos = seq2_rep.find(pep)
		    pep_M3toP10 = seq2_rep[pep_pos-3:pep_pos+10]                                                     
		    seq_M9toP30 = seq2[(pep_pos-3)*3:(pep_pos+10)*3]

		    result =  "|" + str(pep_pos+1) + "|" + seq2_rep + "|" + pep_M3toP10 + "|" +  seq2 + "|" + seq_M9toP30 + "|" + seq_M9toP30[0:3] + "|" +  seq_M9toP30[3:6] + "|" + seq_M9toP30[6:9] + "|" + seq_M9toP30[9:12]                      

		    outputfile.write(result)

	       elif pep in seq3_rep:                       
		    pep_pos = seq3_rep.find(pep)
		    pep_M3toP10 = seq3_rep[pep_pos-3:pep_pos+10]                                                     
		    seq_M9toP30 = seq3[(pep_pos-3)*3:(pep_pos+10)*3]

		    result =  "|" + str(pep_pos+1) + "|" + seq3_rep + "|" + pep_M3toP10 + "|" +  seq3 + "|" + seq_M9toP30 + "|" + seq_M9toP30[0:3] + "|" +  seq_M9toP30[3:6] + "|" + seq_M9toP30[6:9] + "|" + seq_M9toP30[9:12]                      

		    outputfile.write(result)

	       else:
		    result = "No maching frame found"
		    outputfile.write(result)
		    
    newline = "\n"
    outputfile.write(newline)
