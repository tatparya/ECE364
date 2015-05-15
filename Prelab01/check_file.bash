#! /bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-20 17:09:49 -0500 (Tue, 20 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Prelab01/check_file.bash $
# $Revision: 73225 $
# $Id: check_file.bash 73225 2015-01-20 22:09:49Z ee364h05 $
NumParams=$#
if (( NumParams == 0 ))
then
    echo "Usage: ./check_file.bash <filename>"
    exit 0
fi
#
Params=$@
if [[ -e $1 ]]
then
    echo "$1 exists"
else
    echo "$1 does not exist"
fi
if [[ -d $1 ]]
then
    echo "$1 is a directory"
else
    echo "$1 is not a directory"
fi
if [[ -f $1 ]]
then
    echo "$1 is an ordinary file"
else
    echo "$1 is not an ordinary file"
fi
if [[ -r $1 ]]
then
    echo "$1 is readable"
else
    echo "$1 is not readable"
fi
if [[ -w $1 ]]
then
    echo "$1 is writable"
else
    echo "$1 is not writable"
fi
if [[ -x $1 ]]
then
    echo "$1 is executable"
else
    echo "$1 is not executable"
fi
exit 0
