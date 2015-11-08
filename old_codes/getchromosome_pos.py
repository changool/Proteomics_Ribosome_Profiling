from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import sys
shelloutput =  str(sys.argv[3])
outputfile = open(shelloutput, 'w')
 

f={}
if len(sys.argv)<2:
	print "USAGE:python getchromosome_pos.py chromosome.fasta inputfile outputfile"
else:
	for each in SeqIO.parse(open(sys.argv[1]),"fasta"):
	
	
id=each.description
		sequence=str(each.seq)
                sequence_strip = sequence.strip()
                sequence_upper = sequence_strip.upper()
		f[id]=sequence_upper
	
	
	
	for i in open(sys.argv[2]):
                dna_for = i.strip()
                dna_for_seq = Seq(dna_for)
                dna_rev = str(dna_for_seq.reverse_complement())
                for key,value in f.iteritems():
                        counter = 0     
			if dna_for in value:
                                counter += 1
                          
				result = dna_for +"\t"+key.strip() + "\t" + "forward" + "\t" +str(value.index(dna_for)+1)+"\t"+str(value.index(dna_for)+len(dna_for))
				print result
                                outputfile.write(result)                                
                                break
		        elif dna_rev in value:
                                counter += 1
                          
				result = dna_for +"\t"+key.strip() +"\t" + "reverse" +"\t" + str(value.index(dna_rev)+1)+"\t"+str(value.index(dna_rev)+len(dna_rev))
				print result
                                outputfile.write(result)                                
                                break
                if counter == 0:       
 				result1 = dna_for +"\t" + "no matching sequence"
				print result1
                                outputfile.write(result1)                                
 
