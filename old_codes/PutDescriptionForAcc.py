#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

shellinput1 = str(sys.argv[1])
shellinput2 = str(sys.argv[2])
inputfile1 = open (shellinput1, 'r')
inputfile2 = open (shellinput2, 'r')
shelloutput = str(sys.argv[3])
outputfile = open (shelloutput,'w')

dic = {}
for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")):
     header = x.description
     pro = str(x.seq)

     header_sp = header.split("|")
     acc = header_sp[3].strip()

     dic[acc] = header

for num, x in enumerate(inputfile2):
     rnapro = x.split("@")
     pro = rnapro[1].strip()
     if num%1000 == 0:
       print num
     for k,v in dic.iteritems():
         if k == pro:
             result = x.strip() + "@" + v + "\n"
             outputfile.write(result)
   
