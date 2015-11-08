#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
from Bio.Seq import Seq
from Bio import SeqIO
import re

inputfile1 = open(sys.argv[1],'r')
outputfile = open(sys.argv[2],'w')

def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]
    
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")): #rna sequence containing file
    if num%1000 == 0: print num
    header = x.description
    headerlist = header.split(" ")
    acce = headerlist[0]
    if "NR" not in acce and acce.count("_") < 2 and "CDS=" in headerlist[1]:
            cds = headerlist[1]
            cdsre = re.findall("CDS=(.*)-",cds)
            startsite = int(cdsre[0])
            mrnaseq = str(x.seq).upper()
	    utr = mrnaseq[:startsite + 15] # Take down to 5 aa downstream of start site
            nu16 = mrnaseq[startsite + 15]
            nu17 = mrnaseq[startsite + 16]
    
	    if len(utr)%3 == 0:
	       utrcut = utr
	    elif len(utr)%3 == 1:
	       utrcut = utr[1:]
	    elif len(utr)%3 == 2:
	       utrcut = utr[2:]

            frame1 = utrcut
            frame2 = utrcut[1:] + nu16
            frame3 = utrcut[2:] + nu16 + nu17

            codontoswitch = "ACG"
  
 	    codon1 = split(frame1,3)
            frame1_rep = ''
            for z1 in codon1:
               if z1.upper() == codontoswitch:
                   z1 = "ATG"
	           frame1_rep = frame1_rep + z1
               else:
                   frame1_rep = frame1_rep + z1
 
  	    codon2 = split(frame2,3)
            frame2_rep = ''
            for z2 in codon2:
               if z2.upper() == codontoswitch:
                   z2 = "ATG"
	           frame2_rep = frame2_rep + z2
               else:
                   frame2_rep = frame2_rep + z2
                   
       	    codon3 = split(frame3,3)
            frame3_rep = ''
            for z3 in codon3:
               if z3.upper() == codontoswitch:
                   z3 = "ATG"
	           frame3_rep = frame3_rep + z3
               else:
                   frame3_rep = frame3_rep + z3                                 
                                                                                                    
	    seq_trans1 = str(Seq(frame1_rep).translate().strip())
	    seq_trans2 = str(Seq(frame2_rep).translate().strip())
	    seq_trans3 = str(Seq(frame3_rep).translate().strip())
	    seq_split1 = seq_trans1.split("*")
	    seq_split2 = seq_trans2.split("*")
	    seq_split3 = seq_trans3.split("*")
	    

 
            for num10, u_orf in enumerate(reversed(seq_split1)):
               if len(u_orf) >= 6:
	          result = ">" + acce +  "_frame1_UTR_" + codontoswitch  + "-" + str(num10+1) + "|ref|"+ acce +  "_frame1_UTR_" + codontoswitch + "-" + str(num10+1) + "| " + "frame1_UTR_" + codontoswitch + "-" + str(num10+1) + "_" + headerlist[0] + "\n" + u_orf + "\n"
	          outputfile.write(result)
                  
            for num10, u_orf in enumerate(reversed(seq_split2)):
               if len(u_orf) >= 6:
	          result = ">" + acce +  "_frame2_UTR_" + codontoswitch + "-" + str(num10+1) + "|ref|"+ acce +  "_frame2_UTR_" + codontoswitch + "-" + str(num10+1) + "| " + "frame2_UTR_" + codontoswitch + "-" + str(num10+1) + "_" + headerlist[0] + "\n" + u_orf + "\n"

            for num10, u_orf in enumerate(reversed(seq_split3)):
               if len(u_orf) >= 6:
	          result = ">" + acce +  "_frame3_UTR_" + codontoswitch + "-" + str(num10+1) + "|ref|"+ acce +  "_frame3_UTR_" + codontoswitch + "-" + str(num10+1) + "| " + "frame3_UTR_" + codontoswitch + "-" + str(num10+1) + "_" + headerlist[0] + "\n" + u_orf + "\n"
	          outputfile.write(result)





