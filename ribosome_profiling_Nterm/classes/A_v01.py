#!/usr/bin/python
class class_a:# Fetch fasta sequence for mRNA asscession pertaining to acetylated peptides
    
   def __init__(self, x, y):
       self.x = x
       self.y = y
   def a(self):
      outputfile = open('peptide_that_failed_in_fetching_mRNA_seq.txt','w')
      outputfile1 = open('corresponding_fasta_to_pep.fasta','w')
      inputlist1 = self.x
      inputlist2 = self.y
      outputlist = []
      dic = {}
      for num, x in enumerate(inputlist1): #rnaseq containing file generated by gffread with chromosome coordinate for each exons
         x_ls = x.split('@')
         header_ls = x_ls[0].split(" ")         
         mrnaacc0 = header_ls[0]
         if "_" not in header_ls[2] and "NR_" not in mrnaacc0:
            dic[mrnaacc0] = x

      for num1, y in enumerate(inputlist2): # mRNA accession|Pepseq|PSM
           if num1%100 == 0:
              print num1
           y_ls = y.strip().split("|")
           y0 = y_ls[0]
           v = dic.get(y0)
           if v == None:
               outputfile.write(y + '\n')
           else:
               outputlist.append(v)
               rep_v = v.replace("@","\n")
               outputfile1.write(rep_v + '\n')
   
      return outputlist