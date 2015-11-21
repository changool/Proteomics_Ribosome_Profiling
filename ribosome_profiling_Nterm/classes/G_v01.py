class class_g: # Generate figure for each acetylated peptides

    def __init__(self,x,y,z,x1,y1):
        self.x = x
        self.y = y
        self.z = z
        self.x1 = x1
        self.y1 = y1
    
    def a(self):

        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.table import Cell
        import sys
        import os
        import pylab
        inputlist1 = self.x 
        inputlist2 = self.y 
        inputlist3 = self.z
        leftside = self.x1
        rightside = self.y1
        
        figures_failed = open('list_of_peptides_failed_in_generating_figure.txt','w')

	left_side_cut = leftside # the number of amino acid to the left side from the peptide start site
	right_side_cut = rightside # the number of amino acid to the right side from the peptide start site

	dic = {}
	for z in inputlist1: # Chrom '\t' file with accession info '\t' peptide sequence '\t' peptide start position in mRNA '\t' PSM
	   z_ls = z.strip().split('\t')
	   acc_stpos = z_ls[1].strip() + '\t' + str(z_ls[3].strip())
	   acc_pep = z_ls[1].strip() + '\t' + str(z_ls[2].strip())
	   dic[acc_pep] = acc_stpos

	dicRP = {}
	for x1_num, x1 in enumerate(inputlist2): # coor '\t' RiboSeq '\t' PSM file
	   x1_ls = x1.strip().split('\t')
	   zfnum = str(x1_num).zfill(12) + '#'
	   dicRP[zfnum + x1.strip()] = x1_ls[0].strip()

	for zz_num, zz in enumerate(inputlist3): # mRNAacc | peptide seq | PSM
	    zz_ls = zz.strip().split("|")
	    zz_01 = zz_ls[0] + '\t' + zz_ls[1]
            v = dic.get(zz_01)
            if v == None:
                figures_failed.write(str(zz_num) + "|" +zz.strip()+' does not have matching info in start site file'+'\n')
            else:    
                k_ls = zz_01.split('\t')
		k_pep = k_ls[1]
		v_ls = v.strip().split('\t')
		acc = v_ls[0].strip()
		pepstart = int(v_ls[1].strip())
		if pepstart - ((left_side_cut+1)*3-1) > 0: # determining figure start position
		   figure_start = pepstart - ((left_side_cut+1)*3)
		elif (pepstart-1)%3 == 0:
		   figure_start = 1
		elif (pepstart-1)%3 == 1:
		   figure_start = 2
		elif (pepstart-1)%3 == 2:
		   figure_start = 3
		pepstart_m1 = pepstart - 1
		app_aa = [];app_nu = [];app_ribo = [];app_psmdis = [];app_peppos = [];app_nuupper = [];app_acpep = [];acc_list = []
		blank = ""
		
		for k1,v1 in dicRP.iteritems():# dictionary with mRNA accesseion : coor tab riboseq tab psm
		   if v1 == acc:
			acc_list.append(k1)
		if len(acc_list) <= 18: # break if peptide length is equal or shorter than 6
		   break
		for acc_list_num, x in enumerate(sorted(acc_list)):
			x_sp = x.split('#')
			x_ls = x_sp[1].split('\t') 
			nu = x_ls[2].strip()
			nupos = int(x_ls[1].strip())
			aa = x_ls[3].strip()
			ribo = int(x_ls[7].strip())
			psm = int(x_ls[8].strip())
			app_ribo.append(ribo)
			app_nu.append(nu)
			
			if ((acc_list_num+1)-(pepstart+1))%3 == 0:
                    	    app_aa.append(aa)
     			else:
      			    app_aa.append(blank)
      			    
      		        if ((acc_list_num+1)-(pepstart+1))%3 == 0 and nupos >= pepstart_m1 and nupos <= pepstart_m1 + len(k_pep)*3:
      			    app_acpep.append(aa)
      			    app_psmdis.append(psm)
     			else:
      			    app_acpep.append(blank)
      			    app_psmdis.append(blank)


		figure_end = pepstart_m1 + ((right_side_cut-1)*3-1) + 1
		mrnalen = len(acc_list)
		if figure_end > mrnalen:
		   if (mrnalen - figure_start + 1)%3 == 0:
		      figure_end = len(acc_list) + 1
		   elif (mrnalen - figure_start + 1)%3 == 1:
		      figure_end = len(acc_list)
		   else:
		      figure_end = len(acc_list)-1
		      
		for num1, xx in enumerate(app_nu):
			if xx == xx.upper():
			   break
			
		for num2, xxx in enumerate(app_nu):
			nuupper = xxx.upper()
			if num2 < num1 and (num2-num1-1)%3 == 0:
			   peppos = (num2 - num1 - 1)/3
			elif num2 >= num1 and (num2-num1+2)%3 == 0:
			   peppos = (num2 - num1 + 1 + 1)/3
			else:
			   peppos = blank
			app_peppos.append(peppos)
			app_nuupper.append(nuupper)

		app_aa_cut = app_aa[figure_start-1:figure_end]
		app_nuupper_cut = app_nuupper[figure_start-1:figure_end]
		app_ribo_cut = app_ribo[figure_start-1:figure_end]
		app_psmdis_cut = app_psmdis[figure_start-1:figure_end]
		app_peppos_cut = app_peppos[figure_start-1:figure_end]
		app_acpep_cut = app_acpep[figure_start-1:figure_end]
		

			
		app_aa_cut_s = []
		app_aa_cut_num = []
		for n0000, x0000 in enumerate(app_aa_cut):
		    if len(x0000.strip()) > 0:
			app_aa_cut_s.append(x0000)
			app_aa_cut_num.append(n0000)

		app_acpep_cut_s = []
		for n000, x000 in enumerate(app_acpep_cut):
		    if n000 in app_aa_cut_num:
			app_acpep_cut_s.append(x000)
		
		app_peppos_cut_s = []
		for x00000 in app_peppos_cut:
		    if len(str(x00000)) > 0:
			app_peppos_cut_s.append(x00000)

		#try:
      		N = len(app_ribo_cut)
        
      		xlocation = range(N)
      		bar_width = 1
     			
      		fig, ax = plt.subplots(figsize = (10,3))
      		
      		ax.bar(xlocation, app_ribo_cut, bar_width, linewidth = 0.2, color = 'blue')
      		ax.set_ylabel('#RiboSeq')
      		fig_title = acc + '#' + str(app_peppos[pepstart_m1+1]) + '#' + k_pep
      		ax.set_title(fig_title, fontsize = 15, y = 1.27)
        
      		#for ppn, pp in enumerate(app_peppos_cut_s):
      		#    if pp == 1:
     			#met_pos = ppn
      		
      		cell_text1 = [app_acpep_cut_s,app_aa_cut_s]
      		
      		#i = 0
      		#for kkk,vvv in zip(app_acpep_cut_s,app_aa_cut_s):
      		#    if i == met_pos:
     			#color = 'red'
      		#    else:
     			#color = 'black'
      		#    cell_text1 = (kkk,vvv) 			    
      		the_table1 = plt.table(cellText=cell_text1, rowLabels=None, colWidths = None, cellLoc = 'center', loc = 'top', bbox = [0, 1.02, 1, 0.13])#, cellColours = color )
      		the_table1.set_fontsize(20)
#      		    i += 1
      		
      		for tt,(ind, cells) in enumerate(the_table1._cells.iteritems()):
      			#if tt==met_pos*2:
      			#    color = 'r'
      			#else:
      			#    color = 'w'   
      			cells.set_edgecolor('w')
      			cells.set_height(0.1)
      			#cells.set_textcolor(color)
        
      		cell_text2 = [app_peppos_cut_s]
      		the_table2 = plt.table(cellText=cell_text2, rowLabels=None, colWidths = None, cellLoc = 'center', loc = 'bottom', bbox = [0, -0.10, 1, 0.03])
      		the_table2.set_fontsize(20)
      		for ind, cells in the_table2._cells.iteritems():
      			   cells.set_edgecolor('w')
      			   cells.set_height(0.05)
        
      		cell_text3 = [app_nuupper_cut,app_ribo_cut]
      		the_table3 = plt.table(cellText=cell_text3, rowLabels=None, colWidths = None, cellLoc = 'center', loc = 'bottom', bbox = [0, -0.05, 1, 0.05])
      		the_table3.set_fontsize(20)
      		for ind, cells in the_table3._cells.iteritems():
      			   cells.set_edgecolor('w')
      			   cells.set_height(0.05)						 
        
      		ax.xaxis.set_visible(False)
      		plt.subplots_adjust(top=0.7)
      		plt.subplots_adjust(bottom=0.1)
      		
      		#plt.show()
      		#exit()
        
      		if app_aa[pepstart_m1+1] == 'M' and pepstart_m1 == num1:
       		   folder = 'cano_anno'
      		elif app_aa[pepstart_m1-2] == 'M' and pepstart_m1 == num1 + 3:
       		   folder = 'cano_anno'
      		elif app_aa[pepstart_m1+1] == 'M' and pepstart_m1 > num1:
       		   folder = 'cano_down'
      		elif app_aa[pepstart_m1-2] == 'M' and pepstart_m1 > num1 + 3:
       		   folder = 'cano_down'
      		elif app_aa[pepstart_m1+1] != 'M' and app_aa[pepstart_m1-2] != 'M' and pepstart_m1 > num1:
       		   folder = 'noncano_orf'
      		elif app_aa[pepstart_m1+1] != 'M' and app_aa[pepstart_m1-2] != 'M' and pepstart_m1 < num1:
       		   folder = 'noncano_utr'
      		else:
       		   folder = 'unclassified'
      		currentpath = os.getcwd()
      		path = currentpath + '/' +folder + '/' + fig_title + '.png'
      		print zz_num, path
      		plt.axis("tight")
      		plt.margins(0,0)
        
      		plt.xticks(xlocation, xlocation, rotation = 'vertical', fontsize = 1)
        
      		fig.savefig(path, format = 'png', dpi = 600)
      		plt.close()
		#exit()
		#except:
		#    print zz.strip(),'has failed in generating figure'
		#    figures_failed.write(str(zz_num) + "|" + zz.strip() +' failed in generating a figure'+ '\n')
		#    pass
