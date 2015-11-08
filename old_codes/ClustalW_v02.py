#!/usr/bin/python

import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
from Bio.Align.Applications import ClustalOmegaCommandline
#from Bio.Align.Applications import ClustalwCommandline

#inputfile1 = open(sys.argv[1],'r') # fasta file
inputfile2 = open(sys.argv[1],'r') # homologen numbering

#dic = {}
#for x in SeqIO.parse(inputfile1,'fasta'):
#    header = x.description
#    seq = str(x.seq)
#    header_ls = header.split('|')
#    pepseq = header_ls[5]
#    header_seq = '>' + header + '\n' + seq
#    dic[header_seq] = pepseq
    
for y in inputfile2:
    y_sp = y.strip()
    #app = []
    #for k,v in dic.iteritems():
    #    if v == y_sp:
    #        app.append(k)
    #sorted_app = sorted(app)
    #outfile = '\n'.join(sorted_app)
#    outputfilename = y_sp + '.fasta'
#    outputfile = open(outputfilename,'w')
#    outputfile.write(outfile)

#cline = ClustalwCommandline("clustalw", infile='UTR_acetyl_pep_homolog_test.fasta')
#cline()


    in_file = y_sp + ".fasta"
    out_file = y_sp + "_aligned.txt"
    clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
    clustalomega_cline()
