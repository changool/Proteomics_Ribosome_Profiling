#!/usr/bin/python
def main():
	import sys
	from Bio.Seq import Seq
	from Bio.Alphabet import IUPAC
	from Bio import SeqIO
	import os
	
	from classes.A_v01 import class_a
	from classes.B_v01 import class_b 
	from classes.C_v01 import class_c
	from classes.D_v01 import class_d
	from classes.E_v01 import class_e
	from classes.F_v01 import class_f
	from classes.G_v01 import class_g
        inputfile1 = open (sys.argv[1], 'r') # fasta file for mRNA
	inputfile2 = open (sys.argv[2], 'r') # mRNA_accession|Peptide_Seq|PSM
	inputfile3 = open (sys.argv[3], 'r') # RiboSeq data

        inputlist1 = []
        for x in SeqIO.parse(inputfile1,"fasta"):
            header = x.description
            seq = str(x.seq)
            inputlist1.append(header + '@' + seq)
            
        inputlist2 = []
        for y in inputfile2:
            inputlist2.append(y.strip())
            

        A = class_a(inputlist1,inputlist2)    
	class_a_out = A.a() # Fasta database for RNA seq, mRNA_accession|Peptide seq|PSM -> generate mRNA fasta file for peptides
        B = class_b(class_a_out)
	class_b_out = B.a() # Fasta database for RNA seq -> Fetch chromosome coordinate for nucleotide of mRNA

        inputlist3 = []
        for z in inputfile3:
            inputlist3.append(z.strip())
	
	C = class_c(class_b_out,inputlist3)
	class_c_out = C.a() # Fasta file for mRNA, Ribo Seq data -> Fetch RiboSeq data
	
	D = class_d(class_a_out,inputlist2)
	class_d_out = D.a() # Fasta database for RNA seq, mRNA_accession|Peptide seq|PSM -> peptide position in mRNA
	
	E = class_e(class_d_out)
	class_e_out = E.a() # peptide positon in mRNA -> peptide start position
	
	F = class_f(class_c_out,class_d_out)
	class_f_out = F.a() # chromosome coordinate and RiboSeq of mRNA sequences, peptides position in mRNA -> Chromosome Coordinate, RiboSeq and PSM

        if not os.path.exists('cano_anno'):
            os.makedirs('cano_anno')
        if not os.path.exists('cano_down'):
            os.makedirs('cano_down')
        if not os.path.exists('noncano_orf'):
            os.makedirs('noncano_orf')
        if not os.path.exists('noncano_utr'):
            os.makedirs('noncano_utr')
        if not os.path.exists('unclassified'):
            os.makedirs('unclassified')

        leftside = 30 # number of amino acid from the start position of acetylated peptide to the left side
        rightside = 90 # number of amino acid from the start position of acetylated peptide to the right side
 
        G = class_g(class_e_out,class_f_out,inputlist2,leftside,rightside)
        G.a() # peptide start position, coor|RiboSeq|PSM, peptide list, leftside of figure, right side of figure -> generate figures

	
if __name__ == '__main__':
    main()
