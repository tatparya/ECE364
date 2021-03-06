#! /usr/bin/env python3.4
__author__ = 'ee364h05'

import sys
import os
import base64
import re
from PIL import Image

def getImageFile(imageFilePath):

    fp = open("new.png", "wb")

    im = Image.open("bridgeTest.png")
    print (im.format, im.size, im.mode)
    pixels = im.load()


    list1 = [ 7,12,1,14,2,13,8,11,16,3,10,5,9,6,15,4 ]

    img = Image.new( 'L', (4,4), "black" )
    pixelmap = img.load()
    for i in range( 3 ):
        for j in range( 3 ):
            pixelmap[i,j] = list1[ i*j + j ]

    #img.show()
    img.save( "testing.png" )

    #   Get pixels in a list
    pixelList = []

    for i in range( im.size[0] ):
        pixelRows = []
        for j in range( im.size[1] ):
            pixelRows.append( pixels[i,j] )
        pixelList.append( pixelRows )

    #for rows in pixelList:
        #print( rows )
    #im.show()
    return im

def getPixList( ):
    im = openImg()

    pixData = im.load()
    pixelList = []

    for i in range( im.size[0] ):
        pixelRows = []
        for j in range( im.size[1] ):
            pixelRows.append( pixData[i,j] )
        pixelList.append( pixelRows )

    for rows in pixelList:
        print( rows )

def makeImg():
    list1 = [ 7,12,1,14,2,13,8,11,16,3,10,5,9,6,15,4 ]

    img = Image.new( 'L', (4,4), "black" )
    pixelmap = img.load()
    for i in range( 4 ):
        for j in range( 4 ):
            pixelmap[i,j] = list1[ i*4 + j ]

    #img.show()
    img.save( "testing.png" )

def openImg():
    newIm = Image.open( "files/sunflower.png")
    data = newIm.getdata()

    for element in data:
        print( element )

    print( type(element), type(data))

    print( newIm.format, newIm.size, newIm.mode )
    return newIm

def baseEncode( ):

    #b"7,12,1,14,2,13,8,11,16,3,10,5,9,6,15,4"
    #b"7, 12, 1, 14, 2, 13, 8, 11, 16, 3, 10, 5, 9, 6, 15, 4"

    list = [ 7,12,1,14,2,13,8,11,16,3,10,5,9,6,15,4 ]
    by = bytearray( list )

    print( by )
    #message = b'\x07\x0c\x01\x0e\x02\r\x08\x0b\x10\x03\n\x05\t\x06\x0f\x04'
    message = b"Today is the beginning of a new week."
    messageNew = base64.b64encode( message )
    messageBy = base64.b64encode( by )

    #print( messageBy)
    print (messageNew)
    print( len(messageNew) )

    baseDecode()

    #for num in by:
        #print( int(num) )

def baseDecode():
    message = b'VG9kYXkgaXMgdGhlIGJlZ2lubmluZyBvZiBhIG5ldyB3ZWVrLg=='
    #message = "BwwBDgINCAsQAwoFCQYPBA=="
    messageNew = base64.b64decode( message )
    #messageNew = bytearray(base64.b64decode( message ))

    print( messageNew )

def serializeImg():
    im = openImg()

    pixData = im.load()
    pixelList = []

    for i in range( im.size[0] ):
        for j in range( im.size[1] ):
            pixelList.append( pixData[i,j] )

    print( pixelList )

    return pixelList

def getbitString(char):

    asciiChar = ord( char )
    binaryChar = str( bin( asciiChar ) )[2:]

    #   If binaryChar is not 8-bit, pad with 0's
    while len( binaryChar ) < 8:
        binaryChar = '0' + binaryChar

    return binaryChar

def getEncoded():
    pixList = serializeImg()
    binPixArr = bytearray( pixList )
    encoded = base64.b64encode( binPixArr )
    print( "Bytearray", binPixArr )
    print( "Encoded", encoded )

def testing():
    text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
    print( len( text ) )
#   Main Block
def main():
    print( getbitString('a') )

    #testing()
    #baseEncode()
    #openImg()
    #baseDecode()
    #im = getImageFile("bridge.png")
    #makeImg()
    #getPixList()
    #getEncoded()
    pass

if __name__ == "__main__":
    main()