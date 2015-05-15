#! /usr/bin/env python3.4
__author__ = 'ee364h05'

import sys
import os

def parseFile( filename ):
    #   Try openning file
    try:
        fileObj = open( filename, 'r' )
    #   Catch exception
    except IOError :
        print ( filename, " is not a readable file." )
        return

    #   Parse File
    lines = fileObj.readlines()
    for line in lines:
        sum = 0
        numInts = 0
        parts = line.split()
        printLine = []
        avg = ""
        for part in parts:
            try:
                #   Get integer and sum
                sum += int( part )
                numInts += 1
            except ValueError:
                printLine.append( part )
        if numInts != 0:
            avg = sum / numInts
            printStr = ' '.join( printLine )
            print( '{0:.3f}'.format( avg ), " ", printStr )
        else:
            printStr = ' '.join( printLine )
            print( printStr )

    #   Close file ptr
    fileObj.close()

#   Main
def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		parseFile( filename )
	else :
		print ( "Usage: Parse.py [filename];" )


if __name__ == "__main__" :
    main()
