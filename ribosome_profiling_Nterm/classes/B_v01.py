#!/usr/bin/python
class class_b: # Fetch chromosome coordinate for mRNA sequences

    def __init__(self,x):
        self.x = x
    
    def a(self):
        import sys
        from Bio.Seq import Seq
        from Bio import SeqIO
        inputlist1 = self.x
        outputlist = []
        outputfile = open('chrom_coor_for_mRNA.txt','w')
	for num, x in enumerate(inputlist1): #rna sequence containing file
	   if num%50 == 0:
	      print num
	   x_ls = x.split('@')
	   header = x_ls[0]
	   mrnaseq = x_ls[1]
	   header_ls = header.split(" ")
	   mrnaacc0 = header_ls[0]
	   chro_strand_ls = header_ls[2].split("|")
	   strand = chro_strand_ls[2]
	   chromo_ls = chro_strand_ls[0].split(":")
	   chromo = chromo_ls[1].strip()
	   cds_ls = header_ls[1].split("=")
	   start_stop_ls = cds_ls[1].split("-")
	   start = int(start_stop_ls[0])
	   stop = int(start_stop_ls[1])
	   exon_info_ls = header_ls[3].split(':')
	   exon_ls = exon_info_ls[1].split(',')
	   mrnaseq_utr_cds = mrnaseq[0:stop]
	   coor_list = []
	   if strand == "+":
	       for i in exon_ls:
		   coor_st_sp = i.split('-')
		   coor_st = int(coor_st_sp[0])
		   coor_sp = int(coor_st_sp[1])
		   for ii in range(coor_st, coor_sp+1):
		       coor_list.append(ii)   

	   elif strand == "-":
	       for i in exon_ls:
		   coor_st_sp = i.split('-')
		   coor_st = int(coor_st_sp[0])
		   coor_sp = int(coor_st_sp[1])
		   for ii in range(coor_st, coor_sp+1):
		       coor_list.append(ii)   
	       coor_list = coor_list[::-1]
	      

	   for num1, nu1 in enumerate(mrnaseq_utr_cds):
	      if num1 > 0 and num1 < len(mrnaseq_utr_cds)-1:
               	    cu_codon = mrnaseq_utr_cds[num1 - 1] + nu1 + mrnaseq_utr_cds[num1 + 1]
		    if len(cu_codon) == 3:
		       aa = Seq(cu_codon).translate()
		    else:
		       aa = " "
	      else:
		 aa = " "
	      
	      if (num1+1) < start or (num1+1) > stop:
		  nu1 = nu1.lower()
	      else:
	          nu1 = nu1.upper()
		  
	      result = [mrnaacc0, str(num1 + 1), nu1, str(aa), chromo, str(coor_list[num1]), strand]
	      result_join = "\t".join(result)
	      outputlist.append(result_join)
	      outputfile.write(result_join + '\n')
	    
	   if len(mrnaseq_utr_cds) != len(coor_list[0:stop]):
		print "mRNA sequence length is not the same as coordinate length for",mrnaacc0

        return outputlist