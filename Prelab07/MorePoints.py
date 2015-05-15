#! /usr/bin/env python3.4
__author__ = 'ee364h05'


import sys
import os
import math

#	class Def

class Point3D:
	#	Constructor
	def __init__(self, x=0,y=0,z=0):
		self.x = x
		self.y = y
		self.z = z
	
	#	Print
	def __str__( self ):
		string = ('({0:.2f}, {1:.2f}, {2:.2f})'.format( self.x, self.y, self.z ))
		print string
		return string
		
	#	Distance Function
	def distFrom( self, other ):
		#Compute Euclideam distance between points
		distance = math.sqrt( ( self.x - other.x ) ** 2 + ( self.y - other.y ) ** 2 + ( self.z - other.z ) ** 2 )
		return distance
		
	#	Compute and return nearest point for list of points
	def nearestPoint( self, points):
		if( points ):
			closestPoint = Point3D()
			minDist = self.distFrom( points[0] )
			closestPoint.x = points[0].x
			closestPoint.y = points[0].y
			closestPoint.z = points[0].z
			for point in points:
				dist = self.distFrom( point )
				if dist < minDist:
				
					minDist = dist
					closestPoint.x = point.x
					closestPoint.y = point.y
					closestPoint.z = point.z
					
			return closestPoint
		else:
			return None
	
	def clone( self ):
		selfClone = Point3D( self.x, self.y, self.z )
		
		return selfClone
		
	def __hash__(self):
		pointTuple = self.x, self.y, self.z
		return hash(pointTuple)
	 	
	#####	Operator Overloads		#####
	
	def __add__( self, other ):
		x = 0
		y = 0
		z = 0
		#	Add two points
		if isinstance( self, Point3D ) and isinstance( other, Point3D ):
			x = self.x + other.x
			y = self.y + other.y
			z = self.z + other.z
		#	Add a float to point
		elif isinstance( self, Point3D ) and isinstance( other, float ):
			x = self.x + other
			y = self.y + other
			z = self.z + other
			
		newPoint = Point3D( x, y, z )
		
		return newPoint
	__radd__ = __add__
	
	def __sub__( self, other ):
		x = 0
		y = 0
		z = 0
		#	Subtract point from point
		if isinstance( self, Point3D ) and isinstance( other, Point3D ):
			x = self.x - other.x
			y = self.y - other.y
			z = self.z - other.z
		#	Subtract float from point
		elif isinstance( self, Point3D ) and isinstance( other, float ):
			x = self.x - num
			y = self.y - num
			z = self.z - num
			
		newPoint = Point3D( x, y, z )
		
		return newPoint
	
	#	Negate a point	
	def __neg__( self ):
		if isinstance( self, Point3D ):
			x = -self.x
			y = -self.y
			z = -self.z
			newPoint = Point3D( x, y, z )
	
			return newPoint
	#	Divide point with a float
	def __div__( self, num ):
		if isinstance( self, Point3D ):
			x = self.x / num
			y = self.y / num
			z = self.z / num
			newPoint = Point3D( x, y, z )
		
			return newPoint
	#	Multiply point and a float
	def __mul__( self, num ):
		if isinstance( self, Point3D ) and isinstance( num, float ):
			x = self.x * num
			y = self.y * num
			z = self.z * num
			newPoint = Point3D( x, y, z )
			return newPoint
	__rmul__ = __mul__

	#	Check if two points are the same
	def __eq__( self, other ):
		if self.x == other.x and self.y == other.y and self.z == other.z:
			return True
		else:
			return False	
	#	Compute distance from origin greater than
	def __gt__( self, other ):
		origin = Point3D()
		dist1 = distFrom( self, origin )
		dist2 = distFrom( other, origin )
		if dist1 > dist2:
			return True
		else:
			return False
	#	Compute distance from origin greater than equal
	def __ge__( self, other ):
		origin = Point3D()
		dist1 = distFrom( self, origin )
		dist2 = distFrom( other, origin )
		if dist1 >= dist2:
			return True
		else:
			return False
	#	Compute distance from origin less than
	def __lt__( self, other ):
		origin = Point3D()
		dist1 = distFrom( self, origin )
		dist2 = distFrom( other, origin )
		if dist1 < dist2:
			return True
		else:
			return False		
	#	Compute distance from origin less than equal
	def __le__( self, other ):
		origin = Point3D()
		dist1 = distFrom( self, origin )
		dist2 = distFrom( other, origin )
		if dist1 <= dist2:
			return True
		else:
			return False
	
#	Class def ends here

#	class Def

class PointSet:
	#	Constructor
	def __init__(self, points = set() ):
		self.points = set(points)
		
	#	Add a point to the set
	def addPoint( self, p ):
		self.points.add( p )
		
	#	Count the number of points in the set
	def count( self ):
		num = len( self.points )
		return num
		
	#	Compute Bouding Box
	def computeBoundingBox( self ):
		minX = 0
		maxX = 0
		minY = 0
		maxY = 0
		minZ = 0
		maxZ = 0
		
		for point in self.points:
			if minX > point.x:
				minX = point.x
			elif maxX < point.x:
				maxX = point.x
			if minY > point.y:
				minY = point.y
			elif maxY < point.y:
				maxY = point.y
			if minZ > point.z:
				minZ = point.z
			elif maxZ < point.z:
				maxZ = point.z
		
		minPoint = Point3D( minX, minY, minZ )
		maxPoint = Point3D( maxX, maxY, maxZ )
		retTuple = ( minPoint, maxPoint )
		return retTuple
	#	Compute Nearest Neighbours
	def computeNearestNeighbours( self, other ):
		retList = []
		for point in self.points:
			minDist = 10000000000000
			minPoint = None
			for otherPoint in other.points:
				if minDist > point.distFrom( otherPoint ):
					minDist = point.distFrom( otherPoint )
					minPoint = otherPoint.clone()
			pointTuple = ( point, minPoint )
			retList.append( pointTuple )
		return retList
	#####	Operator Overloads		#####
	
	
	def __add__( self, point ):
		#	Add point3d to the pointset
		if isinstance( self, PointSet ) and isinstance( point, Point3D ):
			newSet = PointSet( self )
			newSet.add( point )
		
			return newSet
		#	Add pointset to pointset
		elif isinstance( self, PointSet ) and isinstance( other, PointSet ):
			newSet = PointSet( self )
			otherSet = PointSet( other )
			newSet.update( otherSet )
		
			return newSet
	
	
	def __sub__( self, point ):
		#	Sub point3d from pointset
		if isinstance( self, PointSet ) and isinstance( point, Point3D ):
			newSet = PointSet( self )
			if point in newSet:
				newSet.remove( point )
				return newSet
			else:
				return newSet
		#	Sub pointset from ponitset
		elif isinstance( self, other ) and isinstance( other, PointSet ):
			newSet = cother( self )
			otherSet = other( self )
			newSet.symmetric_different_update( otherSet )
		
			return newSet
	
	#	Greater than
	def __gt__( self, other ):
		num1 = self.count( self )
		num2 = self.count( other )
		
		if num1 > num2:
			return True
		else:
			return False
	
	#	Greater than equal
	def __ge__( self, other ):
		num1 = self.count( self )
		num2 = self.count( other )
		
		if num1 >= num2:
			return True
		else:
			return False
	
	#	Less than
	def __lt__( self, other ):
		num1 = self.count( self )
		num2 = self.count( other )
		
		if num1 < num2:
			return True
		else:
			return False
	
	#	Less than equal
	def __le__( self, other ):
		num1 = self.count( self )
		num2 = self.count( other )
		
		if num1 <= num2:
			return True
		else:
			return False
	
#	Class def ends here
def printSet( pointset ):
	print 'Printing'
	for points in pointset:
		str( points )

def main():
	#pass
	
	newPoint = Point3D( 1,2,3 )
	pt1 = Point3D( 10,1,2 )
	pt2 = Point3D( -1,-2,0 )
	pt3 = Point3D( 2,5,6 )
	pt4 = Point3D( 10, 5, -5 )
	ptList = [ pt1, pt2, pt3, pt4 ]
	pt5 = Point3D( 0,0,0 )
	pt = 2.0 * pt1
	str( pt )
	#pt6 = pt5 + pt1
	#str( pt6 )
	newSet = PointSet( ptList )
	#printSet( newSet.points )
	#print newSet.points
	newSet.addPoint( newPoint )
	#printSet( newSet.points )
	#print newSet.points
	#printSet( newSet.points )
	#num = newSet.count()
	#print num
	#boundingBox = newSet.computeBoundingBox()
	#printSet( boundingBox)
	pt7 = Point3D( 10,10,10 )
	pt8 = Point3D( 5,6,7 )
	pt9 = Point3D( 1,5,1 )
	lis = [ pt7, pt8, pt9 ]
	set2 = PointSet( lis )
	#printSet( set2.points )
	#print set2.points
	nearest = set2.computeNearestNeighbours( newSet )
	#print nearest
	#for element in nearest:
		#printSet( element )
	

if __name__ == "__main__" :
    main()

