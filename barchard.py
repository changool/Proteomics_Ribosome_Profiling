import numpy as np
import matplotlib.pyplot as plt
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
#import argparse
#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')
#args = parser.parse_args()
#shellinput = raw_input('Please type your input file name!\n')
inputfile1 = open (sys.argv[1], 'r')
#inputfile2 = open (sys.argv[2], 'r')
#outputfile = open (sys.argv[3], 'w')

app_aa = []
app_ribo = []
app_psm = []
for x in inputfile1:
   x_ls = x.split("\t")
   if x_ls[0] == "NM_001145797":
      st = 170
      ed = 200
      acc = x_ls[0].strip()
      aa = x_ls[3].strip()
      ribo = int(x_ls[7].strip())
      psm = int(x_ls[8].strip())
      app_aa.append(aa)
      app_ribo.append(ribo)
      app_psm.append(psm)
      app_aa_cut = app_aa[st:ed]
      app_ribo_cut = app_ribo[st:ed]
      app_psm_cut = app_psm[st:ed]

      xlength = len(app_psm_cut)

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = xlength
riboMeans = app_ribo_cut
riboStd =   [0 for i1 in range(1,xlength + 1)]
psmMeans = app_psm_cut
psmStd =   [0 for i2 in range(1,xlength + 1)]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.1                      # the width of the bars

## the bars
rects1 = ax.bar(ind, riboMeans, width,
                color='blue',
                yerr=riboStd,
                error_kw=dict(elinewidth=0,ecolor='black'))

rects2 = ax.bar(ind+width, psmMeans, width,
                    color='red',
                    yerr=psmStd,
                    error_kw=dict(elinewidth=2,ecolor='black'))

# axes and labels
ax.set_xlim(0,ind+width)
ax.set_ylim(0,45)
ax.set_ylabel('read/psm')
ax.set_title('RiboSeq and N-term pep')
xTickMarks = app_aa
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=10)

## add a legend
ax.legend( (rects1[0], rects2[0]), ('RiboSeq', 'Peptide') )

plt.show()
