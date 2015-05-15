#/bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-25 16:29:33 -0500 (Sun, 25 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Prelab02/process_temps.bash $
# $Revision: 73822 $
# $Id: process_temps.bash 73822 2015-01-25 21:29:33Z ee364h05 $
NumParams=$#
ParamVals=$@
#       Check for args
if (( $NumParams < 1 ))
then
    echo "Usage: process_temps.bash <input file>"
    exit 1
fi
if [[ ! -r $1 ]]
then
    echo "Error: $2 is not a readable file."
    exit 2
fi
#       Main Script
exec 5< $1
read -a header<&5    #       Gets header
((numServers=${#header[*]}-1))
while read -a line
do
    #    Average temps and print
    sum=0
    for temp in ${line[*]} 
    do
        if [[ $temp = ${line[0]} ]]
        then
            continue
        fi
        ((sum=$sum + $temp))
    done
    ((avg=$sum / $numServers))
    echo "Average temperature for time ${line[0]} was $avg C."
done <&5




exit 0
