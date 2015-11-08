#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

# python *.py [GeneSym|PepSeq|PSM] [RNAAcce|GeneSymbol|ProteinSeq] [Outputfile]

inputfile1 = open (sys.argv[1], 'r')
inputfile2 = open (sys.argv[2], 'r')
#inputfile3 = open (sys.argv[3], 'r')
outputfile = open (sys.argv[3],'w')


for num2, y in enumerate(inputfile2):
     ysplit = y.strip().split("|")
     rnaacc2 = ysplit[0].strip()
     genesym2 = ysplit[1].strip()
     pro1 = ysplit[2].strip()
     pro2 = pro1.upper()

     for num1, x in enumerate(inputfile1):
        x_ls = x.split("|")
        genesym1 = x_ls[0].strip()
        pepseq1 = x_ls[1].strip()
        psm1 = x_ls[2].strip()
        if genesym1 == genesym2:
           fontsize = int(psm1)/2 + 2
           rep = '<font size="' + str(fontsize) + '" color="red">' + pepseq1.upper() + '</font>'
           pro2 = pro2.replace(pepseq1,rep)
     inputfile1.seek(0)
     pro2ls = pro2.split("^")
     print pro2ls
#     pro2lslen = len(pro2ls)
#     orf = pro2ls[pro2lslen -1]
     for z in pro2ls:
        orf = "" 
        if "font" in z:
           orf = z
           break
     for num3, za in enumerate(orf):
        if za.upper() == "M":
           break

     nterm = orf[:num3]
     cterm = orf[num3:]
     newpro2 = nterm + '<font size="4" color="blue">*</font>' + cterm           
       
     result = rnaacc2 + "#" + genesym2 + "#" + newpro2 + "\n" 
     outputfile.write(result)

