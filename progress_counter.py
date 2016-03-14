import sys
import time
from Bio import SeqIO

def line(inputfile,filetype):
        print 'Counting number of lines for input file'
        if filetype == "fasta":
            num_lines = sum(1 for line in SeqIO.parse(inputfile,'fasta'))

        else:
            num_lines = sum(1 for line in inputfile)
        try:
            inputfile.seek(0)
        except:
            print 'seek(0) did not work'
        global onepercent
        onepercent=round(num_lines/100,0)
        return onepercent
def prog(number,onepercent):
        if number%onepercent == 0:
            progress = int(number/onepercent)
            sys.stdout.write("progress: %d %%   \r" %(progress) )
            sys.stdout.flush()
