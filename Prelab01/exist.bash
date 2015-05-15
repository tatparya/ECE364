#! /bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-20 17:09:49 -0500 (Tue, 20 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Prelab01/exist.bash $
# $Revision: 73225 $
# $Id: exist.bash 73225 2015-01-20 22:09:49Z ee364h05 $
NumParams=$#
Params=$@
Counter=1
for (( ; Counter <= NumParams; Counter++ ))
do
    if [[ -r $1 ]]
    then
        printf "File %s is readable!\n" $1
    elif [[ ! -e $1 ]]
    then
        touch $1
    fi 
    shift
done
exit 0
