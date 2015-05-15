#! /usr/bin/env python3.4
__author__ = 'ee364h05'

import sys
import os
import string
import glob
import filecmp

def getLargestProduct():
	maxProduct = 0
	with open("Number Grid.txt", 'r') as inputFile:
		#	Read all lines
		allLines = inputFile.readlines()	
		#	for every line take four numbers and find product
		for line in allLines:
			numbers = line.split()
			length = len( numbers )
			i = 1;
			while i < length - 4:
				newList = [ numbers[i], numbers[i+1], numbers[i+2], numbers[i+3] ]
				product = getListProduct( newList )
				if product > maxProduct:
					maxList = newList
					maxProduct = product
					orientation = "Horizontal"
				i += 1
			#print maxProduct
		#	For every column four elements and calculate the product
		
		while i < length:
			newList = []
			for line in allLines[:-4]:
				numbers = line.split()
				j = 0
				newList = []
				while j < 4:
					newList.append(numbers[i])
					j += 1
			i += 1
			product = getListProduct( newList )
			if product > maxProduct:
				maxList = newList
				maxProduct = product
				orientation = "Vertical"
			i += 1
			#print maxProduct
	final = ( maxList, maxProduct, orientation )
	#print final
	return final
	
def partition( numList, n ):
	i = 0
	splitList = []
	newList = []
	length = len(numList)
	j = 0
	while j < length - n + 1:
		newList = []
		i = 0
		while i < n:
			newList.append(numList[i+j])
			i+=1
		splitList.append(newList)
		j+=1
	#print splitList
	return splitList
	
def getListProduct( numList ):
	product = 1
	for num in numList:
		product *= int(num)
		
	return product
	
def getLargestPartition( numList, n ):
	max = 1;
	allList = partition( numList, n )
	for element in allList:
		product = int(element[0]) * int(element[1])
		if product > max:
			max = product
			maxList = element
	ret = (element, max)
	return ret
	
###########PART 2########

def getDirectory():
	phoneDict = {}
	with open("Phone Directory.txt", 'r') as inputFile:
		#	Read all lines
		for line in inputFile:
			oneLine = line.split()
			#print oneLine
			firstname = oneLine[2]
			mi = oneLine[1]
			lastname = oneLine[0]
			phoneNum = oneLine[3]+oneLine[4]
			entry = ( firstname, mi, lastname )
			phoneDict[ entry ] = phoneNum
	
	return phoneDict
	
def getPhoneByPartialName( partialName ):
	phoneDict = getDirectory()
	allKeys = phoneDict.keys()
	peopleList = []
	for key in allKeys:
		if partialName in key:
			person = phoneDict[key]
			peopleList.append(person)
	#print peopleList
	return peopleList
	
def reverseLookup( areaCode ):
	peopleList = []
	phoneDict = getDirectory()
	for element in phoneDict.items():
		#print element
		
		key = element[0]
		#print key
		value = element[1]
		area = value.split(')')[0][1:]
		#print area
		#print areaCode
		if int(area) == int(areaCode):
			peopleList.append(key)
			#print "YES!!"
		
	#print peopleList
	return peopleList
			
def main():
	#getDirectory()
	#getPhoneByPartialName( "Stephanie" )
	#reverseLookup ( 512 )
	doSomething = 0
	#getLargestPartition( [ 2,1,4,3], 2 )

if __name__ == "__main__" :
    main()

