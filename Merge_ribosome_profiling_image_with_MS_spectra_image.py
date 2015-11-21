# This code will return files ends with a certain string in a dirctory
import os
import os.path
import datetime
import sys
from PIL import Image
import shutil
import re



#def modification_date(filename):
#    t = os.path.getmtime(filename)
#    return datetime.datetime.fromtimestamp(t)
   
#blankimg = Image.open('blank.jpg')
#blankimg = Image.new("RGB",(800,800),'white')
folder_for_ribo = sys.argv[1] # enter folder location for riboseq
folder_for_pep = sys.argv[2] # enter folder location for peptide
dir_path = os.getcwd()



#for dirpath, dirnames, filename in os.walk(folder_for_ribo):
filename0_list = os.listdir(folder_for_ribo)
filename1_list = os.listdir(folder_for_pep)

for filename in filename0_list:
    file_name_ls = filename.split("#")
    if len(file_name_ls) >= 3:
        pepseq0_ls = file_name_ls[2].split(".")
        pepseq0 = pepseq0_ls[0]
        
        for filename1 in filename1_list:
            file_name_ls1 = filename1.split("_")
            pepseq1 = file_name_ls1[3]
            if pepseq0 == pepseq1:
                #blankimg.paste(dir_path+ '/' + filename, (0,0,0,0))
                #blankimg.paste(dir_path+ '/' + filename1, (400,0,0,0))
    #            merged_image = filename + 'peptide_spectra'
                filename_1 = re.findall('(.*)\.png',filename)
                merged_img_folder = filename_1[0] + '_peptide_spectra'
                if not os.path.exists(merged_img_folder):
                    os.makedirs(merged_img_folder)
                shutil.copy(folder_for_ribo+ '/' + filename, merged_img_folder)
                shutil.copy(folder_for_pep+ '/' + filename1, merged_img_folder)
                        
            #blankimg.show(merged_image)
#            blankimg.save(merged_image)
            
 #except:
 #   print 'error in',filename