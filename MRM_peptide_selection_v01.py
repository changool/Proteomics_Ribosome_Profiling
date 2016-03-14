#!/usr/bin/python

import sys
from Bio import SeqIO

def digest(protein,enzyme,missed_cleavage,min_len,max_len):
    if enzyme == 'trypsin':
        pep_ls = protein.replace("KP","XP").replace("RP","ZP").replace("K","K|").replace("R","R|").replace('X','K').replace('Z','R').split('|')
    elif enzyme == 'lysc':
        pep_ls = protein.replace("K","K|").split('|')
    elif enzyme == 'gluc':
        pep_ls = protein.replace("E","E|").replace('D','D|').split('|')        
    else:
        print 'No matching enzyme'
        exit()
    pep_ls = filter(None,pep_ls)
    pep_ls1 = []
    for n,p in enumerate(pep_ls):
        conca_pep = ''
        for nn in range(missed_cleavage+1):
            if n + nn <= len(pep_ls) - 1:
                conca_pep = conca_pep + pep_ls[n + nn]
                if len(conca_pep) >= min_len and len(conca_pep) <= max_len:
                    pep_ls1.append(conca_pep)
    return pep_ls1

inputfile01 = open(sys.argv[1],'r')
outputfile1 = open(sys.argv[2],'w')

gene_list = ['SAA1']
for g in gene_list:
    gene = g.strip()
    fasta_ls = []
    for x in SeqIO.parse(inputfile01,'fasta'):
        header = x.description
        if '#' + gene + '#' in header:
            seq    = str(x.seq)
            fasta_ls.append(header+'@'+seq)
    inputfile01.seek(0)
    #fasta_ls = ['@PPYEGERKPGGRGGAALRSSST','@AEKGERKPGGRERPKERSSST','@TTPEAGERKPGGREGGGAARSSST']
    
    ls_ls = []
    for hd_pro in fasta_ls:
        hd_pro_ls = hd_pro.split('@')
        header = hd_pro_ls[0]
        pro    = hd_pro_ls[1]
        enzyme = 'trypsin'
        missed_cleavage = 0
        min_pep_length = 6
        max_pep_length = 20
        peplist = digest(pro,enzyme,missed_cleavage,min_pep_length,max_pep_length)
        ls_ls.append(set(peplist))
    shared_peptide_list = list(set.intersection(*ls_ls))
    filtered_list = [n for n in shared_peptide_list if 'M' not in n and 'P' not in n]
    print gene,filtered_list
    outputfile1.write(gene + '#' + '\t'.join(filtered_list))