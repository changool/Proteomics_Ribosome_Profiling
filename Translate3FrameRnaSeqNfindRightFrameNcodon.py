#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
#import argparse
#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')
#args = parser.parse_args()
#shellinput = raw_input('Please type your input file name!\n')
inputfile1 = open (sys.argv[1], 'r')
inputfile2 = open (sys.argv[2], 'r')
outputfile = open (sys.argv[3], 'w')

dic = {}
for x in SeqIO.parse(inputfile1,"fasta"): #rna sequence fast format database
   header = x.description
   mrnaseq = str(x.seq)
   headersplit = header.split("|")
#   headersplit = header.split(" ")
#   mrnaacce = headersplit[3].split(".")
#   mrnaacce0 = mrnaacce[0].strip()
#   mrnaacce0 = headersplit[0].replace("hg19_refGene_","")
   mrnaacce = headersplit[3].split('.')
   mrnaacce0 = mrnaacce[0]
   dic[mrnaacce0] = mrnaseq


head = 'mRNA accession'+ "|"+ 'peptide sequence' + "|" + 'mRNA accession' + "|" + 'peptide sequence' + "|" + 'peptide position from the mRNA start pos' + "|" + 'translated protein seq' + "|" + 'peptide seq from -3 to 10' + "|" + 'mRNA sequence' + "|" + 'mRNA sequence from -9 to 30' + "|" + 'mRNA seq from -9 to -7' + "|" +  'mRNA sequence from -6 to -4' + "|" + 'mRNA seq from -3 to -1' + "|" + 'mRNA seq from 1 to 3' + '\n'                    
outputfile.write(head)

for num, y in enumerate(inputfile2): #mRNA_accession|peptide
    if num%200 == 0:
       print num
    y_strip = y.strip()
    inputinfo = y_strip + "|" 
    outputfile.write(inputinfo)
    y_split = y_strip.split("|")
    mrnaacce1 = y_split[0].split(".")
    mrnaacce2 = mrnaacce1[0].strip()
    pep = y_split[1].strip()
    v = dic.get(mrnaacce2)
    if v != None:
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
	       
	       result0 = mrnaacce2 + "|" + pep
	       outputfile.write(result0)

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
		    result = "|No maching frame found"
		    outputfile.write(result)
		    
    newline = "\n"
    outputfile.write(newline)
