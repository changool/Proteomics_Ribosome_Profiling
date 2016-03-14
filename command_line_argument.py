import sys
import getopt

if len(sys.argv[1:])<=1:  ### Indicates that there are insufficient number of command-line arguments
    print "Warning! wrong command, please read the mannual in Readme.txt."
    print "Example: python trypsin.py --input input_filename --output output_filename --miss 1"
else:
    options, remainder = getopt.getopt(sys.argv[1:],'', ['input=',
                                                         'miss=',
                                                         'output='])
    for opt, arg in options:
        if   opt == '--input': input_file=arg
        elif opt == '--miss': n=int(arg)  #number of miss cleavage allowed
        elif opt == '--output':output_file=arg
        else:
            print "Warning! Command-line argument: %s not recognized. Exiting..." % opt; sys.exit()