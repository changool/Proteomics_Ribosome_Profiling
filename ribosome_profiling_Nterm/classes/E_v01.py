	#!/usr/bin/python
class class_e: # Remove duplicates peptides to generate a file with peptides start position in mRNA

    def __init__(self,x):
        self.x = x    
    def a(self):
        inputlist1 = self.x
	outputfile = open ('pep_start_pos.txt', 'w')
        outputlist = []

	upperline = ""
	for num_y, y in enumerate(inputlist1):# Chr'\t'RNA acce'\t'Pepseq'\t'position in mRNA'\t'PSM
	#        if num_y%100 == 0:
	#           print num_y
		y_st = y.strip()
		y_ls = y_st.split("\t")
		pepseq = y_ls[2].strip()
		if pepseq != upperline:
		   result = y_st
		   outputlist.append(result)
		   outputfile.write(result + '\n')
		upperline = pepseq
        return outputlist