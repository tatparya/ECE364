#! /bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-20 17:09:49 -0500 (Tue, 20 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Prelab01/sum.bash $
# $Revision: 73225 $
# $Id: sum.bash 73225 2015-01-20 22:09:49Z ee364h05 $
#
Num_Params=$#
Param_Values=$@
SumOfParams=0
Param=$1
for (( Counter=1; Counter <= Num_Params; Counter++ ))
do
    ((SumOfParams=$SumOfParams+$1))
    shift
done
printf "%d\n" $SumOfParams
exit 0
