#!/usr/bin/python
# This code extract gi_accession number, protein sequence and length information from fasta database
#argv[1]: fasta database
#argv[2]: output file
import sys
#import argparse

#parser=argparse.ArgumentParser(description='python ***.py input_file database_file output_file')

#args = parser.parse_args()

#shellinput = raw_input('Please type your input file name!\n')
shellinput = str(sys.argv[1])
#shellinput1 = str(sys.argv[2])
read = open (shellinput, 'r')
#read1= open (shellinput1, 'r')
#shelloutput = raw_input('Please type your output file name for over100\n')
#shelloutput =str(sys.argv[2])
#maxsize = input('please type the AA length cutoff \n')
#maxsizenumber = str(maxsize)
#shelloutput = str( 'over' + maxsizenumber + '.txt')
shelloutput = str(sys.argv[2])
#oversizelimit = open (shelloutput,'w')
outputfile = open (shelloutput,'w')
#import temfile

#pep = open ('peptide.txt', 'w')
#length = open ('peptide_len.txt', 'w')
#result = open ('output.txt', 'w')
#rightsize = 0
#small = 0
#big = 0
#total = 0
#bigger_than_sizelimit = 0

for x in read:
  x_strip = x.strip() 
  if '>' in x_strip:
       firstline = x_strip.split("|")
       gi = firstline[1]
       acce = firstline[3]
       seq = read.next()
#       seq_strip =seq.strip()
#       lenth = len(seq)
#       lenth_str = str(lenth)
#       print seq_strip
       result = gi.strip() + "|" + acce.strip() + "|" + seq.strip() + '\n'
#       print result
       outputfile.write(result)
#       sequence = read1.next()
#       sequence_strip = sequence.strip()
#       print y_strip
#       if x_strip in sequence_strip:
#          print x_strip
#          print sequence_strip
#          print y_strip

#          result = x_strip +"|"+ y_strip + ";"
          
#          resultsave.write(result)
#  outputfile.write(resultsave)
#  print resultsave


#    input1_array = y.split("|")
#       input1_acce = input1_array[1]
#       input1_acce_strip = input1_acce.strip()
#       seq = read1.next()
#       seq_strip = seq.strip()
#       print seq_strip
#       break
#       seqdic[input1_acce_strip]=seq_strip
#       print seqdic
#       print seqdic.values()
          

# for x in read:
#       print x
#    z = x
#    for y in read1:
#       x_strip = x.strip()
#       input_array=x_strip.split("|")
#       input_acce=input_array[0] 
#       print input_acce
#       input_acce_strip=input_acce.strip()
#       print input_acce_strip
#       input_seq=input_array[1]
#       input_seq_strip = input_seq.strip()
#       print input_seq_strip
#       x_strip=x.strip()
       
#       if x_strip in seqdic.values():
#            acce = seqdic.get(x_strip)
#            print seq_strip
#            print seqdic.values()
#            break
#         if seq.count(input_seq) > 0:  
#            protein_seq = seqdic.values()
#            print protein_seq
#            print input_seq
#            print protein_seq
#            print input_seq
#            position = protein_seq.find(input_seq_strip)
#            print position
#          to_outputfile = x_strip +"|"+ y_strip + '\n'
 #         print to_outputfile
  #        outputfile.write(to_outputfile)



#    for y in read1:
#      if '>' in y:
 #          input1_array=y.split("|")
 #          input1_acce=input1_array[1]
 #          if input_acce == input1_acce:
 #                     seq = read1.next()
 #                     position = seq.find(input_seq)
 #                     z_position = z + str(position)
 #                     outputfile.write(z_position) 
                                    
     

#  if '>' in x:
#       array=x.split("|")
#       proteinID = x
#  elif '>' not in x: 
#     if   len(x) <= 36:                       
#              rightsize += 1
#              total += 1
#     elif len(x) > 36:
#              big += 1
#              total += 1
#     elif len(x) < 6:
#              small += 1
#              total += 1
#     elif len(x) > maxsize:
#             bigger_than_sizelimit +=1
#              oversizelimit.write(proteinID)
#              oversizelimit.write(x)
#              total += 1
#     elif len(x) > 36:
#              big += 1
#              total += 1


#print '6 to 36 is     ',rightsize,' ',100*rightsize/total,'%'
#print '6< is          ',small,' ',100*small/total,'%'
#print '36> is         ',big,' ',100*big/total,'%'
#print '6< + 36> is    ',small+big,' ',100*(small+big)/total,'%'
#print '>sizelimit is  ',bigger_than_sizelimit,' ',round(100.00*bigger_than_sizelimit/total,3), '%'
#print 'total number is',total
#print 'peptide bigger than 100',peptide_bigger_than_100

