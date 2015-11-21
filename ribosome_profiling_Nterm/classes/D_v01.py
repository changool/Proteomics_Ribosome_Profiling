	#!/usr/bin/python
	# This code extract gi_accession number, protein sequence and length information from fasta database
class class_d: # Find peptide position in mRNA

    def __init__(self,x,y):
        self.x = x
        self.y = y    
    def a(self):
        import sys
        from Bio.Seq import Seq
        from Bio import SeqIO
        import re
        
        inputlist1 = self.x
        inputlist2 = self.y

	outputfile = open ('pep_pos_in_mRNA.txt', 'w')
        outputlist = []

	dic ={}
	for num, x in enumerate(inputlist1): #rna sequence containing file
	    x_ls = x.split('@')
	    header1 = x_ls[0]
	    header1_ls = header1.split(" ")
	    mrnaacc1 = header1_ls[0]
	    dic[mrnaacc1] = x


	for num_y, y in enumerate(inputlist2):# RNA acce|Pepseq|PSM
	   if num_y%100 == 0:
	       print num_y
	   y_st = y.strip()
	   y_ls = y_st.split("|")
	   mrnaacc10 = y_ls[0].strip()
	   pepseq10 = y_ls[1].strip()
	   psm10 = y_ls[2].strip()
	   v = dic.get(mrnaacc10)
	   if v != None:

		   v_ls = v.split('@')
		   mrnaseq = v_ls[1].strip()
		   chrom1 = re.findall('loc:(.*?)\|',v_ls[0])
		   chrom3 = chrom1[0]
			      
		   if len(mrnaseq)%3 == 0:
		       mrnaseq1 = mrnaseq.upper()
		   
		   elif len(mrnaseq)%3 == 1:
		       mrnaseq1 = mrnaseq.upper() + "NN"
	     
		   elif len(mrnaseq)%3 == 2:
		       mrnaseq1 = mrnaseq.upper() + "N"

		   f1 = Seq(mrnaseq1).translate()
		   f2 = Seq(mrnaseq1[1:-2]).translate()
		   f3 = Seq(mrnaseq1[2:-1]).translate()

		   if pepseq10 in f1:
		       pepstpos = (f1.find(pepseq10) + 1)*3 -2  # 1st nucleotide of codon
	   
		   elif pepseq10 in f2:
		       pepstpos = (f2.find(pepseq10) + 1)*3 -2 + 1

		   elif pepseq10 in f3:
		       pepstpos = (f3.find(pepseq10) + 1)*3 -2 + 2
		       
		   if pepstpos >= 0:
	     	       pepsppos = pepstpos + (len(pepseq10)-1)*3
		       while pepstpos <= pepsppos:
		          result = chrom3 + '\t' + mrnaacc10 + "\t" + pepseq10 +"\t"+ str(pepstpos) + "\t" + str(psm10)
		          outputlist.append(result)
		          outputfile.write(result + '\n')
		          pepstpos += 1
	

        return outputlist

