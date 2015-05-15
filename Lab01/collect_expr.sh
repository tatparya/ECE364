#! /bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-22 11:24:49 -0500 (Thu, 22 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Lab01/collect_expr.sh $
# $Revision: 73513 $
# $Id: collect_expr.sh 73513 2015-01-22 16:24:49Z ee364h05 $
NumParams=$#
ParamValues=$@
if (( NumParams < 2 ))
then
    echo "usage: collect_expr.bash <output file> <input file> [input file 2] ... [input file N]"
    exit 1
fi
if [[ -e $1 ]]
then
    echo "error: output file $1 already exists!"
    exit 2
fi
while [[ $2 ]]
do
    if [[ ! -r $2 ]]
    then
        echo "error: $2 is not readable!"
        exit 2
    fi
    sum=0
    average=0
    while read line
    do
        v=($line)
        ((sum=v[1] + v[2] + v[3] + v[4] + v[5]))
        ((average=$sum / 5))
        echo "$line $sum $average"
        readthefile=1
    done < "$2"
    shift
    exit 0
done

exit 0
