#! /bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-22 01:54:36 -0500 (Thu, 22 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Prelab01/svncheck.bash $
# $Revision: 73452 $
# $Id: svncheck.bash 73452 2015-01-22 06:54:36Z ee364h05 $
#
input="file_list"
while read line
do
    echo "Reading $line"
    svnStat=$(svn status $line)
    if [[ $svnStat == ?* ]]
    then
        if [[ -e $line ]]
        then
            if [[ ! -x $line ]]
            then
                echo "Do you want to make the file \"line\" executable? (y/n)"
                read input
                if (( input == "y" ))
                then
                    chmod +x $line
                fi
            fi
            svn add $line
        else
            echo "Error: File $line appears to not exist here or in svn"
        fi
    elif [[ $svnStat != ?* ]]
    then    
        if [[ ! -x $line ]]
        then
            svn propset svn:executale ON $line
        fi
    fi
done < "$input"
svn commit -m "Auto commiting code"

exit 0
