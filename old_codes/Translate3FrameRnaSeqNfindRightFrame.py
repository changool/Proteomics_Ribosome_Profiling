#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
#import argparse

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

#shellinput = raw_input('Please type your input file name!\n')
shellinput1 = str(sys.argv[1])
shellinput2 = str(sys.argv[2])
inputfile1 = open (shellinput1, 'r')
inputfile2 = open (shellinput2, 'r')
#shelloutput = raw_input('Please type your output file name for over100\n')
#shelloutput =str(sys.argv[2])
#maxsize = input('please type the AA length cutoff \n')
#maxsizenumber = str(maxsize)
#shelloutput = str( 'over' + maxsizenumber + '.txt')
shelloutput = str(sys.argv[3])
#oversizelimit = open (shelloutput,'w')
outputfile = open (shelloutput,'w')
#import temfile

#pep = open ('peptide.txt', 'w')
#length = open ('peptide_len.txt', 'w')
#result = open ('output.txt', 'w')
#rightsize = 0
#small = 0
#big = 0
#total = 0
#bigger_than_sizelimit = 0
dic = {}
for x in inputfile1: #rna sequence containing file
   x_strip = x.strip()
   x_split = x_strip.split("|")
   gi1 = x_split[0].strip()
   macc = x_split[1].strip()
   mrna = x_split[2].strip()
   macc_mrna = macc + "|" + mrna
   dic[gi1] = macc_mrna

for y in inputfile2: #peptide containing file

            y_strip = y.strip() 
            y_split = y_strip.split("|")
            gi2 = y_split[0].strip()
            pep = y_split[1].strip()

            for z in dic.keys():
                z_strip = z.strip()
                if gi2 == z_strip:
                       value = dic.get(z)
                       value_strip = value.strip()
                       
                       value_split = value_strip.split("|")      
                       mrna3frame = value_split[1].strip()
                       seq123_split = mrna3frame.split("#")
                       seq1 = seq123_split[0].strip()
                       seq2 = seq123_split[1].strip() 
		       seq3 = seq123_split[2].strip() 

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
                       
                       if pep in seq1_rep:                            
                            pep_pos = seq1_rep.find(pep)
                            pep_M3toP10 = seq1_rep[pep_pos-3:pep_pos+10]                                                    
                            seq_M9toP30 = seq1[(pep_pos-3)*3:(pep_pos+10)*3]

                            result =  z_strip + "|" + pep + "|" + str(pep_pos+1) + "|" + seq1_rep + "|" + pep_M3toP10 + "|" +  seq1 + "|" + seq_M9toP30   + "\n"                       
                            outputfile.write(result)

                       elif pep in seq2_rep:
                            pep_pos = seq2_rep.find(pep)
                            pep_M3toP10 = seq2_rep[pep_pos-3:pep_pos+10]                                                     
                            seq_M9toP30 = seq2[(pep_pos-3)*3:(pep_pos+10)*3]

                            result =  z_strip + "|" + pep + "|" + str(pep_pos+1) + "|" + seq2_rep + "|" + pep_M3toP10 + "|" +  seq2 + "|" + seq_M9toP30   + "\n"                       

                            outputfile.write(result)

                       elif pep in seq3_rep:                       
                            pep_pos = seq3_rep.find(pep)
                            pep_M3toP10 = seq3_rep[pep_pos-3:pep_pos+10]                                                     
                            seq_M9toP30 = seq3[(pep_pos-3)*3:(pep_pos+10)*3]

                            result =  z_strip + "|" + pep + "|" + str(pep_pos+1) + "|" + seq3_rep + "|" + pep_M3toP10 + "|" +  seq3 + "|" + seq_M9toP30   + "\n"                       

                            outputfile.write(result)

                       else:
                            result = "No maching frame found"
                            outputfile.write(result)
                            
 
