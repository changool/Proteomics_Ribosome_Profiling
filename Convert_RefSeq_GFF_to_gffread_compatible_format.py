#!/usr/bin/python
import sys
import re

# python *.py [gff file] [Outputfile]

inputfile1 = open (sys.argv[1], 'r')
outputfile = open (sys.argv[2], 'w')

for num, x in enumerate(inputfile1): # Input file
     if num%10000 == 0:
        print num
     x_st = x.strip()
     x_ls = x_st.split('\t')
     if len(x_ls) >= 9:
        ids = x_ls[8]
        tranid = re.findall("Genbank:(.*?),"    ,ids)
        if len(tranid) == 0:
           tranid = re.findall("Genbank:(.*?);" ,ids) 
        geneid = re.findall("(gene=.*?);"       ,ids)
        if len(tranid) == 0:
            tranid0 = 'transcript_id=empty'
        else:
            tranid0 = 'transcript_id=' + tranid[0]
        if len(geneid) == 0:
            geneid0 = "gene=empty"
        else:
            geneid0 = geneid[0]
        trangene = tranid0 + ';' + geneid0
        ls = [x_ls[0],x_ls[1],x_ls[2],x_ls[3],x_ls[4],x_ls[5],x_ls[6],x_ls[7],trangene]
        joinls = '\t'.join(ls)
        outputfile.write(joinls + '\n')
     else:
        outputfile.write(x_st + '\n')