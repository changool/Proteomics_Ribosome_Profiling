#!/usr/bin/python
import sys

inputfile1 = open (sys.argv[1],'r')
outputfile = open (sys.argv[2],'w')

for num, x in enumerate(inputfile1):
     if num%10000 == 0:
         print num
     taxo = x.split("\t")
     if taxo[0] == str(562):#mouse:10090, human:9606, Ecoli: 562
        outputfile.write(x)

