class class_f: # Put Peptide PSM to the file with chromosome coordinate and RiboSeq information

    def __init__(self,x,y):
        self.x = x
        self.y = y    
            
    def a(self):
        import sys
        from Bio.Seq import Seq
        import operator
        inputlist1 = self.x
        inputlist2 = self.y

	failed_pos = open ('coor_riboseq_psm_failed.txt', 'w')
	outputfile = open ('coor_riboseq_psm.txt', 'w')
        outputlist = []
        
	totallines1 = 0
	for zzz in inputlist1:
	   totallines1 += 1

	totallines2 = 0
	for zzz1 in inputlist2:
	   totallines2 += 1

	dic = {}
	for num_x, x in enumerate(inputlist1): #RNAacce|Position of Nucleotide on mRNA|Nucleotide|AA|Chr|pos|Strand|RiboSeq ReadNo
	    x_ls = x.split("\t")
	    acc = x_ls[0].strip()
	    pos = int(x_ls[1].strip())
	    acc_pos = acc +'|'+ str(pos)
	    x_psm = str(num_x).zfill(12) + "|" + x.strip()+ "@" + str(0)
	    dic[acc_pos] = x_psm
		
	for num_y, y in enumerate(inputlist2):# Chr|RNA acce|Pepseq|Postion on mRNA|PSM
	    if num_y%1000 == 0:
	       print num_y,'out of',totallines2
	   
	    y_ls = y.strip().split("\t")
	    y_mrnaacc = y_ls[1].strip()
	    y_pos = y_ls[3].strip()
	    y_psm = y_ls[4].strip()
	    mr_pos = y_mrnaacc + "|" + y_pos
	    v = dic.get(mr_pos)
	    if v == None:
	        failed_pos.write(y.strip() + ' failed in finding riboseq info')
	    else:
	       v_ls = v.split("@")
	       psm = v_ls[1]
	       new_psm = int(psm) + int(y_psm)
	       dic[mr_pos] = v_ls[0] + "@" + str(new_psm)

	sorted_dic = sorted(dic.iteritems(), key=operator.itemgetter(1))

	odnum = 0
	for k11 in sorted_dic:
	   if odnum%1000 == 0:
	      print odnum, 'out of', totallines1

	   k11_1_ls = k11[1].split("|")
	   result = k11_1_ls[1].replace("@","\t")
	   outputlist.append(result)
	   outputfile.write(result + '\n')
	   odnum += 1
        return outputlist