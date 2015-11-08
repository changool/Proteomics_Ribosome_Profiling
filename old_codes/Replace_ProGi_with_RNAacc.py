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
for num, x in enumerate(inputfile1):
     xstrip = x.strip()
#     if num%1000 == 0:
#        print num
     xlist = xstrip.split("\t")
     rnaacc = xlist[3].strip()
     progi = xlist[6].strip()
     dic[progi] = rnaacc
for num1, y in enumerate(inputfile2):
     ystrip = y.strip()
     if num1%100 == 0:
        print num1
     ylist = ystrip.split("|")
     gi1 = ylist[0]
     pep = ylist[1]
     for k,v in dic.iteritems():
       
        if k.strip() == gi1:
           result = v.strip() 
           outputfile.write(result)
#           print result    	   
           break
       
     result1 = "|" + pep + "\n"    
     outputfile.write(result1)
