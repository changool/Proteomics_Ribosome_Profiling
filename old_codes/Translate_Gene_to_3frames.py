#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
#import argparse

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

#shellinput = raw_input('Please type your input file name!\n')
shellinput1 = str(sys.argv[1])
#shellinput2 = str(sys.argv[2])
inputfile1 = open (shellinput1, 'r')
#inputfile2 = open (shellinput2, 'r')
#shelloutput = raw_input('Please type your output file name for over100\n')
#shelloutput =str(sys.argv[2])
#maxsize = input('please type the AA length cutoff \n')
#maxsizenumber = str(maxsize)
#shelloutput = str( 'over' + maxsizenumber + '.txt')
shelloutput = str(sys.argv[2])
#oversizelimit = open (shelloutput,'w')
outputfile = open (shelloutput,'w')
#import temfile

for n, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #peptide containing file

	head = x.description
        rna = str(x.seq)
        frame1 = rna
        frame2 = rna[1:]
        frame3 = rna[2:]
        
        if len(frame1)%3 == 0:
	   frame1_mod = frame1
        elif len(frame1)%3 ==1:
	   frame1_mod = frame1 + "NN"
        else:
	   frame1_mod = frame1 + "N"
	       
        if len(frame2)%3 == 0:
	   frame2_mod = frame2
        elif len(frame2)%3 ==1:
	   frame2_mod = frame2 + "NN"
        else:
	   frame2_mod = frame2 + "N"

        if len(frame3)%3 == 0:
	   frame3_mod = frame3
        elif len(frame3)%3 ==1:
	   frame3_mod = frame3 + "NN"
        else:
	   frame3_mod = frame3 + "N"

        frame1_per = Seq(frame1_mod)
        frame2_per = Seq(frame2_mod)
        frame3_per = Seq(frame3_mod)

        frame1_trans = frame1_per.translate()
        frame2_trans = frame2_per.translate()
        frame3_trans = frame3_per.translate()
           
        pep1 = str(frame1_trans.strip())
        pep2 = str(frame2_trans.strip())
        pep3 = str(frame3_trans.strip())
		       
        pep01 = pep1.replace("*","^")
        pep02 = pep2.replace("*","^")
        pep03 = pep3.replace("*","^")
             
        pep01_sp = pep01.split("^")       
        pep02_sp = pep02.split("^")       
        pep03_sp = pep03.split("^")       
        		      
        for num1, y1 in enumerate(pep01_sp):
           if len(y1) > 20:
               result1 = ">"+"frame1"+"|"+"stop_to_stop_"+str(num1)+"|"+head+"\n"+y1+"\n"
               outputfile.write(result1)

        for num2, y2 in enumerate(pep02_sp):
           if len(y2) > 20:
               result2 = ">"+"frame2"+"|"+"stop_to_stop_"+str(num2)+"|"+head+"\n"+y2+"\n"
               outputfile.write(result2)

        for num3, y3 in enumerate(pep03_sp):
           if len(y3) > 20:
               result3 = ">"+"frame3"+"|"+"stop_to_stop_"+str(num3)+"|"+head+"\n"+y3+"\n"
               outputfile.write(result3)
        
        n1 = str(n) + "\r"
        sys.stdout.write(n1)
        sys.stdout.flush()
