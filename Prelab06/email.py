#! /usr/bin/env python3.4
__author__ = 'ee364h05'


import sys
import os
import string
import re

def runEmail():
	repl = "@ecn.purdue.edu"
	pattern = r"(\w+)(@)purdue.edu\s+(\d+\.\d+)"
	with open('Part2.in', 'r') as inputs:
		for line in inputs:
			match = re.search( pattern, line )
			if match:
				result = match.group(1) + repl + "\t" + match.group(3) + "/100"
				print result

def main():
	runEmail()	

if __name__ == "__main__" :
    main()

