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
            print 'XXX.py --input <input_fasta_file> --output <output_file> --enzyme <enzyme_to_be_used> --miss <number_of_missed_cleavage_allowed> --min_length <minimum_length_of_peptide> --max_length <maximum_length_of_peptide> --excluded_aa <None, M, P or MP> --gene_symbol <file_for_gene_symbols>'
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
#outputfile1 = open(output_file,'w')

from pyteomics import parser
from pyteomics import mass


#gene_list = ['SAA1']
#gene_list = open(gene_list,'r')
counter = 0
errcounter = 0
pepinput = 'MALTSEYWIILR'
ps0 = parser.parse(pepinput, show_unmodified_termini=True)
referencemass = mass.calculate_mass(parsed_sequence=ps0)
mass_tolerance = 7 # unit: ppm
targetmass = 1422.730378
total_pep_list = []
for num,x in enumerate(SeqIO.parse(inputfile01,'fasta')):
    if num%10000==0:print num
    #if num > 5000:
    #    break
    pro = str(x.seq)
    peplist = digest(pro,enzyme,missed_cleavage,min_pep_length,max_pep_length)
    if len(peplist) > 0:
        for p in peplist:
            total_pep_list.append(p)
sort_list = list(set(total_pep_list))
for num1,pep in enumerate(sort_list):

        if num1%10000 == 0:print num1,counter
        try:
            ps = parser.parse(pep, show_unmodified_termini=True)
            pepmass = mass.calculate_mass(parsed_sequence=ps)
        except:
            print pep
            continue    
        if pepmass > 0:

        
            if float(pepmass) >= referencemass-referencemass*(mass_tolerance/1000000) and float(pepmass) <= referencemass+referencemass*mass_tolerance/1000000:
               counter += 1
print 'the number of peptide is ',counter