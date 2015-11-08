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

dic = {}
for num, y in enumerate(SeqIO.parse(inputfile1,"fasta")):
     header1 = y.description
     pro1 = str(y.seq)
     dic[pro1] = header1

newlist = []
sortedlist = sorted(dic, key=len, reverse = True)
print pro1
print dic[pro1]
i = 0
for pro,header in sortedlist.iteritems():
     i += 1
     if i%1000 == 0:
        print num
     joinstr = " "
     newlistread = joinstr.join(newlist)
     if pro not in newlistread:
        result = ">" + header + "\n" + pro + "\n"
        newlist.append(result)
#print newlist
for y in newlist:
   
     outputfile.write(y)
   
