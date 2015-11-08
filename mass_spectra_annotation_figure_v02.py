import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pylab
import re

inputfile01 = open(sys.argv[1],'r')
ft = str(sys.argv[1])
fig_ls = ft.split("/")
fig_title = fig_ls[len(fig_ls)-1]

numlist = [];masslist = [];intenlist0 = [];intenlist=[];annolist = []
for num, x in enumerate(inputfile01):
    if 'm/z' not in x:
        x_st  = x.strip()
        x_sp  = x_st.split('\t')
        if len(x_sp) == 3:
            number= num + 1; numlist.append(number)
            mass  = float(x_sp[0]); masslist.append(mass)
            inten = float(x_sp[1]); intenlist0.append(inten)
            intenlist  = [y / max(intenlist0)*100 for y in intenlist0]
            anno  = x_sp[2]; annolist.append(anno)
    

fig = plt.figure(figsize=(12, 6))
plt.vlines(masslist,0,intenlist)
plt.xlabel('m/z')
plt.ylabel('Relative intensity')
plt.gca().get_xaxis().set_tick_params(which='both', direction='out')
plt.gca().get_yaxis().set_tick_params(which='both', direction='out')
for a,b,c in zip(masslist,intenlist,annolist):
    if 'b (' in c or 'y (' in c:
        n0 =re.findall('(\w?)\s\(\d*\)',c)
        n1 =re.findall('\w\s\((\d*?)\)',c)
        n2 =re.findall('\w\s\(\d*\)\s\((.*?)\)',c)
        n3 =re.findall('\w\s\(\d*\)\s\(.*\)(.*)',c)
        ion=n0[0];pos=n1[0];cha=n2[0];der=n3[0]
        peaklabel0='$'+ion+'^{'+cha+'}_{'+pos+'}$'
        if der == '-NH3':
            der = '$-NH_{3}$'
        elif der == '-H2O':
            der = '$-H_{2}O$'
        elif der == '-H3OP4':
            der = '$-H_{3}PO_{4}$'
        peaklabel =peaklabel0+der
        if 'b (' in c:
            txtcolor = 'red'
        elif 'y (' in c:
            txtcolor = 'blue'
        plt.text(a,b,peaklabel,rotation=90,horizontalalignment='center',verticalalignment='bottom',color=txtcolor,size=15)
        #plt.annotate(peaklabel,xy=(a,b),arrowprops=dict(arrowstyle='->'))
plt.title(fig_title)
plt.subplots_adjust(top=0.8)
plt.subplots_adjust(bottom=0.1)
plt.show()
exit()

