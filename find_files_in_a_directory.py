# This code will return files ends with a certain string in a dirctory
import os
import datetime
import sys

inputfile01 = open(sys.argv[1],'r')
def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)
   
#dirpath = "G:\Chan_Documents\N-term_pep\HPM_unmatched_spectra"
dirpath = "C:\Users\Chan-Hyun\VirtualBoxShare\Nterm\JPT_synthetic_pep\synthetic_pep"
extention_name = ".txt"
outputfile = open(dirpath + '\\' + 'all.txt','w')

for name in os.listdir(dirpath):
    if name.endswith(extention_name):
        pathname = dirpath +'\\'+ name
#        name_ls = name.split('_')
#        name01 = name[1] + '_' + name[2]
        inputfile = open(pathname, 'r')
#        for x in inputfile:
#            result = x.strip() + '\t' + name01
#            outputfile.write(result)
#        d = modification_date(pathname)
        print name
#        print d
        