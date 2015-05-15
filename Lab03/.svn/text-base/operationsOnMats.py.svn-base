#! /usr/bin/env python3.4
__author__ = 'ee364h05'

import sys
import os

def checkIfMatrixIsValid( matrix ):
    #   CHeck for list of list
    if type( matrix[0]) != list :
        return False
    numCols = 0
    numRows = 0
    lenLastRow = 0
    lengthList = len( matrix )
    i = 0
    valid = 1
    while i < lengthList - 1 :
        lenRow = len( matrix[i])
        lenNextRow = len( matrix[i+1] )
        if lenRow != lenNextRow :
            valid = 0
        i += 1
    if valid :
        #print("Valid")
        return True
    else :
        #print("Not valid")
        return False

def getMatrixSize( matrix ):
    isValid = checkIfMatrixIsValid( matrix )
    falseList = []
    if not isValid :
        #print falseList
        return falseList
    numRows = len( matrix )
    numCols = len( matrix[0] )
    trueList = [ numRows, numCols ]
    #print trueList
    return trueList

def getRow( matrix, rowIndex ):
    isValid = checkIfMatrixIsValid( matrix )
    falseList = []
    if not isValid :
        return falseList
    else :
        matSize = getMatrixSize( matrix )
        #print matSize
    if rowIndex <= ( matSize[0] - 1 ):
        #print ("Printing")
        #print matrix[rowIndex]
        return matrix[rowIndex]
    else :
        print("Too big")
        return falseList

def getColumn( matrix, columnIndex ):
    isValid = checkIfMatrixIsValid( matrix )
    falseList = []
    if not isValid :
        #print falseList
        return falseList
    else :
        matSize = getMatrixSize( matrix )
        #print matSize
    if columnIndex <= ( matSize[1] - 1 ):
        #print ("Printing")
        numCols = matSize[0]
        i = 0
        retList = []
        for row in matrix:
            retList.append(row[columnIndex])
        #print retList
        return retList
    else :
        print("Too big")
        return falseList

def transposeMatrix( matrix ):
    isValid = checkIfMatrixIsValid( matrix )
    falseList = []
    if not isValid :
        #print "Not Valid"
        return None
    transMatrix = []
    newRow = []
    i = 0
    matSize = getMatrixSize(matrix)
    while i <= ( matSize[1] - 1 ) :
        for row in matrix:
            newRow.append(row[i])
        transMatrix.append(newRow)
        newRow = []
        i += 1

    #print transMatrix
    return transMatrix

def dotProduct( row, column ):
    lenRow = len(row)
    lenCol = len(column)
    if not ( lenRow == lenCol and ( lenCol > 0 ) and ( lenRow > 0 ) ):
        return None
    product = 0
    i = 0
    while i <= ( lenRow - 1 ):
        product += row[i]*column[i]
        i += 1
    #print product
    return product

def multiplyMatrices( matrix1, matrix2 ):
    isValid1 = checkIfMatrixIsValid( matrix1 )
    isValid2 = checkIfMatrixIsValid( matrix2 )
    if not ( isValid1 and isValid2 ):
        #print "Either of the two matrices are not valid"
        return None
    mat1Size = getMatrixSize( matrix1 )
    mat2Size = getMatrixSize( matrix2 )
    if mat1Size[1] != mat2Size[0]:
        #print mat1Size[1]
        #print mat2Size[0]
        #print "Sizes incompatible"
        return None
    finalMatrix = [[0] * mat2Size[1] for i in range ( mat1Size[0] ) ]
    #print finalMatrix
    #   Multiplying
    r = mat1Size[0]
    #print r

    c = mat2Size[1]
    #print c
    i = 0
    j = 0
    while i <= r-1:
        j=0
        while j <= c - 1:
            row = getRow( matrix1, i )
            col = getColumn( matrix2, j )
            finalMatrix[i][j] += dotProduct(row, col)
            #print dotProduct( row,col)
            j += 1
            #print finalMatrix
        i += 1
    #print finalMatrix
    return finalMatrix

def main():
    mat1 = [[3,2,1],[4,5],[3,1,0]]
    mat2 = [[9,1],[1,3],[3,1]]
    mat3 = [[9,8,5,2]]
    mat4 = [1,6,1,2,3]

    mat5 = [[7,8,-2],[4,2,5]]
    mat6 = [[9,0],[3,7],[-2,10]]
    mat7 = [[9,10],[6,3],[10,4]]
    mat8 = [[7,0,4],[5,4,1]]
    mat9 = [[3,2,8]]
    mat10 = [[0,-1,-1],[4,-3,8],[-3,-3,2]]
    row = [6,2,9,0]
    col = [1,3,2,1]

    #multiplyMatrices( mat5, mat6 )

if __name__ == "__main__" :
    main()

