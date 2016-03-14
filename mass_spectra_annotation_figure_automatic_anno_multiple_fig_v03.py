import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pylab
import re
from os import listdir
from os.path import isfile, join

# instructions
# You make a folder named 'synthetic_pep' and 'real_pep'. Put your text files there
# Precursor mass will be removed from the figure
####################################################################################################
#method for putting annotation
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
            axis.arrow(x,t,0,y-t, color=txtcolor,alpha=0.4, width=0.5,
                    head_width=0, head_length=0, 
                    zorder=0,length_includes_head=False,linestyle = 'dotted')
        else:
            axis.text(x+10, t+2, a ,rotation=0, color=txtcolor,horizontalalignment='center',style = 'normal')
########################################################################################################
intensity_threshold = 5 # Set intensity to put label (0% to 100%)
currentpath = os.getcwd()
synthetic_pep_path = currentpath + '/synthetic_pep'
real_pep_path = currentpath + '/real_pep'
synthetic_pep_files_in_the_folder = [ f for f in listdir(synthetic_pep_path) if isfile(join(synthetic_pep_path,f)) ]
real_pep_files_in_the_folder       = [ f for f in listdir(real_pep_path) if isfile(join(real_pep_path,f)) ]
for filenum, filename in enumerate(real_pep_files_in_the_folder):
 #if 'AAAAAGANLGDR' in filename:    
    inputfile = open(real_pep_path+ '/'+filename, 'r')
    fig_title = filename
    pep_seq_ls = filename.split('_')
    pep_seq = pep_seq_ls[0]
    
    numlist = [];masslist = [];intenlist0 = [];intenlist=[];annolist = []
    for num, x in enumerate(inputfile):
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
    
                peaklabel0= '$\mathrm{'+ion+'}^{'+cha+'}_{'+pos+'}$'
               

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
    
    for filenum_1, filename_1 in enumerate(synthetic_pep_files_in_the_folder):
      #if 'AAAAAGANLGDR' in filename:   
        inputfile_1 = open(synthetic_pep_path+ '/'+filename_1, 'r')
        fig_title_1 = filename_1  
        pep_seq_1_ls = filename_1.split('_')
        pep_seq_1 = pep_seq_1_ls[0]      
        if pep_seq == pep_seq_1:
            
            numlist_1 = [];masslist_1 = [];intenlist0_1 = [];intenlist_1 = [];annolist_1 = []
            for num_1, x_1 in enumerate(inputfile_1):
                if 'm/z' not in x_1:
                    x_st_1  = x_1.strip()
                    x_sp_1  = x_st_1.split('\t')
                    if len(x_sp_1) == 3:
                        if '[M' not in x_sp_1[2] and 'Tyr' not in x_sp_1[2]:#Precursor and Tyr derivative peak will be removed
                            number_1= num_1 + 1; numlist_1.append(number_1)
                            mass_1  = float(x_sp_1[0]); masslist_1.append(mass_1)
                            inten_1 = float(x_sp_1[1]); intenlist0_1.append(inten_1)
                            intenlist_1  = [y_1 / max(intenlist0_1)*100 for y_1 in intenlist0_1]
                            anno_1  = x_sp_1[2].strip(); annolist_1.append(anno_1)
                    elif len(x_sp_1) == 2:
                            number_1= num_1 + 1; numlist_1.append(number_1)
                            mass_1  = float(x_sp_1[0]); masslist_1.append(mass_1)
                            inten_1 = float(x_sp_1[1]); intenlist0_1.append(inten_1)
                            intenlist_1  = [y_1 / max(intenlist0_1)*100 for y_1 in intenlist0_1]
                            anno_1  = ''; annolist_1.append(anno_1)
                        
            annolist_1_new=[]
            for ii_1,c_1 in zip(intenlist_1,annolist_1):
                if ii_1 < intensity_threshold:# Remove labels that has intensity lower than 5
                    peaklabel_1 = ''
                else:
                    if 'b (' in c_1 or 'y (' in c_1:
                        n0_1 =re.findall('(\w?)\s\(\d*\)',c_1)
                        n1_1 =re.findall('\w\s\((\d*?)\)',c_1)
                        n2_1 =re.findall('\w\s\(\d*\)\s\((.*?)\)',c_1)
                        n3_1 =re.findall('\w\s\(\d*\)\s\(.*\)(.*)',c_1)
                        ion_1=n0_1[0];pos_1=n1_1[0];cha_1=n2_1[0];der_1=n3_1[0]
                        peaklabel0_1= '$\mathrm{'+ion_1+'}^{'+cha_1+'}_{'+pos_1+'}$'

                        if der_1 == '-NH3':
                            der_1 = '-'+'$\mathrm{NH}_{3}$'
                        elif der_1 == '-H2O':
                            der_1 = '-'+'$\mathrm{H}_{2}\mathrm{O}$'
                        elif der_1 == '-H3OP4':
                            der_1 = '-'+'$\mathrm{H}_{3}\mathrm{PO}_{4}$'
                        else:
                            der_1 = der_1
                        peaklabel_1 =peaklabel0_1+der_1
                        
                    else:
                        peaklabel_1 = ''
                annolist_1_new.append(peaklabel_1)
            
            masslist1_1=np.array(masslist_1,dtype='f');intenlist1_1=np.array(intenlist_1,dtype='f');annolist1_1=np.array(annolist_1_new)
                    
          
            #random test data:
            x_data = masslist1
            y_data = intenlist1
            x_data_1 = masslist1_1
            y_data_1 = intenlist1_1
            x_merge = [min(x_data),max(x_data),min(x_data_1),max(x_data_1)]
                  
            fig = plt.figure(figsize=(12,10))
            
            #Upper figure
            ax1 = fig.add_subplot(211)
            for xx,yy,zz in zip (x_data,y_data,annolist1):
                if 'b' in zz:
                    ax1.vlines(xx,0,yy,linewidth = 1.5,color='red')
                elif 'y' in zz:
                    ax1.vlines(xx,0,yy,linewidth = 1.5,color='blue')
                else:
                    ax1.vlines(xx,0,yy,linewidth = 1.5,color='gray')
            #plt.xlabel('m/z',fontstyle = 'italic')
            plt.ylabel('Relative intensity')
            plt.gca().get_xaxis().set_tick_params(which='both', direction='out')
            plt.gca().get_yaxis().set_tick_params(which='both', direction='out')
            #set the bbox for the text. Increase txt_width for wider text.
            txt_height = 0.05*(plt.ylim()[1] - plt.ylim()[0])
            txt_width = 0.03*(plt.xlim()[1] - plt.xlim()[0])
            #Get the corrected text positions, then write the text.
            text_positions = get_text_positions(x_data, y_data, txt_width, txt_height)
            text_plotter(x_data, y_data, text_positions, ax1, annolist1, txt_width, txt_height)
            
            plt.xlim(min(x_merge)-50,max(x_merge)+50)
            plt.ylim(0,max(text_positions)+2*txt_height)
            
            #combined_fig_title = fig_title+'\n'+fig_title_1
            plt.title('Ac-'+pep_seq+'\n\n'+'Peptide identified from sample',fontsize = 20, y = 1.02)
            plt.subplots_adjust(top=0.85)
            plt.subplots_adjust(bottom=0.08)

            #Lower figure
            ax1_1 = fig.add_subplot(212)
            for xx_1,yy_1,zz_1 in zip (x_data_1,y_data_1,annolist1_1):
                if 'b' in zz_1:
                    ax1_1.vlines(xx_1,0,yy_1,linewidth = 1.5,color='red')
                elif 'y' in zz_1:
                    ax1_1.vlines(xx_1,0,yy_1,linewidth = 1.5,color='blue')
                else:
                    ax1_1.vlines(xx_1,0,yy_1,linewidth = 1.5,color='gray')
            plt.xlabel('m/z',fontstyle = 'italic')
            plt.ylabel('Relative intensity')
            plt.gca().get_xaxis().set_tick_params(which='both', direction='out')
            plt.gca().get_yaxis().set_tick_params(which='both', direction='out')
            #set the bbox for the text. Increase txt_width for wider text.
            txt_height_1 = 0.05*(plt.ylim()[1] - plt.ylim()[0])
            txt_width_1 = 0.03*(plt.xlim()[1] - plt.xlim()[0])
            #Get the corrected text positions, then write the text.
            text_positions_1 = get_text_positions(x_data_1, y_data_1, txt_width_1, txt_height_1)
            text_plotter(x_data_1, y_data_1, text_positions_1, ax1_1, annolist1_1, txt_width_1, txt_height_1)
            
            
            plt.xlim(min(x_merge)-50,max(x_merge)+50)
            plt.ylim(0,max(text_positions_1)+2*txt_height_1)
            plt.title('Synthetic peptide',fontsize = 20, y = 1.02)
            #plt.subplots_adjust(top=0.85)
            #plt.subplots_adjust(bottom=0.17)        
                        
            #plt.show();exit()
            
            if not os.path.exists('combined_figures'):
                os.makedirs('combined_figures')
            currentpath = os.getcwd()
            path = currentpath + '/'+"combined_figures"+'/' +str(filenum)+'_'+str(filenum_1)+'_combined_' +fig_title + '.pdf'
            print filenum, fig_title
            plt.savefig(path, format = 'pdf', dpi = 600)
            plt.close()
