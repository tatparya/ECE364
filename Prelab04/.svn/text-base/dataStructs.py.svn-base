#! /usr/bin/env python3.4
__author__ = 'ee364h05'


import sys
import os
import string
import glob
import filecmp

def importFilenames():

    filenames = glob.glob('files/*')
    return filenames

def getWordFrequency():
    #Import filenames
    filenames = importFilenames()

    wordDict = {}
    for name in filenames:
        with open(name,'r') as inputFile:
            for line in inputFile:
                for word in line.split():
                    #Accounting for punctuations
                    ch = word[len(word) - 1]
                    if ch < 'A' or ( ch > 'Z' and ch < 'a' ) or ch > 'z':
                        newWord = word[0:-1]
                    else:
                        newWord = word

                    if word in wordDict:
                        wordDict[newWord] += 1
                    else:
                        wordDict[newWord] = 1
    #print wordDict
    return wordDict

def findCount( groupKey ):
    count = 0
    with open(groupKey, 'r') as inputFile:
        for line in inputFile:
            for word in line.split():
                count += 1
    return count

def checkDup( name, filenames ):
    group = [name[6:9]]
    for filename in filenames:
        if name != filename:
            if filecmp.cmp(name, filename):
                group.append(filename[6:9])

    list.sort(group)
    return group

def getDuplicates():
    #Import filenames
    filenames = glob.glob('files/*.txt')

    groupDict = {}
    readNames = []

    for name in filenames:
        if name not in readNames:
            group = checkDup( name, filenames )
            readNames.append(group)
            length = len(group)

            if length > 1:
                groupKey = group[0]
                groupKeyPath = "files/%s.txt"%(groupKey)
                wordCount = findCount( groupKeyPath )
                groupTuple = ( wordCount, group )
                groupDict[groupKey] = groupTuple

    #print groupDict

    return groupDict

# ===========PART 2===========\

def importFilenames2():

    filenames = glob.glob('purchases/purchase_*')
    return filenames

def getPurchaseReport():
    filenames = importFilenames2()
    items = []
    with open('purchases/Item List.txt', 'r') as itemList:
        for line in itemList:
            items.append(line)

    sumDict = {}
    for file in filenames:
        sum = 0
        with open( file, 'r' ) as inputFile:
            allLines = inputFile.readlines()
            transactionLines = allLines[2:]
            for line in transactionLines:
                parts = line.split()
                sum += float(parts[1])
        #print file
        sumDict[file[19:22]] = float(sum)
    #print sumDict
    return sumDict

def makedic(filename):
    dicto = {}
    with open(filename,"r") as readfile:
        for line in readfile:
            splitline = line.split()
            if(len(splitline)) == 2:
                product = splitline[0]
                price = splitline[1]

                dicto[product] = price
    return dicto

def getTotalSold():
    dictionary = {}
    files = glob.glob('./purchases/*')
    files.remove('./purchases/Item List.txt')
    pricedict = makedic('./purchases/Item List.txt')
    keys = pricedict.keys()
    for each in keys:
        if each != "Name":
            sum2 = 0
            for name in files:
                purdict = makedic(name)

                if each in purdict:
                    sum2 += float(purdict[each])

                dictionary[each] = sum2
    #print dictionary
    return dictionary

def main():

    #getWordFrequency()
    #getDuplicates()
    getPurchaseReport()

if __name__ == "__main__" :
    main()

