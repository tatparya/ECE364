#! /bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-24 16:51:30 -0500 (Sat, 24 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Prelab02/yards.bash $
# $Revision: 73756 $
# $Id: yards.bash 73756 2015-01-24 21:51:30Z ee364h05 $
NumParams=$#
ParamVals=$@

if (( NumParams < 1 ))
then
    echo "Usage: yards.bash <filename>"
    exit 0
fi
if [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 0
fi
# read file
largestAvg=0
while read line
do
    v=($line)
    size=(${#v[*]})
    #calc avg
    sum=0
    for element in ${v[*]}
    do 
        if (( ${v[0]} == $element ))
        then
            continue
        fi
        ((sum=$sum + $element))
    done
    ((avg=$sum / ($size-1)))
    if [[ $avg > $largestAvg ]]
    then
        largestAvg=$avg
    fi
    #cals variance
    y=0
    for element in ${v[*]}
    do
        if (( ${v[0]} == $element ))
        then
            continue
        fi
        ((x=($element-$avg)*($element-$avg)))
        ((y=$y+$x))
    done
    ((var=$y / ($size-1)))
    echo "${v[0]} schools averaged $avg yards receiving with a variance $var"
done < "$1"
echo "The largest average yardage was $largestAvg"

exit 0
