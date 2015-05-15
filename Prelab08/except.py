#! /usr/bin/env python3.4
__author__ = 'ee364h05'

import sys
import os

def calcSum( inString ):
    #   Parse string to find floats and add
    sum = 0
    for item in inString.split():
        #   Try conversion
        try:
            sum += float( item )
        #   Catch exception
        except ValueError:
            pass

    return sum

#   Main
def main():
    inString = input( "Please enter some values: " )

    sum = calcSum( inString )
    print ( "The sum is: ", sum )

#   Main
if __name__ == "__main__" :
    main()