def main():    
    import sys
    from Bio import SeqIO
    
    inputfile1 = open(sys.argv[1],'r')
    inputfile2 = open(sys.argv[2],'r')
    outputfile = open(sys.argv[3],'w')
    
    i = 0
    for nn in inputfile1:
        if '>' in nn:
            i += 1
                
    inputfile1.seek(0)
    rangenum = 50   
    for nnn in range(rangenum):

        dic = {}
        for num, x in enumerate(SeqIO.parse(inputfile1,'fasta')): #fasta file
            if num <= i*(nnn+1)/rangenum: 
                if num%10000 == 0:
                    print num, 'lines out of', i
                header = x.description
                header_ls = header.split("|")
                acc_ls = header_ls[3].split('.')
                acc = acc_ls[0]
                seq = str(x.seq)
                dic[acc] = seq
            else:
                break
        
        inputfile2.seek(0)
        for linenum, y in enumerate(inputfile2): # mRNA accession
                
                    if linenum%10 == 0:
                        print 'Current line is ',str(linenum)                        
                
                    y_st = y.strip()
                    v = dic.get(y_st)
                    if v != None:
                        outputfile.write(y_st + '\t' + v + '\n')
        
if __name__ == '__main__':
    main()
