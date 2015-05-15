#! /usr/bin/env python3.4
__author__ = 'ee364h05'


import sys
import os
import math

#	class Def

class Experiment:
	#	Constructor
	def __init__( self, experimentNo, experimentDate, virusName, unitCount, unitCost ):
		self.experimentNumber = experimentNo
		self.experimentDate = experimentDate
		self.virusName = virusName
		self.unitCount = unitCount
		self.unitCost = unitCost
		self.totalCost = unitCount * unitCost
	
	#	Print funciton
	def __str__( self ):
		string = ('{0:03d}, {1}, ${2:06.2f}: {3}'.format( self.experimentNumber, self.experimentDate, self.totalCost, self.virusName ) )
		
		return string
	
#	Class def ends here

#	class Def

class Technician:
	#	Constructor
	def __init__( self, techName, techID ):
		self.techName = techName
		self.techID = techID
		self.experiments = {}
		
	#	Add experiment
	def addExperiment( self, experiment ):
		#	Update if exists
		if experiment.experimentNumber in self.experiments:
			self.experiments[ experiment.experimentNumber ] = experiment
		#	Create new entry	
		else:
			self.experiments[ experiment.experimentNumber ] = experiment
		
	#	Get number of experiments
	def getNumExp( self ):
		keyList = self.experiments.keys()
		num = len( keyList )
		
		return num
		
	#	Print funciton
	def __str__( self ):
		string = ('{0}, {1}: {2:02d} Experiments'.format( self.techID, self.techName, self.getNumExp() ) )
		return string
		
	#	Return multiline String of experiment details
	#	Sort using IDS
	def generateTechActivity( self ):
		firstLine = ('{0}, {1}\n'.format( self.techID, self.techName ) )
		retString = firstLine
		#	Get keys
		keyList = self.experiments.keys()
		#	Sort keys
		keyList.sort()
		#	Iterate over keys and create retString
		for key in keyList:
			#	Get experiment details
			otherLine = ('{0}\n'.format( str( self.experiments[ key ] ) ) )
			#	Add to retString
			retString += otherLine
		
		return retString
		
	#	Load exp from file
	def loadExperimentsFromFile( self, fileName ):
		#	Get line from file
		with open( fileName, 'r' ) as inputFile:
			allLines = inputFile.readlines()
			for line in allLines[ 2 : ]:
				#	Extract Information
				data = line.split()
				no = int(data[0])
				date = data[1]
				virusName = data[2]
				unitCount = int(data[3])
				unitCost = float(data[4][1:])
				#	Create experiment instance
				experiment = Experiment( no, date, virusName, unitCount, unitCost ) 
				#	Push to dictionary
				self.addExperiment( experiment )
		
#	Class def ends here

#	class Def

class Laboratory:
	#	Constructor
	def __init__( self, labName ):
		self.labName = labName
		self.technicians = {}
	
	#	Add experiment
	def addTechnician( self, technician ):
		#	Update if exists
		if technician.techName in self.technicians:
			self.technicians[ technician.techName ] = technician
		#	Create new entry	
		else:
			self.technicians[ technician.techName ] = technician
		
	#	Get number of technicians	
	def numTechnicians( self ):
		keyList = self.technicians.keys()
		num = len( keyList )
		
		return num
		
	#	Print funciton
	def __str__( self ):
		firstLine = ('{0}: {1:02d} Technicians\n'.format( self.labName, self.numTechnicians() ) )
		retString = firstLine
		#	Get keys
		keyList = self.technicians.keys()
		#	Sort keys
		keyList.sort()
		stringList = []
		#	Iterate over keys and create retString
		for key in keyList:
			#	Get experiment details
			otherLine = ('{0}\n'.format( str( self.technicians[ key ] ) ) )
			#	Add to retString
			stringList.append( otherLine )
			
		stringList.sort()
		for aString in stringList:
			retString += aString
		string = retString[:-1]
		
		return string
	
	#	Get string containing experiments from all techniciancs
	def generateLabActivity( self ):
		#	Get keys
		keyList = self.technicians.keys()
		keyList.sort()
		retString = ''
		#	Sort keys
		for key in keyList:
			#	Get tech activity
			activity = self.technicians[ key ].generateTechActivity()
			#	Concatnate
			retString += activity + '\n'
			
		string = retString[:-1]
		
		return string
		
		
#	Class def ends here

def main():
	pass
	

if __name__ == "__main__" :
    main()

