#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

inputfile1 = open(sys.argv[1],'r')
outputfile = open(sys.argv[2],'w')


for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
    header = x.description
    headerlist = header.split(" ")
    acce = headerlist[0].replace("hg19_refGene_","")
    accelist = acce.split("_")
    nmnr = accelist[0].strip()
    if "NR" not in nmnr:
	    mrnaseq = str(x.seq).strip()
	    for num1, char in enumerate(mrnaseq):
	       if char == char.upper():
		  upperpos = num1
		  break
	    utr = mrnaseq[:upperpos + 15] # Take down to 5 aa downstream of start site
            nu16 = mrnaseq[upperpos + 15]
            nu17 = mrnaseq[upperpos + 16]
	    if num%200 == 0:
	       print num
	    
	    if len(utr)%3 == 0:
	       utrcut = utr
	    elif len(utr)%3 == 1:
	       utrcut = utr[1:]
	    elif len(utr)%3 == 2:
	       utrcut = utr[2:]

            frame1 = utrcut
            frame2 = utrcut[1:] + nu16
            frame3 = utrcut[2:] + nu16 + nu17
            
	    seq_trans1 = str(Seq(frame1).translate().strip())
	    seq_trans2 = str(Seq(frame2).translate().strip())
	    seq_trans3 = str(Seq(frame3).translate().strip())
	    seq_split1 = seq_trans1.split("*")
	    seq_split2 = seq_trans2.split("*")
	    seq_split3 = seq_trans3.split("*")
 
            for num10, u_orf in enumerate(reversed(seq_split1)):
               if len(u_orf) >= 6:
	          result = ">" + acce +  "_frame1_uORF" + "-" + str(num10+1) + "|" + "frame1_uORF" + "-" + str(num10+1) + "_" + headerlist[0] + "\n" + u_orf + "\n"
	          outputfile.write(result)
                  
            for num10, u_orf in enumerate(reversed(seq_split2)):
               if len(u_orf) >= 6:
	          result = ">" + acce +  "_frame2_uORF" + "-" + str(num10+1) + "|" + "frame2_uORF" + "-" + str(num10+1) + "_" + headerlist[0] + "\n" + u_orf + "\n"
	          outputfile.write(result)

            for num10, u_orf in enumerate(reversed(seq_split3)):
               if len(u_orf) >= 6:
	          result = ">" + acce +  "_frame3_uORF" + "-" + str(num10+1) + "|" + "frame3_uORF" + "-" + str(num10+1) + "_" + headerlist[0] + "\n" + u_orf + "\n"
	          outputfile.write(result)





