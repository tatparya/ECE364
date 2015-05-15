#! /usr/bin/env python3.4
__author__ = 'ee364h05'

import sys
import os
import re
import vtools



#   Main
def main():
    print (sys.argv)
    if len(sys.argv) > 3:
        print( "Usage: verilog2vhdl.py [infile] [outfile]" )
        return 1

    #   Check if in file can be opened
    try:
        fin = open( sys.argv[1], 'r' )
        allLines = fin.readlines()
        outputStr = ""
        for line in allLines:
            try:
                out = vtools.parse_net( line )
                #   Parse lines from tuple
                component = out[0]
                instance = out[1]
                asList = out[3]

                outputStr += component + ": " + instance + "("
                for element in asList:
                    outputStr += element[0] + "=>" + element[1] + ", "

                outputStr = outputStr[:-2]
                outputStr += ";\n"

            catch ValueError:
                print( "Error: input file is not a valid Verilog port map!")
                return 4


    except IOError:
        print IOError
        return 2

    #   Check if out file can be opened
    try:
        fout = open( sys.argv[2], 'r' )
        fout.write( outputStr )
    except IOError:
        print IOError
        return 3



#   Main
if __name__ == "__main__" :
    main()