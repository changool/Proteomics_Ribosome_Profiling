#Developed by Chan-Hyun Na
#Copyright: You may freely use this script
# This version automatically detect data acquisition type (DIA or DDA) and their isolation window for DIA. It works for DIA and DDA mix as well
import base64
import struct
import re
import numpy as np
import os
import sys

#Define the following parameters#
##############################################################################################
isolation_window_for_DDA = 1.6 # Define this number if the data acquisition is DDA
left_isolation_window_offset = 0 # distance for precursor prediction to the left side from the boundary of the isolation window. Unit is dalton.
right_isolation_window_offset = 0 # distance for precursor prediction to the right side from the boundary of the isolation window. Unit is dalton.
monoisotope_search_offset = 1.5 # this parameter determine how far it will search for monoisotopic peak outside of isolation window to the left side
ms2_generation_iteration_count = 5 # how many times it will iterate for MS2 generation for a certain isolation window
isoppm = 10 # this is ppm for isotope cluster extraction, 10 ppm is default
removal_isoppm = 10 # this is ppm for peak removal for the next iteration, 10 ppm is default
initial_max_peak_intensity_threshold = 10000 # intensity threshold for precursor peak for precursor prediction
iteration_intensity_ratio_threshold = 0.2 # this parameter determine when to stop finding more precursors than one (current highest peak/initial highest peak)
##############################################################################################

def decode_spectrum(line):
    decoded = base64.decodestring(line)
    tmp_size = len(decoded)/4
    unpack_format1 = ">%dL" % tmp_size
    
    idx = 0
    mz_list = []
    intensity_list = []
    
    for tmp in struct.unpack(unpack_format1,decoded):
        tmp_i = struct.pack("I",tmp)
        tmp_f = struct.unpack("f",tmp_i)[0]
        if( idx % 2 == 0 ):
            mz_list.append( float(tmp_f) )
        else:
            intensity_list.append( float(tmp_f) )
        idx += 1          
    return [mz_list,intensity_list]

#dirpath = os.getcwd()
#for filename in os.listdir(dirpath):
#    filename_ls = filename.split('.')
#    if filename.endswith(".raw"):
#        if filename_ls[0] + '.mzXML' in os.listdir(dirpath):
#            inputfile1 = open(filename_ls[0] + '.mzXML','r')
#        else:    
#            cmd1 = 'ReAdW --mzXML -c ' +  filename + ' ' + filename_ls[0] + '.mzXML'
#            os.system(cmd1)
#            inputfile1 = open(filename_ls[0] + '.mzXML','r')
#        outputfile = open(filename_ls[0] + '_corrected.mzXML','w')
#    elif filename.endswith(".mzXML") and not filename.endswith("_corrected.mzXML"):
#        inputfile1 = open(filename_ls[0] + '.mzXML','r')
#        outputfile = open(filename_ls[0] + '_corrected.mzXML','w')    
#
def main():
    
        inputfile1 = open(sys.argv[1],'r')
        inputfile_ls = sys.argv[1].split('.')
        outputfile = open(inputfile_ls[0] + '_corrected.mzXML','w')

        inputlist1 = []
        previous1 = ''
        ms1ms2list = []
        ms1ms2_append_switch = 'OFF'
        scan_num = 0
        msLevel = 0
        for num, xx in enumerate(inputfile1): # Input file
        
            if num%100000 == 0:
                print str(num) + ' lines'
                
            if 'msLevel="1"' in xx:msLevel = 1
            if 'msLevel="2"' in xx:msLevel = 2            
            if '<scan num=' in xx:
                ms1ms2_append_switch = 'ON'
            
            if ms1ms2_append_switch == 'ON':
                ms1ms2list.append(xx)
                                
            if ms1ms2_append_switch == 'OFF':
                inputlist1.append(xx)
                        
            if '</scan>' in xx and msLevel == 1:
                for nn, x in enumerate(ms1ms2list):
                    if '<scan num=' in x:
                        scan_num += 1
                        x = '   <scan num="' + str(scan_num) + '"\n' 
                    inputlist1.append(x)
                ms1ms2list = []              
            
            if '</scan>' in previous1 and '</scan>' in xx:
                              
                

                #print ms1ms2list
                ms1ms2_append_switch = 'OFF'
                ms1ms2list_join = "#".join(ms1ms2list)
                ms2mz1_ls = re.findall('ms2 (.*?)@hcd',ms1ms2list_join)
                
                xxx_previous = 0.0
                iso_win_list = []
                for nx, xxx in enumerate(ms2mz1_ls):
                    if nx > 0:
                        IsolationWindowDistance = float(xxx) - float(xxx_previous)
                        iso_win_list.append(IsolationWindowDistance)
                    xxx_previous = xxx
                if len(ms2mz1_ls) > 10:
                    StandardDeviation = np.std(iso_win_list)
                    IsolationWindow = np.mean(iso_win_list)
                else:
                    StandardDeviation = 100
                    IsolationWindow = isolation_window_for_DDA
                        
                if StandardDeviation < 2 and len(ms2mz1_ls) > 10:    
                    #print IsolationWindow
                    left_isolation_window = IsolationWindow/2 + left_isolation_window_offset
                    right_isolation_window = IsolationWindow/2 + right_isolation_window_offset
                else:
                    left_isolation_window = isolation_window_for_DDA/2 + left_isolation_window_offset
                    right_isolation_window = isolation_window_for_DDA/2 + right_isolation_window_offset
                    
                msLevel = 0
                scan_unit = []
                msms_count = 0
                
                for nn, x in enumerate(ms1ms2list):

                    if 'msLevel="1"' in x:msLevel = 1
                    if 'msLevel="2"' in x:msLevel = 2
                    if '<scan num=' in  x:msms_count += 1
                    if msms_count > 1    :scan_unit.append(x)
                
                    if msLevel == 1:
                        if 'compressedLen=' in x:
                            peaks_ls = re.findall('compressedLen="0" >(.*?)</peaks>',x)         
                            peaks = peaks_ls[0]
                            de_peaks = decode_spectrum(peaks)
                        
                            if len(de_peaks[0]) > 0:
                                peak_list = de_peaks[0]
                                peak_int  = de_peaks[1]
                            else:
                                pass
                                
                
                    if '<scan num=' in x and msms_count == 1:
                        scan_num += 1
                        x = '   <scan num="' + str(scan_num) + '"\n' 
                    
                    if msms_count == 1 or nn+1 == len(ms1ms2list):                            
                        inputlist1.append(x)
                   
                    if msLevel == 2 and '</scan>' in x:
                        #print scan_unit
                        ms2_generation = 'ON'
                        iteration_count = 0
                        peak_list_in_win = []
                        peak_int_in_win = []
                        peak_list_in_win_for_charge = []
                        peak_int_in_win_for_charge = []  
                                        
                        while ms2_generation == 'ON' and iteration_count < ms2_generation_iteration_count: # control this parameter
                            
                            for y in scan_unit:
                                if '<scan num=' in y:
                                    scan_num += 1
                                    y = '   <scan num="' + str(scan_num) + '"\n'
                                    inputlist1.append(y)
                                elif 'filterLine=' in y:
                                    #print ms1ms2list
                                    ms2mz_ls = re.findall('ms2 (.*?)@hcd',y)
                                    #print ms2mz_ls
                                    ms2mz = float(ms2mz_ls[0])
                                                                
                                    if iteration_count == 0:
                                        for y1,y2 in zip(peak_list,peak_int):
                                            y1 = float(y1)
                                            if y1 > ms2mz - left_isolation_window and y1 < ms2mz + right_isolation_window:
                                                peak_list_in_win.append(y1)
                                                peak_int_in_win.append(y2)
                                            if y1 > ms2mz + right_isolation_window + 3:
                                                break
                                            if y1 > ms2mz - monoisotope_search_offset - left_isolation_window and y1 < ms2mz + right_isolation_window + 3:
                                                peak_list_in_win_for_charge.append(y1)
                                                peak_int_in_win_for_charge.append(y2)
                                                
                                    if len(peak_list_in_win) == 0:
                                        inputlist1.append(y)
                                        maxpeakint = 1
                                        NewMaxInt = 1
                                        best_match_charge = 1
                                        best_match_mz = 1
                                        continue
                    
                
                                    maxpeakpos = peak_int_in_win.index(max(peak_int_in_win))
                                    maxpeakmz  = float(peak_list_in_win[maxpeakpos]) # this is new m/z
                
                                    maxpeakint = peak_int_in_win[maxpeakpos] # this is new max intensity
                                    if iteration_count == 0:
                                        initial_maxpeakint = maxpeakint
                                        
                                    mz_m2_charge2_ls = [];mz_m2_charge2_int=[];mz_m1_charge2_ls = [];mz_m1_charge2_int=[];mz_0_charge2_ls = [];mz_0_charge2_int=[];mz_p1_charge2_ls = [];mz_p1_charge2_int=[];mz_p2_charge2_ls = [];mz_p2_charge2_int=[];mz_p3_charge2_ls = [];mz_p3_charge2_int=[];
                                    mz_m2_charge3_ls = [];mz_m2_charge3_int=[];mz_m1_charge3_ls = [];mz_m1_charge3_int=[];mz_0_charge3_ls = [];mz_0_charge3_int=[];mz_p1_charge3_ls = [];mz_p1_charge3_int=[];mz_p2_charge3_ls = [];mz_p2_charge3_int=[];mz_p3_charge3_ls = [];mz_p3_charge3_int=[];
                                    mz_m2_charge4_ls = [];mz_m2_charge4_int=[];mz_m1_charge4_ls = [];mz_m1_charge4_int=[];mz_0_charge4_ls = [];mz_0_charge4_int=[];mz_p1_charge4_ls = [];mz_p1_charge4_int=[];mz_p2_charge4_ls = [];mz_p2_charge4_int=[];mz_p3_charge4_ls = [];mz_p3_charge4_int=[];
                
                                    isotope_dis = 1.00000000
                                    for z1,z2 in zip(peak_list_in_win_for_charge,peak_int_in_win_for_charge):
                                        if z1 > (maxpeakmz + isotope_dis*(-2)/2) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*(-2)/2) + maxpeakmz*isoppm/1000000:
                                            mz_m2_charge2_ls.append(z1)
                                            mz_m2_charge2_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*(-2)/3) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*(-2)/3) + maxpeakmz*isoppm/1000000:
                                            mz_m2_charge3_ls.append(z1)
                                            mz_m2_charge3_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*(-2)/4) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*(-2)/4) + maxpeakmz*isoppm/1000000:
                                            mz_m2_charge4_ls.append(z1)
                                            mz_m2_charge4_int.append(z2)                        
                
                                        if z1 > (maxpeakmz + isotope_dis*(-1)/2) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*(-1)/2) + maxpeakmz*isoppm/1000000:
                                            mz_m1_charge2_ls.append(z1)
                                            mz_m1_charge2_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*(-1)/3) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*(-1)/3) + maxpeakmz*isoppm/1000000:
                                            mz_m1_charge3_ls.append(z1)
                                            mz_m1_charge3_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*(-1)/4) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*(-1)/4) + maxpeakmz*isoppm/1000000:
                                            mz_m1_charge4_ls.append(z1)
                                            mz_m1_charge4_int.append(z2) 
                
                                        if z1 > (maxpeakmz + isotope_dis*0/2) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*0/2) + maxpeakmz*isoppm/1000000:
                                            mz_0_charge2_ls.append(z1)
                                            mz_0_charge2_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*0/3) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*0/3) + maxpeakmz*isoppm/1000000:
                                            mz_0_charge3_ls.append(z1)
                                            mz_0_charge3_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*0/4) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*0/4) + maxpeakmz*isoppm/1000000:
                                            mz_0_charge4_ls.append(z1)
                                            mz_0_charge4_int.append(z2)
                
                                        if z1 > (maxpeakmz + isotope_dis*1/2) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*1/2) + maxpeakmz*isoppm/1000000:
                                            mz_p1_charge2_ls.append(z1)
                                            mz_p1_charge2_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*1/3) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*1/3) + maxpeakmz*isoppm/1000000:
                                            mz_p1_charge3_ls.append(z1)
                                            mz_p1_charge3_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*1/4) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*1/4) + maxpeakmz*isoppm/1000000:
                                            mz_p1_charge4_ls.append(z1)
                                            mz_p1_charge4_int.append(z2)
                
                                        if z1 > (maxpeakmz + isotope_dis*2/2) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*2/2) + maxpeakmz*isoppm/1000000:
                                            mz_p2_charge2_ls.append(z1)
                                            mz_p2_charge2_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*2/3) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*2/3) + maxpeakmz*isoppm/1000000:
                                            mz_p2_charge3_ls.append(z1)
                                            mz_p2_charge3_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*2/4) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*2/4) + maxpeakmz*isoppm/1000000:
                                            mz_p2_charge4_ls.append(z1)
                                            mz_p2_charge4_int.append(z2)
                
                                        if z1 > (maxpeakmz + isotope_dis*3/2) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*3/2) + maxpeakmz*isoppm/1000000:
                                            mz_p3_charge2_ls.append(z1)
                                            mz_p3_charge2_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*3/3) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*3/3) + maxpeakmz*isoppm/1000000:
                                            mz_p3_charge3_ls.append(z1)
                                            mz_p3_charge3_int.append(z2)
                                        if z1 > (maxpeakmz + isotope_dis*3/4) - maxpeakmz*isoppm/1000000 and z1 < (maxpeakmz + isotope_dis*3/4) + maxpeakmz*isoppm/1000000:
                                            mz_p3_charge4_ls.append(z1)
                                            mz_p3_charge4_int.append(z2)
                
                                    
                                    ms2_c2 = ms2mz * 2
                                    ms2_c3 = ms2mz * 3
                                    ms2_c4 = ms2mz * 4
                                    
                                    M1_c2_int = 6*(10**-8)*(ms2_c2**2) + 0.0002*ms2_c2 + 0.3757
                                    M2_c2_int = 2*(10**-7)*(ms2_c2**2) - 0.0003*ms2_c2 + 0.318
                                    M3_c2_int = 2*(10**-7)*(ms2_c2**2) - 0.0004*ms2_c2 + 0.2418
                                    
                                    M1_c3_int = 6*(10**-8)*(ms2_c3**2) + 0.0002*ms2_c3 + 0.3757
                                    M2_c3_int = 2*(10**-7)*(ms2_c3**2) - 0.0003*ms2_c3 + 0.318
                                    M3_c3_int = 2*(10**-7)*(ms2_c3**2) - 0.0004*ms2_c3 + 0.2418                        
                                    
                                    M1_c4_int = 6*(10**-8)*(ms2_c4**2) + 0.0002*ms2_c4 + 0.3757
                                    M2_c4_int = 2*(10**-7)*(ms2_c4**2) - 0.0003*ms2_c4 + 0.318
                                    M3_c4_int = 2*(10**-7)*(ms2_c4**2) - 0.0004*ms2_c4 + 0.2418                        
                                    
                                    #print M1_c2_int,M2_c2_int,M3_c2_int,M1_c3_int,M2_c3_int,M3_c3_int,M1_c4_int,M2_c4_int,M3_c4_int
                
                                    if len(mz_m2_charge2_int)==0 or max(mz_m2_charge2_int)==0: max_m2_charge2_int = 0.00001 
                                    else: max_m2_charge2_int = max(mz_m2_charge2_int)    
                                    if len(mz_m1_charge2_int)==0 or max(mz_m1_charge2_int)==0: max_m1_charge2_int = 0.00001
                                    else: max_m1_charge2_int = max(mz_m1_charge2_int) 
                                    if len(mz_0_charge2_int) ==0 or max(mz_0_charge2_int) ==0: max_0_charge2_int  = 0.00001 
                                    else: max_0_charge2_int  = max(mz_0_charge2_int)                                                           
                                    if len(mz_p1_charge2_int)==0 or max(mz_p1_charge2_int)==0: max_p1_charge2_int = 0.00001
                                    else: max_p1_charge2_int = max(mz_p1_charge2_int)   
                                    if len(mz_p2_charge2_int)==0 or max(mz_p2_charge2_int)==0: max_p2_charge2_int = 0.00001 
                                    else: max_p2_charge2_int = max(mz_p2_charge2_int)                                                                                       
                                    if len(mz_p3_charge2_int)==0 or max(mz_p3_charge2_int)==0: max_p3_charge2_int = 0.00001
                                    else: max_p3_charge2_int = max(mz_p3_charge2_int)                                                                                                                                                                                                       
                                    ###############################################
                                    if len(mz_m2_charge3_int)==0 or max(mz_m2_charge3_int)==0: max_m2_charge3_int = 0.00001 
                                    else: max_m2_charge3_int = max(mz_m2_charge3_int)    
                                    if len(mz_m1_charge3_int)==0 or max(mz_m1_charge3_int)==0: max_m1_charge3_int = 0.00001 
                                    else: max_m1_charge3_int = max(mz_m1_charge3_int) 
                                    if len(mz_0_charge3_int) ==0 or max(mz_0_charge3_int) ==0: max_0_charge3_int  = 0.00001 
                                    else: max_0_charge3_int  = max(mz_0_charge3_int)                                                           
                                    if len(mz_p1_charge3_int)==0 or max(mz_p1_charge3_int)==0: max_p1_charge3_int = 0.00001 
                                    else: max_p1_charge3_int = max(mz_p1_charge3_int)   
                                    if len(mz_p2_charge3_int)==0 or max(mz_p2_charge3_int)==0: max_p2_charge3_int = 0.00001 
                                    else: max_p2_charge3_int = max(mz_p2_charge3_int)                                                                                       
                                    if len(mz_p3_charge3_int)==0 or max(mz_p3_charge3_int)==0: max_p3_charge3_int = 0.00001 
                                    else: max_p3_charge3_int = max(mz_p3_charge3_int)                                                             
                                    ###############################################                                              
                                    if len(mz_m2_charge4_int)==0 or max(mz_m2_charge4_int)==0: max_m2_charge4_int = 0.00001 
                                    else: max_m2_charge4_int = max(mz_m2_charge4_int)    
                                    if len(mz_m1_charge4_int)==0 or max(mz_m1_charge4_int)==0: max_m1_charge4_int = 0.00001 
                                    else: max_m1_charge4_int = max(mz_m1_charge4_int) 
                                    if len(mz_0_charge4_int) ==0 or max(mz_0_charge4_int) ==0: max_0_charge4_int  = 0.00001 
                                    else: max_0_charge4_int  = max(mz_0_charge4_int)                                                           
                                    if len(mz_p1_charge4_int)==0 or max(mz_p1_charge4_int)==0: max_p1_charge4_int = 0.00001 
                                    else: max_p1_charge4_int = max(mz_p1_charge4_int)   
                                    if len(mz_p2_charge4_int)==0 or max(mz_p2_charge4_int)==0: max_p2_charge4_int = 0.00001 
                                    else: max_p2_charge4_int = max(mz_p2_charge4_int)                                                                                       
                                    if len(mz_p3_charge4_int)==0 or max(mz_p3_charge4_int)==0: max_p3_charge4_int = 0.00001 
                                    else: max_p3_charge4_int = max(mz_p3_charge4_int)                                                                                                                                                                                    
                
                                    mz_charge2_maxint_ls = [max_m2_charge2_int,max_m1_charge2_int,max_0_charge2_int,max_p1_charge2_int,max_p2_charge2_int,max_p3_charge2_int]
                                    mz_charge3_maxint_ls = [max_m2_charge3_int,max_m1_charge3_int,max_0_charge3_int,max_p1_charge3_int,max_p2_charge3_int,max_p3_charge3_int]
                                    mz_charge4_maxint_ls = [max_m2_charge4_int,max_m1_charge4_int,max_0_charge4_int,max_p1_charge4_int,max_p2_charge4_int,max_p3_charge4_int]
                
                                    m2_charge2 = mz_charge2_maxint_ls[:4]
                                    m1_charge2 = mz_charge2_maxint_ls[1:5]
                                    m0_charge2 = mz_charge2_maxint_ls[2:]
                                    m2_charge3 = mz_charge3_maxint_ls[:4]
                                    m1_charge3 = mz_charge3_maxint_ls[1:5]
                                    m0_charge3 = mz_charge3_maxint_ls[2:]
                                    m2_charge4 = mz_charge4_maxint_ls[:4]
                                    m1_charge4 = mz_charge4_maxint_ls[1:5]
                                    m0_charge4 = mz_charge4_maxint_ls[2:]
                                    
                                    m2_charge2_norm = [m2_charge2[0]/m2_charge2[0],m2_charge2[1]/m2_charge2[0],m2_charge2[2]/m2_charge2[0],m2_charge2[3]/m2_charge2[0]]
                                    m1_charge2_norm = [m1_charge2[0]/m1_charge2[0],m1_charge2[1]/m1_charge2[0],m1_charge2[2]/m1_charge2[0],m1_charge2[3]/m1_charge2[0]]
                                    m0_charge2_norm = [m0_charge2[0]/m0_charge2[0],m0_charge2[1]/m0_charge2[0],m0_charge2[2]/m0_charge2[0],m0_charge2[3]/m0_charge2[0]]
                                    
                                    m2_charge3_norm = [m2_charge3[0]/m2_charge3[0],m2_charge3[1]/m2_charge3[0],m2_charge3[2]/m2_charge3[0],m2_charge3[3]/m2_charge3[0]]
                                    m1_charge3_norm = [m1_charge3[0]/m1_charge3[0],m1_charge3[1]/m1_charge3[0],m1_charge3[2]/m1_charge3[0],m1_charge3[3]/m1_charge3[0]]
                                    m0_charge3_norm = [m0_charge3[0]/m0_charge3[0],m0_charge3[1]/m0_charge3[0],m0_charge3[2]/m0_charge3[0],m0_charge3[3]/m0_charge3[0]]                      
                                    
                                    m2_charge4_norm = [m2_charge4[0]/m2_charge4[0],m2_charge4[1]/m2_charge4[0],m2_charge4[2]/m2_charge4[0],m2_charge4[3]/m2_charge4[0]]
                                    m1_charge4_norm = [m1_charge4[0]/m1_charge4[0],m1_charge4[1]/m1_charge4[0],m1_charge4[2]/m1_charge4[0],m1_charge4[3]/m1_charge4[0]]
                                    m0_charge4_norm = [m0_charge4[0]/m0_charge4[0],m0_charge4[1]/m0_charge4[0],m0_charge4[2]/m0_charge4[0],m0_charge4[3]/m0_charge4[0]]
                                                                
                                    m2_c2 = (1 - m2_charge2_norm[0])**2 + (M1_c2_int - m2_charge2_norm[1])**2 + (M2_c2_int - m2_charge2_norm[2])**2 + (M3_c2_int - m2_charge2_norm[3])**2
                                    m1_c2 = (1 - m1_charge2_norm[0])**2 + (M1_c2_int - m1_charge2_norm[1])**2 + (M2_c2_int - m1_charge2_norm[2])**2 + (M3_c2_int - m1_charge2_norm[3])**2
                                    m0_c2 = (1 - m0_charge2_norm[0])**2 + (M1_c2_int - m0_charge2_norm[1])**2 + (M2_c2_int - m0_charge2_norm[2])**2 + (M3_c2_int - m0_charge2_norm[3])**2
                                    
                                    m2_c3 = (1 - m2_charge3_norm[0])**2 + (M1_c3_int - m2_charge3_norm[1])**2 + (M2_c3_int - m2_charge3_norm[2])**2 + (M3_c3_int - m2_charge3_norm[3])**2
                                    m1_c3 = (1 - m1_charge3_norm[0])**2 + (M1_c3_int - m1_charge3_norm[1])**2 + (M2_c3_int - m1_charge3_norm[2])**2 + (M3_c3_int - m1_charge3_norm[3])**2
                                    m0_c3 = (1 - m0_charge3_norm[0])**2 + (M1_c3_int - m0_charge3_norm[1])**2 + (M2_c3_int - m0_charge3_norm[2])**2 + (M3_c3_int - m0_charge3_norm[3])**2
                                    
                                    m2_c4 = (1 - m2_charge4_norm[0])**2 + (M1_c4_int - m2_charge4_norm[1])**2 + (M2_c4_int - m2_charge4_norm[2])**2 + (M3_c4_int - m2_charge4_norm[3])**2
                                    m1_c4 = (1 - m1_charge4_norm[0])**2 + (M1_c4_int - m1_charge4_norm[1])**2 + (M2_c4_int - m1_charge4_norm[2])**2 + (M3_c4_int - m1_charge4_norm[3])**2
                                    m0_c4 = (1 - m0_charge4_norm[0])**2 + (M1_c4_int - m0_charge4_norm[1])**2 + (M2_c4_int - m0_charge4_norm[2])**2 + (M3_c4_int - m0_charge4_norm[3])**2
                                    
                                    if len(mz_m2_charge2_ls) == 0:mz_m2_charge2_ls = [1]                                        
                                    if len(mz_m1_charge2_ls) == 0:mz_m1_charge2_ls = [1]
                                    if len(mz_0_charge2_ls)  == 0:mz_0_charge2_ls  = [1]
                                    if len(mz_m2_charge3_ls) == 0:mz_m2_charge3_ls = [1]                            
                                    if len(mz_m1_charge3_ls) == 0:mz_m1_charge3_ls = [1]
                                    if len(mz_0_charge3_ls)  == 0:mz_0_charge3_ls  = [1]
                                    if len(mz_m2_charge4_ls) == 0:mz_m2_charge4_ls = [1]        
                                    if len(mz_m1_charge4_ls) == 0:mz_m1_charge4_ls = [1]                                                                
                                    if len(mz_0_charge4_ls)  == 0:mz_0_charge4_ls  = [1]                                                                                                                                                                        
                
                                    mz_value = [np.mean(mz_m2_charge2_ls),np.mean(mz_m1_charge2_ls),np.mean(mz_0_charge2_ls),np.mean(mz_m2_charge3_ls),np.mean(mz_m1_charge3_ls),np.mean(mz_0_charge3_ls),np.mean(mz_m2_charge4_ls),np.mean(mz_m1_charge4_ls),np.mean(mz_0_charge4_ls)]
                                    #print mz_value
                                    values_for_envelope = [m2_c2,m1_c2,m0_c2,m2_c3,m1_c3,m0_c3,m2_c4,m1_c4,m0_c4]
                                    #print values_for_envelope
                                    index_number_for_min = values_for_envelope.index(min(values_for_envelope))
                                    best_match_mz = mz_value[index_number_for_min]
                                    
                                    MaxIntDeterList = []
                                    for aaa,bbb in zip(peak_list_in_win_for_charge,peak_int_in_win_for_charge):
                                       if aaa > best_match_mz  - best_match_mz*isoppm/1000000 and aaa < best_match_mz + best_match_mz*isoppm/1000000:
                                           MaxIntDeterList.append(bbb)
                                    if len(MaxIntDeterList) > 0:
                                        NewMaxInt=max(MaxIntDeterList)       
                                    else:
                                        NewMaxInt = 1    
                                    
                                    if index_number_for_min < 3:
                                        best_match_charge = 2
                                    elif index_number_for_min >= 3 and index_number_for_min < 6:
                                        best_match_charge = 3
                                    else:
                                        best_match_charge = 4    
                                    
                    
                                    #line_ls = y.split('ms2 ')
                                    #line_later = line_ls[1].split('@')
                                    #y = line_ls[0] +'ms2 '+ str(best_match_mz) +'@'+ line_later[1]
                                    inputlist1.append(y)
                
                                elif '<precursorMz precursorIntensity=' in y:
                                    y = '    <precursorMz precursorIntensity="%d" precursorCharge="%d" activationMethod="HCD">%f</precursorMz>\n' % (NewMaxInt,best_match_charge,best_match_mz)
                
                                    inputlist1.append(y)
                                    
                                else:    
                                    inputlist1.append(y)
                            iteration_count += 1        
                            
                
                            if len(peak_list_in_win) > 0 and len(peak_int_in_win) > 0 and best_match_mz > 300 and initial_maxpeakint > initial_max_peak_intensity_threshold: # control this parameter
                                #print len(peak_list_in_win)
                                
                                new_peak_list = []
                                new_int_list = []
                                new_peak_list_for_charge = []
                                new_int_list_for_charge = []
                                if maxpeakmz * best_match_charge < 1000:        
                                    removal_list = [best_match_mz,best_match_mz+(isotope_dis*1)/best_match_charge,best_match_mz+(isotope_dis*2)/best_match_charge,best_match_mz+(isotope_dis*3)/best_match_charge]
                                elif maxpeakmz * best_match_charge >= 1000 and maxpeakmz * best_match_charge < 2500:        
                                    removal_list = [best_match_mz,best_match_mz+(isotope_dis*1)/best_match_charge,best_match_mz+(isotope_dis*2)/best_match_charge,best_match_mz+(isotope_dis*3)/best_match_charge,best_match_mz+(isotope_dis*4)/best_match_charge]
                                elif maxpeakmz * best_match_charge >= 2500 and maxpeakmz * best_match_charge < 3000:        
                                    removal_list = [best_match_mz,best_match_mz+(isotope_dis*1)/best_match_charge,best_match_mz+(isotope_dis*2)/best_match_charge,best_match_mz+(isotope_dis*3)/best_match_charge,best_match_mz+(isotope_dis*4)/best_match_charge,best_match_mz+(isotope_dis*5)/best_match_charge]
                                else:
                                    removal_list = [best_match_mz,best_match_mz+(isotope_dis*1)/best_match_charge,best_match_mz+(isotope_dis*2)/best_match_charge,best_match_mz+(isotope_dis*3)/best_match_charge,best_match_mz+(isotope_dis*4)/best_match_charge,best_match_mz+(isotope_dis*5)/best_match_charge,best_match_mz+(isotope_dis*6)/best_match_charge]

                                for x2,y2 in zip(peak_list_in_win,peak_int_in_win):
                                    removal_switch1 = 'OFF'
                                    for z10 in removal_list:
                                        if x2 > z10-z10*removal_isoppm/1000000 and x2 < z10+z10*removal_isoppm/1000000:
                                            removal_switch1 = 'ON'

                                           
                                    if removal_switch1 == 'OFF':
                                        new_peak_list.append(x2)
                                        new_int_list.append(y2)

                                peak_list_in_win = new_peak_list
                                peak_int_in_win = new_int_list

                                           
                                for x3,y3 in zip(peak_list_in_win_for_charge,peak_int_in_win_for_charge):
                                    removal_switch2 = 'OFF'
                                    for z10 in removal_list:

                                        if x3 > z10-z10*removal_isoppm/1000000 and x3 < z10+z10*removal_isoppm/1000000:
                                            removal_switch2 = 'ON'

                                    if removal_switch2 == 'OFF':    
                                        new_peak_list_for_charge.append(x3)
                                        new_int_list_for_charge.append(y3)

                                peak_list_in_win_for_charge = new_peak_list_for_charge
                                peak_int_in_win_for_charge = new_int_list_for_charge    
                                
                                                                                                                
                
                                if len(peak_int_in_win) == 0:
                                    ms2_generation = 'OFF'
                                elif float(max(peak_int_in_win)/initial_maxpeakint) <  iteration_intensity_ratio_threshold: # control this parameter
                                    ms2_generation = 'OFF'  
                            else:
                                ms2_generation = 'OFF'            
                        scan_unit = []
                msms_count = 0
                ms1ms2list = []            
            previous1 = xx
            

        ss_count = 0
        char_count = 0
        scan_num_count = 0
        offset = {}
        write_switch1 = 'ON'
        for zz in inputlist1:
            if '<msRun scanCount=' in zz:
                zz_ls = zz.split('startTime')
                zz = ' <msRun scanCount="' + str(scan_num) + '" startTime' + zz_ls[1]
            if '</scan>' in zz:
                ss_count += 1
            else:
                ss_count = 0
            
            if '<scan num=' in zz:
                scan_num_count += 1
                scan_num_position = zz.index('<scan num')
                offset_pos = char_count + scan_num_position
                offset[scan_num_count] = offset_pos
                
            if '<index name=' in zz:
                index_pos = char_count + zz.index('<index name')
            
            char_count += len(zz)
            
            if '<offset id=' in zz:
                write_switch1 = 'OFF'   
                    
            if ss_count != 3 and write_switch1 == 'ON':    
                if '<indexOffset>' in zz:
                    outputfile.write(' <indexOffset>%d</indexOffset>\n' %(index_pos))
                
                else:
                    outputfile.write(zz)      
                
            if '</index>' in zz:
                write_switch1 = 'ON'
                for k,v in offset.iteritems():
                    outputfile.write('    <offset id="%d">%d</offset>\n' %(k,v))
                outputfile.write('   </index>\n')   
                
        
if __name__ == "__main__":main()