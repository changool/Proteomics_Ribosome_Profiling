#!/usr/bin/python
import sys
from Bio import SeqIO
import progress_counter_for_list as prog

inputfile1 = open (sys.argv[1], 'r') # Database from dbPTM
inputfile2 = open ('acclist_ptmlist.txt','r')
inputfile3 = open ('PTM_to_be_selected_1.txt','r')
outputfile = open (sys.argv[2], 'w') # output
#outputfile1 = open ('acclist_ptmlist.txt','w')

acclist_ptmlist = []
for uu in inputfile2:
    acclist_ptmlist.append(uu.strip())
    continue

allptm=[];inputlist1=[];allacc=[];hprd=[];sysptm=[];swissprot=[];pubdb=[];ubiprot=[]

for num111, yy in enumerate(inputfile1):
  if num111 > 0:
    yy_ls = yy.split('\t')
    ptm = yy_ls[9].strip()
    db = yy_ls[5].strip()
    acc1 = yy_ls[1].strip()
    tryppep = yy_ls[11].strip()
    for numyyy, yyy in enumerate(tryppep):
        if yyy != yyy.upper():
            ptmresidue = numyyy+1
            percentile = round(100*ptmresidue/len(tryppep),0)
            break
        
    allptm.append(ptm)
    inputlist1.append(yy.strip()+'\t'+str(percentile))
    allacc.append(acc1)
#    acc_ptm_pep = acc1+"|"+ptm+"|"+tryppep
#    if db == 'HPRD 9.0':
#        hprd.append(acc_ptm_pep)
#    elif db == 'SysPTM 1.1':
#        sysptm.append(acc_ptm_pep)
#    elif db == 'Swiss-Prot 1010711':
#        swissprot.append(acc_ptm_pep)
#    elif db == 'PupDB 1.0':
#        pubdb.append(acc_ptm_pep)
#    elif db == 'UbiProtDB 1.0':
#        ubiprot.append(acc_ptm_pep)
#
#common_acc_ptm_pep = set(hprd)&set(swissprot)
#print common_acc_ptm_pep


inputfile1.seek(0)
ptmlist = list(set(allptm))
acclist = list(set(allacc))

#tempinputlist1 = inputlist1
#oneper = prog.line(acclist,'nonfasta')
#print 'generating acclist_ptmlist'
#for num11, kk in enumerate(acclist):
#    prog.prog(num11,oneper)
#    templist = []
#    for kkk in tempinputlist1:
#        kkk_ls = kkk.split('\t')
#        acc2 = kkk_ls[1].strip()
#        ptm2 = kkk_ls[9].strip()
#        if kk.strip() == acc2:
#            acc_ptm = acc2 + '_' + ptm2
#            acclist_ptmlist.append(acc_ptm)
#            outputfile1.write(acc_ptm+'\n')
#            templist.append(kkk)
#    for kkkk in templist:
#        tempinputlist1.remove(kkkk)
 
  
#oneper = prog.line(inputfile3,'nonfasta')
print 'filtering peptides'
for num111, ptmx in enumerate(inputfile3):
    print num111
#    prog.prog(num111,oneper)
    tempptmlist = [] 
    for num1, x in enumerate(inputlist1):
        x_ls = x.split('\t')
        ptm11 = x_ls[9].strip()
        acc11 = x_ls[1].strip()
        tryppep11 = x_ls[11].strip()
        acc11_ptm11 = acc11 + '_' + ptm11
        if ptmx.strip() in ptm11:
            tempptmlist.append(x.strip())
    temp_select_list = []
    for xx in tempptmlist:
        xx_ls = xx.split('\t')
        ptm111 = xx_ls[9].strip()
        acc111 = xx_ls[1].strip()
        if len(xx_ls) <15:
            pos111 = 50
        else:
            pos111 = int(float(x_ls[14].strip()))
        tryppep111 = xx_ls[11].strip()        
        if len(tryppep111) == 15 and pos111 >30 and pos111 < 70 and 'M' not in tryppep111 and 'C' not in tryppep111:
            temp_select_list.append(xx)
    if len(temp_select_list) < 1:
        temp_select_list = []
        for xx in tempptmlist:
            xx_ls = xx.split('\t')
            ptm111 = xx_ls[9].strip()
            acc111 = xx_ls[1].strip()
            if len(xx_ls) <15:
                pos111 = 50
            else:
                pos111 = int(float(x_ls[14].strip()))
            tryppep111 = xx_ls[11].strip()        
            if len(tryppep111) >= 10 and len(tryppep111) <= 20 and pos111 >30 and pos111 < 70 and 'M' not in tryppep111 and 'C' not in tryppep111:
                temp_select_list.append(xx)
        if len(temp_select_list) < 1:
            temp_select_list = []
            for xx in tempptmlist:
                xx_ls = xx.split('\t')
                ptm111 = xx_ls[9].strip()
                acc111 = xx_ls[1].strip()
                if len(xx_ls) <15:
                    pos111 = 50
                else:
                    pos111 = int(float(x_ls[14].strip()))                
                tryppep111 = xx_ls[11].strip()        
                if len(tryppep111) >= 10 and len(tryppep111) <= 20 and pos111 >30 and pos111 < 70 and 'C' not in tryppep111:
                    temp_select_list.append(xx)
            if len(temp_select_list) < 1:
                temp_select_list = []
                for xx in tempptmlist:
                    xx_ls = xx.split('\t')
                    ptm111 = xx_ls[9].strip()
                    acc111 = xx_ls[1].strip()
                    if len(xx_ls) <15:
                        pos111 = 50
                    else:
                        pos111 = int(float(x_ls[14].strip()))                    
                    tryppep111 = xx_ls[11].strip()        
                    if len(tryppep111) >= 10 and len(tryppep111) <= 20 and pos111 >30 and pos111 < 70 :
                        temp_select_list.append(xx)            
                if len(temp_select_list) < 1:
                    temp_select_list = []
                    for xx in tempptmlist:
                        xx_ls = xx.split('\t')
                        ptm111 = xx_ls[9].strip()
                        acc111 = xx_ls[1].strip()
                        tryppep111 = xx_ls[11].strip()        
                        if len(tryppep111) >= 8 and len(tryppep111) <= 25:
                            temp_select_list.append(xx)                      
                    if len(temp_select_list) < 1:
                        temp_select_list = tempptmlist
                          
    
    if len(temp_select_list)>1:
            dic1 = {}
            for yy in temp_select_list:
                yy_ls = yy.split('\t')
                accyy = yy_ls[1].strip()
                ptmyy = yy_ls[9].strip()
                accyy_ptmyy = accyy +'_'+ ptmyy
                freq = acclist_ptmlist.count(accyy_ptmyy)
                dic1[yy] = int(freq)
            maxacc = max(dic1,key=dic1.get)
            outputfile.write(maxacc + '\n')
    else:
            for yy in temp_select_list:
                outputfile.write(yy.strip() + '\n')
    
                
    
    
