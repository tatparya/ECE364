#! /usr/bin/env python3.4
__author__ = 'ee364h05'

import sys
import os
import listmod

merged = 0
medianFound = 0
list1 = []
list2 = []

i1 = input( "Enter the first list of numbers: " )
i2 = input( "Enter the second list of numbers: " )

#   Convert input to two lists
l1 = i1.split()
l2 = i2.split()

#   Convert to list of integers
for item in l1:
    list1.append( int(item) )

for item in l2:
    list2.append( int(item) )

#   Call for merge function
( Median, Sorted_List ) = listmod.find_median( list1, list2 )
medianFound = 1

#   Output statements
print( "First list: ", list1 )
print( "Second list: ", list2 )

if medianFound == 0:
    print( "Merged list: Not implemented" )
    print( "Median: Not Implemented" )

else:
    print( "Merged list: ", Sorted_List )
    print( "Median:", Median )


