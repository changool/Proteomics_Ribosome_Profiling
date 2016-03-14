import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pylab
import re
from os import listdir
from os.path import isfile, join
from matplotlib import rc

intensity_threshold = 1 # Set intensity to put label (0% to 100%)
currentpath = os.getcwd()
files_in_the_folder = [ f for f in listdir(currentpath) if isfile(join(currentpath,f)) ]
for filenum, filename in enumerate(files_in_the_folder):
 #if 'AAAAAGANLGDR' in filename:
    inputfile01 = open(filename, 'r')
    fig_title = filename    
    
    numlist = [];masslist = [];intenlist0 = [];intenlist=[];annolist = []
    for num, x in enumerate(inputfile01):
        if 'm/z' not in x:
            x_st  = x.strip()
            x_sp  = x_st.split('\t')
            if len(x_sp) == 3:
                if '[M' not in x_sp[2] and 'Tyr' not in x_sp[2]:#Precursor and Tyr derivative peak will be removed
                    number= num + 1; numlist.append(number)
                    mass  = float(x_sp[0]); masslist.append(mass)
                    inten = float(x_sp[1]); intenlist0.append(inten)
                    intenlist  = [y / max(intenlist0)*100 for y in intenlist0]
                    anno  = x_sp[2].strip(); annolist.append(anno)
            elif len(x_sp) == 2:
                    number= num + 1; numlist.append(number)
                    mass  = float(x_sp[0]); masslist.append(mass)
                    inten = float(x_sp[1]); intenlist0.append(inten)
                    intenlist  = [y / max(intenlist0)*100 for y in intenlist0]
                    anno  = ''; annolist.append(anno)
                
    annolist_new=[]
    for ii,c in zip(intenlist,annolist):
        if ii < intensity_threshold:# Remove labels that has intensity lower than 5
            peaklabel = ''
        else:
            if 'b (' in c or 'y (' in c:
                n0 =re.findall('(\w?)\s\(\d*\)',c)
                n1 =re.findall('\w\s\((\d*?)\)',c)
                n2 =re.findall('\w\s\(\d*\)\s\((.*?)\)',c)
                n3 =re.findall('\w\s\(\d*\)\s\(.*\)(.*)',c)
                ion=n0[0];pos=n1[0];cha=n2[0];der=n3[0]
    
                #peaklabel0= ion+'$^{'+cha+'}_{'+pos+'}$'
                peaklabel0= '$\mathrm{'+ion+'}^{'+cha+'}_{'+pos+'}$'
                #peaklabel0= ion+'$\mathregular{^'+cha+'}_{'+pos+'}$'
                
                'meters $\mathregular{10^1}$',
                if der == '-NH3':
                    der = '-'+'$\mathrm{NH}_{3}$'
                elif der == '-H2O':
                    der = '-'+'$\mathrm{H}_{2}\mathrm{O}$'
                elif der == '-H3OP4':
                    der = '-'+'$\mathrm{H}_{3}\mathrm{PO}_{4}$'
                else:
                    der = der
                peaklabel =peaklabel0+der
                
            else:
                peaklabel = ''
        annolist_new.append(peaklabel)
    
    masslist1=np.array(masslist,dtype='f');intenlist1=np.array(intenlist,dtype='f');annolist1=np.array(annolist_new)
    #print masslist1,'\n',intenlist1,'\n',annolist1;exit()
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
    
    def text_plotter(x_data, y_data, text_positions, axis, annolist1,txt_width,txt_height):
        for x,y,t,a in zip(x_data, y_data, text_positions, annolist1):
            if 'b' in a:
                txtcolor = 'red'
            elif 'y' in c:
                txtcolor = 'blue'
            else:
                txtcolor = 'blue'       
            if y != t and len(a)> 0:
                axis.text(x+10, t, a ,rotation=0, color=txtcolor,horizontalalignment='center',style = 'normal')
                axis.arrow(x,t,0,y-t, color=txtcolor,alpha=0.3, width=0.3,
                        head_width=0, head_length=0, 
                        zorder=0,length_includes_head=False,linestyle = 'dotted')
            else:
                axis.text(x+10, t+2, a ,rotation=0, color=txtcolor,horizontalalignment='center',style = 'normal')
                        
    #random test data:
    x_data = masslist1
    y_data = intenlist1

    #rc('font',**{'family':'sans-serif',
    #         'sans-serif':['Helvetica'],
    #         'style':'normal',
    #         'size':12 })
    #rc('text', usetex=True)  
              
    #GOOD PLOT:
    fig2 = plt.figure(figsize=(6,6))
    ax2 = fig2.add_subplot(111)
    for xx,yy,zz in zip (x_data,y_data,annolist1):
        if 'b' not in zz and 'y' not in zz:
            ax2.vlines(xx,0,yy,linewidth = 1.2,color='gray')
        elif 'b' in zz:
            ax2.vlines(xx,0,yy,linewidth = 1.5,color='red')
        elif 'y' in zz:
            ax2.vlines(xx,0,yy,linewidth = 1.5,color='blue')
        #else:
        #    ax2.vlines(xx,0,yy,linewidth = 1.2,color='gray')
    plt.xlabel('m/z',fontstyle = 'italic')
    plt.ylabel('Relative intensity')
    plt.gca().get_xaxis().set_tick_params(which='both', direction='out')
    plt.gca().get_yaxis().set_tick_params(which='both', direction='out')
    #set the bbox for the text. Increase txt_width for wider text.
    txt_height = 0.06*(plt.ylim()[1] - plt.ylim()[0])
    txt_width = 0.03*(plt.xlim()[1] - plt.xlim()[0])
    #Get the corrected text positions, then write the text.
    text_positions = get_text_positions(x_data, y_data, txt_width, txt_height)
    text_plotter(x_data, y_data, text_positions, ax2, annolist1, txt_width, txt_height)
    
    plt.ylim(0,max(text_positions)+2*txt_height)
    
    fig_title_ls = fig_title.split('_')
    plt.title(fig_title_ls[0],fontsize = 20, y = 1.04)
    plt.subplots_adjust(top=0.85)
    plt.subplots_adjust(bottom=0.17)

    #plt.show();exit()
    
    if not os.path.exists('figures'):
        os.makedirs('figures')
    currentpath = os.getcwd()
    path = currentpath + '/'+"figures"+'/' + fig_title + '.pdf'
    print filenum, fig_title
    plt.savefig(path, format = 'pdf', dpi = 600)
    plt.close()
