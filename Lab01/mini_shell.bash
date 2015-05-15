#! /bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-22 11:22:33 -0500 (Thu, 22 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Lab01/mini_shell.bash $
# $Revision: 73509 $
# $Id: mini_shell.bash 73509 2015-01-22 16:22:33Z ee364h05 $
echo -n "Enter a command : "
read userinput
while [[ $userinput != "quit" ]]
do
    if (( userinput == "compile" ))
    then
        echo -n "Enter filename: "
        read input
        if [[ -r input ]]
        then
            complie=&(gcc -Wall -Werror $input)
            if (( complie == 0 ))
            then
                echo "Compilation succeeded"
            else
                echo "Compilation failed"
            fi
        else
            echo "That file does not exist"
        fi
    elif (( userinput == "hello" ))
    then
        # Say hello user
        echo "Hello $(whoami)"
    elif (( userinput == quit ))
    then
        echo "Exitting..."
        exit 0
    else
        echo "Error: Unrecognized input"
    fi

    echo -n "Enter a command : "
    read userinput
done
echo "Exitting..."
exit 0
