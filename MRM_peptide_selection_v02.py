#!/usr/bin/python

import sys
from Bio import SeqIO
import getopt

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



options, remainder = getopt.getopt(sys.argv[1:],'', ['input=',
                                                     'miss=',
                                                     'output=',
                                                     'enzyme=',
                                                     'min_length=',
                                                     'max_length=',
                                                     'excluded_aa=',
                                                     'gene_symbol=',
                                                     'help'])
       
for opt, arg in options:
        if opt == '--help':
            print 'MRM_peptide_selection_vXX.py --input <input_fasta_file> --output <output_file> --enzyme <enzyme_to_be_used> --miss <number_of_missed_cleavage_allowed> --min_length <minimum_length_of_peptide> --max_length <maximum_length_of_peptide> --excluded_aa <None, M, P or MP> --gene_symbol <file_for_gene_symbols>'
            sys.exit()
        elif opt == '--input': input_file=arg
        elif opt == '--miss': missed_cleavage=int(arg)  #number of miss cleavage allowed
        elif opt == '--output':output_file=arg
        elif opt == '--enzyme':enzyme=arg
        elif opt == '--gene_symbol':gene_list=arg
        elif opt == '--excluded_aa':excluded_aa=arg
        elif opt == '--min_length':min_pep_length=int(arg)
        elif opt == '--max_length':max_pep_length=int(arg)
        else:
            print "Warning! Command-line argument: %s not recognized. Exiting..." % opt; sys.exit()

inputfile01 = open(input_file,'r')
outputfile1 = open(output_file,'w')

#gene_list = ['SAA1']
gene_list = open(gene_list,'r')
for g in gene_list:
    gene = g.strip()
    fasta_ls = []
    protein_for_other_genes_ls = []
    for x in SeqIO.parse(inputfile01,'fasta'):
        header = x.description
        seq    = str(x.seq)
        if '#' + gene + '#' in header:
            fasta_ls.append(header+'@'+seq)
        else:
            protein_for_other_genes_ls.append(seq)
    protein_for_other_genes = '#'.join(protein_for_other_genes_ls)        
    inputfile01.seek(0)
    if len(fasta_ls) == 0:
        print 'No mathcing genes'
        outputline = g.strip() + ' does not have matching sequence' + '\n'
        outputfile1.write(outputline)
        continue
    #fasta_ls = ['@PPYEGERKPGGRGGAALRSSST','@AEKGERKPGGRERPKERSSST','@TTPEAGERKPGGREGGGAARSSST']
    
    ls_ls = []
    for hd_pro in fasta_ls:
        hd_pro_ls = hd_pro.split('@')
        header = hd_pro_ls[0]
        pro    = hd_pro_ls[1]
        peplist = digest(pro,enzyme,missed_cleavage,min_pep_length,max_pep_length)
        ls_ls.append(set(peplist))
    shared_peptide_list = list(set.intersection(*ls_ls))
    if excluded_aa == 'M':
        filtered_list = [n for n in shared_peptide_list if 'M' not in n]
    elif excluded_aa == 'P':
        filtered_list = [n for n in shared_peptide_list if 'P' not in n]    
    elif excluded_aa == 'C':
        filtered_list = [n for n in shared_peptide_list if 'C' not in n]            
    elif excluded_aa == 'MC':
        filtered_list = [n for n in shared_peptide_list if 'M' not in n and 'C' not in n]
    else:
        filtered_list = shared_peptide_list
    filtered_list1 = []
    for pep in filtered_list:
        if pep not in protein_for_other_genes:
            filtered_list1.append(pep)
    print gene,filtered_list1
    outputfile1.write(gene + '\t' + '\t'.join(filtered_list1) + '\n')