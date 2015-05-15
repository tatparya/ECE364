#! /bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-20 17:09:49 -0500 (Tue, 20 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Prelab01/line_num.bash $
# $Revision: 73225 $
# $Id: line_num.bash 73225 2015-01-20 22:09:49Z ee364h05 $
NumParams=$#
if (( NumParams > 1 ))
then
    echo "More than one arguments entered"
    exit 0
elif (( NumParams == 0 ))
then
    echo "Usage: line_num.bash <filename>"
    exit 0
fi
#
Params=$@
if [[ ! -e $1 && ! -r $1 ]]
then
    echo "Cannot read $1"
    exit 0
fi
#
Counter=1
echo "outside"
while read line 
do
    echo "$Counter: $line"
    ((Counter++))
done < $1
echo "Done"
exit 0
