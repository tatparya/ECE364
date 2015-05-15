#! /usr/bin/env python3.4
__author__ = 'ee364h05'


import sys
import os
import string
import re

def runEmail( filename ):
	message = "Error"
	#r"def\s+(([a-z]|[A-Z])(\w|-|_)+)\(((.*),?)\)"
	pattern = r"def\s+(([a-z]|[A-Z])(\w|-|_)+)\((.*)\)"
	if os.path.exists(filename) and os.R_OK:
		with open( filename, 'r' ) as inputfile:
			for line in inputfile:
				match = re.findall( pattern, line )
				matchList = []
				if match:
					for obj in match:
						for thing in obj:
							matchList.append( thing )
					funcName = matchList[0]
					print funcName
					arguments = matchList[-1].split(',')
					argList = []
					for argument in arguments:
						argList.append( argument.strip() )
					length = len( argList )
					i = 0
					while i < length:
						print "Arg" + str(i + 1) + ": " + str(argList[i])
						i += 1
	else:
		print message + ": Cannot read " + filename

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		runEmail( filename )
	else :
		print "Usage: function_finder.py"
		

if __name__ == "__main__" :
    main()

#if __name__ == "__main__":
#    if len(sys.argv) == 2:
#        inputFileName = sys.argv[1]
#    else:
#        inputFileName = "somefile.txt"
    # Work with your input file ...
