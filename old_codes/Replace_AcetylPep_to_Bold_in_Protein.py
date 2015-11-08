#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

# python *.py [GeneSym|PepSeq] [RNAAcce|GeneSymbol|ProteinSeq] [Outputfile]

shellinput1 = str(sys.argv[1])
shellinput2 = str(sys.argv[2])
#shellinput3 = str(sys.argv[3])
inputfile1 = open (shellinput1, 'r')
inputfile2 = open (shellinput2, 'r')
#inputfile3 = open (shellinput3, 'r')
shelloutput = str(sys.argv[3])
outputfile = open (shelloutput,'w')

dic1 = {}
for num1, x in enumerate(inputfile1):
     xsplit = x.strip().split("|")
     genesym1 = xsplit[0].strip()
     pepseq1 = xsplit[1].strip()

#     genesym= xsplit[15].strip()
     dic1[pepseq1] = genesym1 

for num2, y in enumerate(inputfile2):
     ysplit = y.strip().split("|")
     rnaacc2 = ysplit[0].strip()
     genesym2 = ysplit[1].strip()
     pro2 = ysplit[2].strip()

     for k,v in dic1.iteritems():
        if v == genesym2:
           rep = "<<" + k.upper() + ">>"
           pro2 = pro2.replace(k,rep)
     pro2ls = pro2.split("^")
     for z in pro2ls:
        if "<<" in z:
           orf = z
           break
     result = rnaacc2 + "|" + genesym2 + "|" + orf + "\n"
     outputfile.write(result)

