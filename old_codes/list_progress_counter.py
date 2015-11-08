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

linenum = sum(1 for line in inputfile1)
inputfile1.seek(0)
print "Total item number is " + str(linenum)
progress1 = 0
inputfile1 = open (shellinput1, 'r')
for num, x in enumerate(inputfile1):
     progress = round(100*num/linenum,0)
     if progress > progress1:
        progress1 = progress 
        print str(round(progress1,0)) + " %"

     taxo = x.split("\t")
     taxo0 = taxo[0].strip()
     
     if taxo0 == str(10090):#mouse:10090, human:9606
#        print taxo0
       
        outputfile.write(x)
#     print header1
