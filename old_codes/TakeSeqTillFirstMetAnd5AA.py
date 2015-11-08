#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

shellinput1 = str(sys.argv[1])
#shellinput2 = str(sys.argv[2])
inputfile1 = open (shellinput1, 'r')
#inputfile2 = open (shellinput2, 'r')
shelloutput = str(sys.argv[2])
outputfile = open (shelloutput,'w')

newlist = []
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")):
     if num%1000 == 0:
        print num
     header = x.description
     pro = str(x.seq)
     mpos = pro.find("M")
     nterm = pro[:mpos+5]
     if len(nterm) > 5:
        result = ">" + header + "\n" + nterm + "\n"
   
        outputfile.write(result)
