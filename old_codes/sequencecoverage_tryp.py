#!/usr/bin/python
import numpy
import sys, getopt
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from collections import Counter
def main(argv):
	#inputfile = ''
	#outputfile = ''
	try:
	   opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
	   print 'test.py -i <inputfile1> -o <outputfile1>'
	   sys.exit(2)
	for opt, arg in opts:
	   if opt == '-h':
	      print 'test.py -i <inputfile1> -o <outputfile1>'
	      sys.exit()
	   elif opt in ("-i", "--ifile"):
	      inputfile1 = arg
	   elif opt in ("-o", "--ofile"):
	      outputfile1 = arg
#   print 'Input file is "', inputfile
#   print 'Output file is "', outputfile


	#shellinput = raw_input('Please type your input file name!\n')
	inputfile1 = str(sys.argv[1])
#	inputfile2 = str(sys.argv[2])
	inputfile01 = open(inputfile1, 'r')
#	inputfile02 = open(inputfile2, 'r')
	#shelloutput = raw_input('Please type your output file name for over100\n')
	#shelloutput =str(sys.argv[2])
	#maxsize = input('please type the AA length cutoff \n')
	#maxsizenumber = str(maxsize)
	#shelloutput = str( 'over' + maxsizenumber + '.txt')
	outputfile1 = str(sys.argv[2])
	outputfile01 = open(outputfile1,'w')
	outputfile2 = str(sys.argv[3])
	outputfile02 = open(outputfile2,'w')
	#import temfile
	app = []
	for num, x in enumerate(SeqIO.parse(inputfile01,"fasta")):
	   dic = {}
	   p = str(x.seq)
	   pep = p.strip()
	   i = 0   
	   while i <= len(pep)-1:
	      dic[i] = 0
	      i += 1

#Trypsin 	      
              
	   pep01 = pep.replace("KP","XP")
	   pep02 = pep01.replace("RP","YP")
	   pep_rep03 = pep02.replace("K","K|")
	   pep_rep04 = pep_rep03.replace("R","R|")
	   if pep_rep04[-1] == "|":
	       pep_rep04= pep_rep04[:-2]
	   pep_enz01 = pep_rep04.split("|")
	   for y01 in pep_enz01:
	      pep_len01 = len(y01)     
	      if pep_len01 >= 6 and pep_len01 <= 40:
		 pep_pos01 = pep02.find(y01)
		 for key,value in dic.iteritems():
		     if key >= pep_pos01 and key <= pep_pos01 + pep_len01 -1:
			  dic[key] += 1




	   zero = Counter(dic.values())
	   noncovered = zero[0]
	   seq_coverage = 100*(len(pep)-int(noncovered))/len(pep)
           if seq_coverage <= 20:
               lowcov =   str(seq_coverage)+"|"+x.description +"\n"
               outputfile02.write(lowcov)
	   printout = str(num) +  " sequence coverage is " + str(seq_coverage) + " %" + "\r"
	   printout1 =  str(seq_coverage) + "#" + x.description + "\n"
	   sys.stdout.write(printout)
	   sys.stdout.flush()
	   app.append(seq_coverage)
           outputfile01.write(printout1)

	finalcov = "total average for sequence coverage is " + str(numpy.mean(app)) + " %"
	print finalcov 
        outputfile01.write(finalcov)

if __name__ == "__main__":
   main(sys.argv[1:])
