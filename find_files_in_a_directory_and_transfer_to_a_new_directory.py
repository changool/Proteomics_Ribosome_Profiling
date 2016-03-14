# This code will return files ends with a certain string in a dirctory
import os
import datetime
import sys
import shutil

inputfile01 = open(sys.argv[1],'r')

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

currentpath = os.getcwd()   
if not os.path.exists('exported_files'):
    os.makedirs('exported_files')

exportpath = currentpath + "/exported_files"

counter = 0

for x in inputfile01: # peptide list    
    for name in os.listdir(currentpath):
        name_ls = name.split('_')
        if x.strip() == name_ls[0]:
            counter += 1
            print counter
            srcfile = currentpath + '/' + name
            shutil.copy(srcfile,exportpath)
