#! /usr/bin/env python3.4
__author__ = 'ee364h05'

import sys
import os
import re
import string

def is_valid_name( identifier ):
    #   Check if a given name is valid or not
    #   String to check : identifier
    pattern = r"(\d*\w*_*)"

    match = re.findall( pattern, identifier )
    #   Gives len 2 list if vaild
    #if match:
        #print (match)

    if len( match ) > 2:
        valid = False
    else:
        valid = True

    #print( valid )

    return valid

def parse_pin_assignment( assignment ):
    #   Check if the passed argument is a valid verilog assignment
    #   Syntax for assignment: .portname(pin name)
    pattern = r"\.(.*)\((.*)\)"
    assignmentValid = False
    match = re.findall( pattern, assignment )

    if match:
        portName = match[0][0]
        #   Check if portname is valid
        portNameValid = is_valid_name( portName )
        pinName = match[0][1]
        pinNameValid = is_valid_name( pinName )

        if portNameValid and pinNameValid:
            assignmentValid = True
            retTuple = ( portName, pinName )
            return retTuple

    #print (assignment)
    #print (match)

    if not assignmentValid:
        raise ValueError( assignment )

def parse_net( line ):
    isValid = False
    invalid = False

    pattern1 = r"(\d*\w*_*)\s*(\d*\w*_*)\s*\((.*)\)"

    match = re.findall( pattern1, line )

    #print( match )
    if match:
        #   Parse line
        component = match[0][0]
        instance = match[0][1]
        assignments = match[0][2].split(',')
        assignmentList = []

        if not len( component ) == 0 and not len( instance ) == 0:
            #   Check component
            componentValid = is_valid_name( component )

            #   Check instance
            instanceValid = is_valid_name( instance )

            #   Check assignments
            for assignment in assignments:
                assignment = assignment.strip()
                assignmentValid = parse_pin_assignment( assignment )
                if not assignmentValid:
                    invalid = True
                else:
                    assignmentList.append(assignmentValid)

            if componentValid and instanceValid and not invalid:
                retTuple = ( component, instance, tuple( assignmentList ) )
                print (retTuple)
                return retTuple
        else:
            raise ValueError( line )
            return ()

        #print( component )
        #print( instance )
        #print( assignments )
    else:
        return ()

    pass

#   Main
def main():
    parse_net("OAI22X1     U11(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))")
    pass

#   Main
if __name__ == "__main__" :
    main()