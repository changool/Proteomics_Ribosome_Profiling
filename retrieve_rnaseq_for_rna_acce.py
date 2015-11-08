def main():    
    import sys
    from Bio import SeqIO
    
    inputfile1 = open(sys.argv[1],'r')
    inputfile2 = open(sys.argv[2],'r')
    outputfile = open(sys.argv[3],'w')
    
    #entrynum = inputfile1.readlines().count(">")
    
    dic = {}
    for num, x in enumerate(SeqIO.parse(inputfile1,'fasta')): #fasta file
        if num%10000 == 0:
            print num, 'lines out of', #entrynum
        #header = x.description
        #header_ls = header.split("|")
        #acc_ls = header_ls[3].split('.')
        #acc = acc_ls[0]
        #seq = str(x.seq)
        #dic[acc] = seq
    exit()
    for linenum, y in enumerate(inputfile2): # mRNA accession
    
        if linenum%10 == 0:
            current_line =  'Current line is ' + str(linenum) + "\r"
            sys.stdout.write(current_line)
            sys.stdout.flush()    
    
        y_st = y.strip()
        v = dic.get(y_st)
        outputfile.write(y_st + '\t' + v + '\n')
        
if __name__ == '__main__':
    main()