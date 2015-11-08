# Last editted on 8/1/2015
#!/usr/bin/python
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import time
#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')
#args = parser.parse_args()


#python thisfile.py [gene2accession] [input fasta file] [output fasta file]

inputfile1 = open (sys.argv[1], 'r')#gene2accession_hs
inputfile2 = open (sys.argv[2], 'r')#input fasta
outputfile = open (sys.argv[3], 'w')

dic = {}
start=time.clock()
for num, y in enumerate(inputfile1): 
    y_ls = y.split("\t")
    rnaacc = y_ls[5].split(".")
    rnaacc1 = rnaacc[0].strip()
    genesym = y_ls[15].strip()
    dic[rnaacc1] = genesym

for num, x in enumerate(SeqIO.parse(inputfile2,"fasta")):
     if num%5000 == 0:
        print num
     header = x.description
     pro = str(x.seq)
     seqid = x.id
     try:
        header_ls = header.split("|")
        des = header_ls[4].strip()
        acc1 = header_ls[3].split('.')
        acc = acc1[0]

        genesym1=dic.get(acc)
        if genesym1 == None:
           genesym1 = 'NONE'
           print x,'does not have matching gene'


        newheader = seqid + " " + acc + "#" + genesym1 +"#"+ des

        result = ">" + newheader + "\n" + pro + "\n"
     except:   
        result = ">" + header + "\n" + pro + "\n"
        print "failed for", x
     outputfile.write(result)

end=time.clock()
print end - start