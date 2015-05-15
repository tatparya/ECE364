#/bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-29 11:18:32 -0500 (Thu, 29 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Lab02/analysis.bash $
# $Revision: 74583 $
# $Id: analysis.bash 74583 2015-01-29 16:18:32Z ee364h05 $
NumParams=$#
ParamVals=$@
#       Check for 0 args
if (( $NumParams != 1 ))
then
    echo "Usage: analysis.bash <input file>"
    exit 1
fi
if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file"
    exit 2
fi

#       Main Script
bestAvgPPW=0
while read -a line
do
    processor=${line[0]}
    numArrElements=${#line[*]}
    ((numBen=$numArrElements - 3))
    sum=0
    for(( i=0; i<=$numBen-1; i++ ))
    do
        ((sum=$sum + ${line[i+2]}))
    done
    ((avg=$sum / $numBen))
    ((avgPPW=$avg / ${line[numArrElements-1]}))
    ((avg90per=$avg*90/100))
    if [[ $avgPPW > $bestAvgPPW ]]
    then
        bestAvgPPW=$avgPPW
        bestProcessor=$processor
        bestSpeed=${line[1]}
    fi
    for(( i=0; i<=$numBen-1; i++ ))
    do
        if [[ $avg90per > ${line[i+2]} ]]
        then
            echo "Run $((i+1)) for $processor ${line[1]} with score ${line[i+2]} was 90% less than average"
        fi
    done
    echo "$processor ${line[1]} scored an average of $avg" 
done < "$1"
echo "The best performance per watt was achieved by $bestProcessor $bestSpeed at $bestAvgPPW"
#       check for $1 exists
exit 0
