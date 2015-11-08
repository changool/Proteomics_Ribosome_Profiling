from termcolor import colored
import sys

outputfile = open(sys.argv[1], 'w')


color = colored('hi','red')
result= "how"+ color+"are you"
outputfile.write(result)
