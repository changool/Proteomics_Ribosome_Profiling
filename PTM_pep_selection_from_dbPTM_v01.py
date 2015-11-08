#!/usr/bin/python
import sys

inputfile1 = open (sys.argv[1], 'r')
outputfile = open (sys.argv[2], 'w')

inputlist = []
for num1, x in enumerate(inputfile1): # convert file to a list
    if num1 != 0:
        inputlist.append(x.strip())
    
inputlist1 = []    
for y in inputlist: # Make a list for Modifications
    y_ls = y.split('\t')
    inputlist1.append(y_ls[3])

ptmlist = list(set(inputlist1))

for num, z in enumerate(ptmlist): # Iterate for PTM list
    dic = {}
    for zz in inputlist: # Select item that include right PTM
       zz_ls = zz.split("\t")
       if zz_ls[3] == z:
           dic[zz_ls[0]] = int(zz_ls[1])
    maxptm = max(dic,key=dic.get) # Select items with maximum position
    maxnum = dic.get(maxptm)
    outputfile.write(maxptm + '\t' + str(maxnum) + '\n')    
            
        