#! /usr/bin/env python3.4
__author__ = 'ee364h05'


import sys
import os
import string
import re

def runEmail( filename ):
	pattern = r"(0{0,2}\d+)\.(0{0,2}\d+)\.(0{0,2}\d+)\.(0{0,2}\d+):(\d+).*"
	invalidIP = 0
	invalidPort = 0
	required = 0
	required = 0
	with open( filename, 'r') as inputs:
		for line in inputs:
			match = re.match( pattern, line ) 
			if match:				
				i = 1
				invalidIP = 0
				invalidPort = 0
				required = 0
				while i <= 4:
					if not int(match.group(i)) <= 255 :
						invalidIP = 1
					i += 1
				if not int(match.group(5)) <= 32767:
					invalidPort = 1
				if int(match.group(5)) <= 1024:
					required = 1;
			else:
				print "No matches found"
			if invalidIP:
				message = "Invalid IP Address"
			elif invalidPort:
				message = "Invalid Port Number"
			elif required:
				message = "Valid (root privileges required )"
			else:
				message = "Valid"
		
			print match.group() + " " + message	
	

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	else :
		print "Invalid num args"
	runEmail( filename )	

if __name__ == "__main__" :
    main()

#if __name__ == "__main__":
#    if len(sys.argv) == 2:
#        inputFileName = sys.argv[1]
#    else:
#        inputFileName = "somefile.txt"
    # Work with your input file ...
