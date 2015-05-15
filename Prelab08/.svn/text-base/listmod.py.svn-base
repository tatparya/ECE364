#! /usr/bin/env python3.4
__author__ = 'ee364h05'

import sys
import os

#   Fuction definition
def find_median( list1, list2 ):
    #   Merge the two lists
    mergedList = []
    for item in list1:
        mergedList.append( item )
    for item in list2:
        mergedList.append( item )

    #   Sort the merged list
    mergedList.sort()

    #   Find the median
    length = len( mergedList )
    medianIndex = int( ( length - 1 ) / 2 )
    median = mergedList[ medianIndex ]

    #   Create and return Tuple
    retTuple = ( median, mergedList )

    return retTuple
