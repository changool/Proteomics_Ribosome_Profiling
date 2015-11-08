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


     acc = x.split("\t")
     if len(acc) >= 16:
	     result = acc[3].strip() + "@" +  acc[4].strip() + "@" + acc[5].strip() + "@" + acc[6].strip() + "@" + acc[15].strip() + "\n"     
   	     outputfile.write(result)
	#     print header1
