#!/usr/bin/python
# This code takes file [peptide1|gi_accession1|protein_length1;peptide1|gi_accesion2|protein_length2;...] and gives gi accession number with largest protein and peptide position on the protein
# argv1: database [peptide1|gi_accession1|protein_length1;peptide1|gi_accession2|protein_length2;...]
# argv2: output file [peptide1|gi_accession?|protein_length_of_largest_one|position_of_pep]
import sys
import fnmatch
import string
import operator

inputfile1 = open(sys.argv[1],'r')
outputfile = open(sys.argv[2],'w')

for x in inputfile1:
    x_rcut = x[:-2]
    print x_rcut
    x_strip = x_rcut.strip()
    m1aa_pep_id_len_pos = x_strip.split(";")
    dic = {}

    for y in m1aa_pep_id_len_pos:
        y_strip = y.strip()
        y_split = y_strip.split("#")
        pos = y_split[4].strip()
        dic[y_strip] = pos

    min_result = min(dic,key=dic.get) + ";"
    max_result = max(dic,key=dic.get) + "\n"
    outputfile.write(min_result)
    outputfile.write(max_result)
