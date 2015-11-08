#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

# python *.py [GeneSym|PepSeq] [RNAAcce|GeneSymbol|ProteinSeq] [Outputfile]

shellinput1 = str(sys.argv[1])
#shellinput2 = str(sys.argv[2])
#shellinput3 = str(sys.argv[3])
inputfile1 = open (shellinput1, 'r')
#inputfile2 = open (shellinput2, 'r')
#inputfile3 = open (shellinput3, 'r')
#shelloutput = str(sys.argv[3])
#outputfile = open (shelloutput,'w')

dic1 = {}
for num1, x in enumerate(inputfile1):
     xsplit = x.strip().split("|")
     genesym1 = xsplit[0].strip()
     pepseq1 = xsplit[1].strip()

#     genesym= xsplit[15].strip()
     dic1[pepseq1] = genesym1 

for k,v in dic1.iteritems():
     
     if v == "GDI1":
        print v 
#           rep = "<<" + v.upper() + ">>"
#           pro2 = pro2.replace(v,rep)

