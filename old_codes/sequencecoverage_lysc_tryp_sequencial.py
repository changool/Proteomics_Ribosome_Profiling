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
	   print 'test.py -i <inputfile> -o <outputfile>'
	   sys.exit(2)
	for opt, arg in opts:
	   if opt == '-h':
	      print 'test.py -i <inputfile> -o <outputfile>'
	      sys.exit()
	   elif opt in ("-i", "--ifile"):
	      inputfile = arg
	   elif opt in ("-o", "--ofile"):
	      outputfile = arg
#   print 'Input file is "', inputfile
#   print 'Output file is "', outputfile


	#shellinput = raw_input('Please type your input file name!\n')
	#shellinput1 = str(sys.argv[1])
	#shellinput2 = str(sys.argv[2])
	inputfile1 = open(inputfile, 'r')
	#inputfile2 = open (shellinput2, 'r')
	#shelloutput = raw_input('Please type your output file name for over100\n')
	#shelloutput =str(sys.argv[2])
	#maxsize = input('please type the AA length cutoff \n')
	#maxsizenumber = str(maxsize)
	#shelloutput = str( 'over' + maxsizenumber + '.txt')
	#shelloutput = str(sys.argv[2])
	#oversizelimit = open (shelloutput,'w')
	outputfile1 = open(outputfile,'w')
	#import temfile
	app = []
	for num, x in enumerate(SeqIO.parse(inputfile1,"fasta")):
	   dic = {}
	   p = str(x.seq)
	   pep = p.strip()
	   i = 0   
	   while i <= len(pep)-1:
	      dic[i] = 0
	      i += 1
	#      print len(pep), i
#LysC
#	   pep_rep2 = pep_rep1.replace("KP","X|")
           pep_rep2 = pep
	   pep_rep3 = pep_rep2.replace("K","K|")
	   if pep_rep3[-1] == "|":
	       pep_rep3 = pep_rep3[:-2]
	   pep_enz = pep_rep3.split("|")
	   for y in pep_enz:
	      pep_len = len(y)     
	      if pep_len >= 6 and pep_len <= 40:
		 pep_pos = pep.find(y)
		 for key,value in dic.iteritems():
		     if key >= pep_pos and key <= pep_pos + pep_len -1:
			  dic[key] += 1

#Trypsin sequential	      
              elif pep_len >= 41:
                   #pep01 = pep.replace("KP","XP")
                   pep02 = pep.replace("RP","YP")
                   #pep_rep01 = y.replace("KP","XP")
                   #pep_rep02 = pep_rep01.replace("RP","YP")
                   pep_rep02 = y.replace("RP","YP")
		   #pep_rep03 = pep_rep02.replace("K","K|")
		   pep_rep04 = pep_rep02.replace("R","R|")
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
	   printout = str(num) +  " sequence coverage is " + str(seq_coverage) + " %" + "\r"
	   printout1 = str(num)+"|" + x.id +"|" + str(seq_coverage) + " %" + "\n"
	   sys.stdout.write(printout)
	   sys.stdout.flush()
	   app.append(seq_coverage)
           outputfile1.write(printout1)

	finalcov = "total average for sequence coverage is " + str(numpy.mean(app)) + " %"
	print finalcov 
        outputfile1.write(finalcov)

if __name__ == "__main__":
   main(sys.argv[1:])
