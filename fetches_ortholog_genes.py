def main():    
    import sys

    inputfile1 = open(sys.argv[1],'r') # gene symbols
    inputfile2 = open(sys.argv[2],'r') # homologene file
    outputfile = open(sys.argv[3],'w')
    
    dic_gene = {}
    for x in inputfile2:
        x_ls = x.split('\t')
        hs_genesym = x_ls[1].strip() +'\t'+ x_ls[3].strip()
        dic_gene[hs_genesym] = x.strip()
    
    dic_num = {}  
    inputfile2.seek(0)  
    for x in inputfile2:
        x_ls = x.split('\t')
        num_x = x_ls[0].strip()
        dic_num[x.strip()] = num_x
        
    for y in inputfile1:
        tax_genesym = '9606' + '\t' + y.strip()
        v = dic_gene.get(tax_genesym)

        if v != None:
            v_ls = v.split('\t')
            num = v_ls[0].strip()
            for k1,v1 in dic_num.iteritems():
                if v1 == num:
                    outputfile.write(k1 + '\n')
                    
        else:
            outputfile.write(y.strip()+' does not have matches'+'\n')
    

if __name__ == '__main__':
    main()