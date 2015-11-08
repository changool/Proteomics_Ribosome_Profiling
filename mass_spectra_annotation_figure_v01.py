import numpy as np
import matplotlib.pyplot as plt
from matplotlib.table import Cell
import sys
import os
import pylab

inputfile01 = open(sys.argv[1],'r')
ft = str(sys.argv[1])
fig_ls = ft.split("/")
fig_title = fig_ls[len(fig_ls)-1]

numlist = [];masslist = [];intenlist = [];annolist = []
for num, x in enumerate(inputfile01):
    if 'm/z' not in x:
        x_st  = x.strip()
        x_sp  = x_st.split('\t')
        if len(x_sp) == 3:
            number= num + 1; numlist.append(number)
            mass  = float(x_sp[0]); masslist.append(mass)
            inten = float(x_sp[1]); intenlist.append(inten)
            anno  = x_sp[2]; annolist.append(anno)
    
            #N = len(numlist)
            #xlocation = range(int(min(masslist)),int(max(masslist)))
            #bar_width = 0
   					
fig, ax = plt.subplots(figsize = (10,5))
ax.plot(masslist,intenlist)
ax.set_ylabel('Relative intensity')
ax.set_xlabel('m/z')
ax.set_title(fig_title, fontsize = 10, y = 1.1)
#ax.xaxis.set_visible(False)
plt.subplots_adjust(top=0.8)
plt.subplots_adjust(bottom=0.1)
plt.show()
exit()
    
currentpath = os.getcwd()
path = currentpath + '/' + fig_title + '.png'
print number, path
plt.axis("tight")
plt.margins(0,0)
plt.xticks(xlocation, xlocation, rotation = 'vertical', fontsize = 1)
 
fig.savefig(path, format = 'png', dpi = 600)
plt.close()
#exit()


