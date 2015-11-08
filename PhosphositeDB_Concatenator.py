#!/usr/bin/python
import sys

inputfile1 = open (sys.argv[1], 'r')# Phosphosite DB from phosphoplus (PROTEIN,ACC_ID,GENE,HU_CHR_LOC,MOD_RSD,SITE_GRP_ID,ORGANISM,MW_kD,DOMAIN,SITE_+/-7_AA,LT_LIT,MS_LIT,MS_CST,CST_CAT#)
outputfile = open (sys.argv[2], 'w')

def main():
    sample_species = 'mouse' # 'human' or 'mouse' or 'rat'
    
    con_seq = ''
    for yyy in inputfile1:
        yyy_ls = yyy.split('\t')
        if len(yyy_ls) >= 10:
            if yyy_ls[6].strip() == sample_species:
                con_seq = con_seq +'#'+ yyy_ls[9].strip()
    con_seq = con_seq.upper() + '#'
    
    outputfile.write(con_seq)
        
    
    
if __name__ == '__main__':
    main()