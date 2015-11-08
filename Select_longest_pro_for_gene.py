#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()


inputfile1 = open (sys.argv[1], 'r')
inputfile2 = open (sys.argv[2], 'r')
#inputfile3 = open (sys.argv[3], 'r')
outputfile = open (sys.argv[3],'w')


for num1, y in enumerate(inputfile1): # gene list
     if num1%100 == 0:
        print num1
     gene1 = y.strip()
     genels = []
     dic = {}
     for num2, x in enumerate(SeqIO.parse(inputfile2,"fasta")):
        header = x.description
        headerls = header.split(" ")
        accgene = headerls[1].split("#")
        gene2 = accgene[1].strip()
        proseq = str(x.seq)
        if gene2 == gene1:
           prolen = len(proseq)
           header_seq = header + "@" + proseq
           dic[header_seq] = [prolen]
#           print prolen
           continue 
     prolenmax = max(dic,key=dic.get)
     prolenmax_ls = prolenmax.split("@")

     result = ">" +  prolenmax_ls[0] + "\n" + prolenmax_ls[1] + "\n"
#     print len(prolenmax_ls[1])
#     print result
     outputfile.write(result)
     inputfile2.seek(0)
                    

