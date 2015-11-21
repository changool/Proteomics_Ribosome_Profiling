	#!/usr/bin/python
class class_c: # Fetch RiboSeq data

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def a(self):
        import sys
        from Bio.Seq import Seq
        from Bio.Alphabet import IUPAC
        from Bio import SeqIO
        import re
        inputlist1 = self.x
        inputlist2 = self.y
        outputlist = []
        outputfile = open ('chromo_coor_riboseq.txt','w')
        totallines = 0
	for zzz in inputlist1:
	   totallines += 1

	dic = {}
	print 'In the middle of dictionary generation'

	for y in inputlist2:# Riboseq data
			 y_ls = y.strip().split("\t")
			 if "#" in y or len(y_ls) != 4:
			    continue
			 chrom2 = y_ls[0].strip()
			 coor5p = int(y_ls[1].strip())
			 coor3p = int(y_ls[2].strip())
			 readnum = int(y_ls[3].strip())

                         while coor5p + 1 == coor3p:
				  chrom_coor = chrom2 + '-' + str(coor5p + 1)
				  dic[chrom_coor] = str(readnum)
				  coor5p += 1


	for num, x in enumerate(inputlist1): #rna and protein sequence and chromosome coordinate
		   if num%10000 == 0:
		      print num, "of", totallines, "lines"

		   x_ls = x.strip().split("\t")
		   chrom1_coor1 = x_ls[4].strip() + '-' + x_ls[5].strip()	   
		   b = dic.get(chrom1_coor1)
		   if b is None: 
			 matchedv = '0' 
		   else: 
			 matchedv = b
				  
		   result = x.strip() + '\t' + str(matchedv)
		   outputlist.append(result)
                   outputfile.write(result + '\n')
        return outputlist   