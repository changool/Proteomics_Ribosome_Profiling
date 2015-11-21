#!/usr/bin/python
def main():
	import sys
	import re
	
        inputfile01 = open (sys.argv[1], 'r') # merged bed file format
	outputfile1 = open (sys.argv[2], 'w')
        
        initiation = 0
        for num,x in enumerate(inputfile01):
            if num%100000==0:
                print num
            xst = x.strip()
            xls = xst.split('\t')
            if 'variableStep' in xst:
                initiation += 1
                chrom_ls = re.findall('chrom=(.*)\sspan',xst)
                chrom = chrom_ls[0]

            if initiation > 0 and len(xls) > 1 and '#' not in xst:
                coor = int(xls[0])
                readnum = xls[1]
                output = [chrom,str(coor-1),str(coor),readnum+'\n']
                outputfile1.write('\t'.join(output))

if __name__ == '__main__':
    main()
