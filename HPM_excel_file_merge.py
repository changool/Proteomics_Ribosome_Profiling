import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pylab
import re
from os import listdir
from os.path import isfile, join
from matplotlib import rc
import pandas as pd
import xlsxwriter


if not os.path.exists('merged_file'):
    os.makedirs('merged_file')
intensity_threshold = 5 # Set intensity to put label (0% to 100%)
currentpath = os.getcwd()
masterlist = []
files_in_the_folder = [ f for f in listdir(currentpath) if isfile(join(currentpath,f)) ]
for filenum, filename in enumerate(files_in_the_folder):
 #if 'AAAAAGANLGDR' in filename:
 try:
    inputfile01 = open(filename, 'r')
    title = filename
    title_ls = title.split('_')
    
    # open the file
    df = pd.read_excel(currentpath+'/'+filename,sheetname=0)

    
    # get the first sheet as an object
    #sheet1 = xlsx.parse(0)
    
    # get the first column as a list you can loop through
    ## where the is 0 in the code below change to the row or column number you want    
    #column = sheet1.icol(0).real
    #
    ## get the first row as a list you can loop through
    #row = sheet1.irow(0).real
    origin = title_ls[0] + '_' + title_ls[1]
    total_rows=len(df.axes[0])
    templist = []
    for xx in range(total_rows):
        templist.append(origin)
    
    col1 = pd.Series(templist,name = 'Origin')
    df['Origin'] = col1
    masterlist.append(df)
 except:
     print 'error for', filename
     continue


df_con = pd.concat(masterlist)
df_con.to_csv('merged.txt',sep='\t')
