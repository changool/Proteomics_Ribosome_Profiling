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

for num, x in enumerate(inputfile1):
     if num%100000 == 0:
        print num

     acc = x.split("\t")
     rna = acc[3].strip()
     pro = acc[5].strip()
     result = rna + "@" + pro +"\n"     
     if "-" not in result:
         outputfile.write(result)
#     print header1
