import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pylab
import re

##############################################################################
# This is module part for automatic annotation positioning
def get_text_positions(x_data, y_data, txt_width, txt_height):
    a = zip(y_data, x_data)
    text_positions = y_data.copy()
    for index, (y, x) in enumerate(a):
        local_text_positions = [i for i in a if i[0] > (y - txt_height) 
                            and (abs(i[1] - x) < txt_width * 2) and i != (y,x)]
        if local_text_positions:
            sorted_ltp = sorted(local_text_positions)
            if abs(sorted_ltp[0][0] - y) < txt_height: #True == collision
                differ = np.diff(sorted_ltp, axis=0)
                a[index] = (sorted_ltp[-1][0] + txt_height, a[index][1])
                text_positions[index] = sorted_ltp[-1][0] + txt_height
                for k, (j, m) in enumerate(differ):
                    #j is the vertical distance between words
                    if j > txt_height * 2: #if True then room to fit a word in
                        a[index] = (sorted_ltp[k][0] + txt_height, a[index][1])
                        text_positions[index] = sorted_ltp[k][0] + txt_height
                        break
    return text_positions

def text_plotter(x_data, y_data, text_positions, axis,txt_width,txt_height):
    for x,y,t in zip(x_data, y_data, text_positions):
        axis.text(x - txt_width, 1.01*t, '%d'%int(y),rotation=0, color='blue')
        if y != t:
            axis.arrow(x, t,0,y-t, color='red',alpha=0.3, width=txt_width*0.1, 
                       head_width=txt_width, head_length=txt_height*0.5, 
                       zorder=0,length_includes_head=True)
#################################################################################

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
                                                                     
#random test data:
x_data = random_sample(100)
y_data = random_integers(10,50,(100))

#GOOD PLOT:
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.bar(x_data, y_data,width=0.00001)
#set the bbox for the text. Increase txt_width for wider text.
txt_height = 0.04*(plt.ylim()[1] - plt.ylim()[0])
txt_width = 0.02*(plt.xlim()[1] - plt.xlim()[0])
#Get the corrected text positions, then write the text.
text_positions = get_text_positions(x_data, y_data, txt_width, txt_height)
text_plotter(x_data, y_data, text_positions, ax2, txt_width, txt_height)

plt.ylim(0,max(text_positions)+2*txt_height)
plt.xlim(-0.1,1.1)


plt.show()