#! /usr/bin/env python3.4
__author__ = 'ee364h05'


import sys
import os
import string
import glob
import filecmp

def importFilenames():
	#	Import all files in reports folder
    filenames = glob.glob('reports/*')
    return filenames

def generateReportForAllUsers():
	files = importFilenames()
	userDict = {}
	#iterate through all files in reports
	for names in files:
		units = 0
		totalSpending = 0
		empTuple = ()
		with open(names, 'r') as inputFile:
			#	get id , name
			allLines = inputFile.readlines()
			id = allLines[0].split()[2]
			#	get name
			with open('users.txt', 'r') as inputName:
				allLines2 = inputName.readlines()
				for lines in allLines2[2:]:
					line = lines.split()
					if id == line[3]:
						name = line[1] + " " + line[0][:-1]	
			for line in allLines[4:]:
				parts = line.split()
				units += int(parts[2])
				totalSpending += float(parts[3][1:])
			#	check if user exists
			if name not in userDict:
				empTuple = ( units, totalSpending )
				userDict[name] = empTuple
			else:
				oldTuple = userDict[name]
				units += oldTuple[0]
				totalSpending += oldTuple[1]
				empTuple = ( units, totalSpending )
				userDict[name] = empTuple
	return userDict

def generateReportForAllViruses():
	files = importFilenames()	
	virusDict = {}
	#iterate through all files in reports
	for names in files:
		units = 0
		totalSpending = 0
		vTuple = ()		
		with open(names, 'r') as inputFile:
			allLines = inputFile.readlines()	
			for line in allLines[4:]:
				parts = line.split()
				#	get name
				name = parts[1]
				#	check if virus in dict
				if name not in virusDict:
					vTuple = (int(parts[2]), float(parts[3][1:]))
					virusDict[name] = vTuple
				else:
					totalSpending = float(parts[3][1:]) + virusDict[name][1]
					units = int(parts[2]) + virusDict[name][0]
					vTuple = (totalSpending, units)
					virusDict[name] = vTuple
	
	return virusDict
	
def getUserWithoutReports():
	
	empList = []
	#	check in users.txt and in the userDict
	with open('users.txt', 'r') as inputFile:
		allLines = inputFile.readlines()
		userDict = generateReportForAllUsers()
		for lines in allLines[2:]:
			line = lines.split()
			name = line[1] + " " + line[0][:-1]
			#	check if user in dict
			if name not in userDict:
				empList.append(name)
	empSet = set(empList)
	return empSet
	
def getTotalSpending():
	files = importFilenames()
	sum = 0
	#iterate through all files in reports
	for names in files:
		totalSpending = 0
		with open(names, 'r') as inputFile:
			allLines = inputFile.readlines()
			#	add all spendings
			for line in allLines[4:]:
				sum += float(line.split()[3][1:])
	return sum
	
def main():

    getUserWithoutReports()
    getTotalSpending()

if __name__ == "__main__" :
    main()

