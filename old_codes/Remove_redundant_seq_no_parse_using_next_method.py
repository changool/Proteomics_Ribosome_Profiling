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
for num, x in enumerate(inputfile1):
     xstrip = x.strip()
     xnext = inputfile1.next().strip()
     if num%1000 == 0:
        print num
     if xstrip != xnext:
        result = xstrip + "\n"
        outputfile.write(result)
   
