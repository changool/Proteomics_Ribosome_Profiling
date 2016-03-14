# This code will return files ends with a certain string in a dirctory
import os
import datetime
#import sys


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)
   
#dirpath = "G:\Chan_Documents\N-term_pep\HPM_unmatched_spectra"
dirpath = "G:\Chan_Documents\N-term_pep\HPM_unmatched_spectra\HPM_unmatched_spectra_UTR_ORF\exported_txt_files2"
extention_name = ".txt"
outputfilename = "all.txt"
outputfile = open(dirpath + '\\' + outputfilename,'w')

for name in os.listdir(dirpath):
    if name.endswith(extention_name) and name != outputfilename:
        pathname = dirpath +'\\'+ name
        inputfile = open(pathname, 'r')
        print name
        for num, x in enumerate(inputfile):
            result = x.strip() + '\t' + name + '\n'
#            if num%100 == 0:
            outputfile.write(result)

#        d = modification_date(pathname)
#        print name
#        print d
        