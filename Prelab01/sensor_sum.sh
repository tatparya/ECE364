#! /bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-20 17:46:26 -0500 (Tue, 20 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Prelab01/sensor_sum.sh $
# $Revision: 73262 $
# $Id: sensor_sum.sh 73262 2015-01-20 22:46:26Z ee364h05 $
#
Num_Params=$#
Param_Values=$@
if (( $# == 0 ))
then
    echo "usage: sensor_sum.sh"
    exit 0
fi
if [[ ! -r $1 ]]
then
    echo "error: $1 is not a readable file!"
    exit 0
fi
while read line
do
    sum=0
    v=($line)
    ((sum = v[1] + v[2] + v[3]))
    file=$(echo "$line" | head -c2)
    echo -n "$file "
    echo "$sum"
done < "$1"
exit 0
