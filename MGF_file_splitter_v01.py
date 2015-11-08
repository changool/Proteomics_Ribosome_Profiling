#!/usr/bin/python

import sys

inputfile01 = open(sys.argv[1],'r')
inputfilename = sys.argv[1]
outputfile1 = open(inputfilename+"_1",'w')
outputfile2 = open(inputfilename+"_2",'w')
outputfile3 = open(inputfilename+"_3",'w')
outputfile4 = open(inputfilename+"_4",'w')
outputfile5 = open(inputfilename+"_5",'w')

split_n = float(5)

outputfile1.write("MASS=Monoisotopic"+"\n")
outputfile2.write("MASS=Monoisotopic"+"\n")
outputfile3.write("MASS=Monoisotopic"+"\n")
outputfile4.write("MASS=Monoisotopic"+"\n")
outputfile5.write("MASS=Monoisotopic"+"\n")

i = 0
for x in inputfile01:
    if x.strip() == 'BEGIN IONS':
        i += 1
inputfile01.seek(0)

ii = 0
for num, y in enumerate(inputfile01):

    if num > 0:  
        if ii < i*(1/split_n):
            outputfile1.write(y)
        elif ii >= i*(1/split_n) and ii < i*(2/split_n):
            outputfile2.write(y)
        elif ii >= i*(2/split_n) and ii < i*(3/split_n):
            outputfile3.write(y)
        elif ii >= i*(3/split_n) and ii < i*(4/split_n):
            outputfile4.write(y)
        elif ii >= i*(4/split_n):
            outputfile5.write(y)
    if 'END IONS' in y:
        ii += 1

print inputfilename, i, ii