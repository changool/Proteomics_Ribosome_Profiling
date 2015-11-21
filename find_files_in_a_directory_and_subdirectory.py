# This code will return files ends with a certain string in a dirctory
import os
import os.path
import datetime
import sys



def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)
   
#dirpath = "H:\Elite Data Back UP"
dirpath = "E:\Elite Data Back UP"
extention_name = ".raw"
outputfilename = "summary.txt"
outputfile = open(dirpath + '\\' + outputfilename, 'w')

head = "file path" + '\t' + "file name" + '\t' + "file size (byte)" + '\t' + "generated date and time" + '\n'
outputfile.write(head)
for dirpath, dirnames, filenames in os.walk(dirpath):
    for filename in [f for f in filenames if f.endswith(extention_name) and f != outputfilename]:
        pathname = os.path.join(dirpath, filename)
        filesize = os.path.getsize(pathname)
        d = modification_date(pathname)
#        print pathname
#        print filename
#        print d
        result = pathname + '\t' + filename + "\t" + str(filesize) + '\t' + str(d) + '\n'
        outputfile.write(result)