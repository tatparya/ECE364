#! /usr/bin/env python3.4
__author__ = 'ee364h05'


import sys
import os
import string
import re

def convertToAttrib( ):
	filename = "points.xml"
	LongString = ""
	outFilename = "points_out.xml"
	with open( filename, 'r' ) as inputFile:
		content = inputFile.readlines()
		#for line in content:
	LongString = LongString.join(content)
	PointList = LongString.split("<point>")
	OutFile = open( outFilename, 'w' )
	#print PointList
	for point in PointList:
		matchID = re.findall( r"<ID>(.*)</ID>", point )
		matchY = re.findall( r"<Y>(.*)</Y>", point )
		matchX = re.findall( r"<X>\n *(.*)\n", point )
		
		if matchID:
			#print "MAtched"
			#print matchX[0]
			#print matchY[0]
			#print matchID[0]
			writeLine = '\t<point ID="' + matchID[0] + '" X="' + matchX[0] + '" Y="' + matchY[0] + '" />' + '\n'
			#writeLine = '<point ID=""{}"" X=""{}"" Y=""{}"" />'.format( matchID[0], matchX[0], matchY[0] )
			OutFile.write( writeLine )
		else:
			OutFile.write( point[:-3] )
			
			
		#r"<X>(\n)?\w*(.*?)(\n)?\w*</X>"
	OutFile.write( "</coordinates>\n" )

def getEntireFile():
	filename = "books.xml"
	LongString = ""
	with open( filename, 'r' ) as inputFile:
		content = inputFile.readlines()
		#for line in content:
	LongString = LongString.join(content)
	BookList = LongString.split("</book>")
	return LongString

def getGenres( ):
	allFile = getEntireFile()
	BookList = allFile.split("</book>")
	genres = re.findall( r"<genre>(.*)</genre>", allFile )
	#print genres
	genres.sort()
	genreSet = set(genres)
	#print genreSet
	finalList = list( genreSet )
	finalList.sort()
	#print finalList
	return finalList

def getAuthorOf( bookName ):
	allFile = getEntireFile()
	bookList = allFile.split("<book")
	#print bookList
	for book in bookList:
		matchTitle = re.findall( r".*<title>(.*)</title>.*", book )
		if matchTitle:
			#print matchTitle
			if bookName == matchTitle[0]:
				#print "Matched! Find the author"
				matchAuthor = re.findall( r".*<author>(.*)</author>.*", book )
				#print matchAuthor[0]
	if matchAuthor[0]:
		return matchAuthor[0]
	else:
		return None

def getBookInfo( bookID ):
	allFile = getEntireFile()
	bookList = allFile.split("<book")
	#print bookList
	exists = 0
	for book in bookList:
		matchID = re.findall( r".*id=\"(.*)\">.*", book )
		if matchID:
			#print matchID
			if bookID == matchID[0]:
				exists = 1
				#print "Matched! Find the author AND TITLE"
				matchTitle = re.findall( r".*<title>(.*)</title>.*", book )
				matchAuthor = re.findall( r".*<author>(.*)</author>.*", book )
				#print matchAuthor[0]
				#print matchTitle[0]
				retTuple = ( matchTitle[0], matchAuthor[0] )
	#	Return
	if exists:
		#print retTuple
		return retTuple
	else:
		return None

def getBooksBy( authorName ):
	allFile = getEntireFile()
	bookList = allFile.split("<book")
	retList = []
	#print bookList
	for book in bookList:
		matchAuthor = re.findall( r".*<author>(.*)</author>.*", book )
		if matchAuthor:
			#print matchTitle
			if authorName == matchAuthor[0]:
				#print "Matched! Find the author"
				matchTitle = re.findall( r".*<title>(.*)</title>.*", book )
				retList.append( matchTitle[0] )
				#print matchAuthor[0]
	#print retList
	return retList

def getBooksBelow( bookPrice ):
	allFile = getEntireFile()
	bookList = allFile.split("<book")
	retList = []
	#print bookList
	for book in bookList:
		matchPrice = re.findall( r".*<price>(.*)</price>.*", book )
		if matchPrice:
			#print matchTitle
			if bookPrice > float(matchPrice[0]):
				#print "Matched! Find the author"
				matchTitle = re.findall( r".*<title>(.*)</title>.*", book )
				retList.append( matchTitle[0] )
				#print matchAuthor[0]
	print retList
	return retList

def searchForWord( word ):
	allFile = getEntireFile()
	bookList = allFile.split("<book")
	retList = []
	descList = []
	found = 0
	#print bookList
	for book in bookList:
		descList = []
		pattern = r".*" + str(word) + ".*"
		matchTitle = re.findall( r".*<title>(.*)</title>.*", book )
		matchDesc = re.findall( r".*<description>(.*)\n(.*)", book )
		for element in matchDesc:
			for listElement in element:
				descList.append( listElement )
		if matchTitle:
			#print matchTitle
			#print descList
			if re.findall( pattern, matchTitle[0]):
				matchTitle = re.findall( r".*<title>(.*)</title>.*", book )
				retList.append( matchTitle[0] )
			if re.findall( pattern, descList[0]):
				matchTitle = re.findall( r".*<title>(.*)</title>.*", book )
				retList.append( matchTitle[0] )
			if re.findall( pattern, descList[1]):
				matchTitle = re.findall( r".*<title>(.*)</title>.*", book )
				retList.append( matchTitle[0] )
	#
	retSet = set(retList)
	retList = list(retSet)
	#print (retList)
	return retList
	
def main():
	searchForWord( "After" )
		

if __name__ == "__main__" :
    main()
