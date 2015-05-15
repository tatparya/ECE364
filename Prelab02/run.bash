#/bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-01-25 23:37:47 -0500 (Sun, 25 Jan 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Prelab02/run.bash $
# $Revision: 73879 $
# $Id: run.bash 73879 2015-01-26 04:37:47Z ee364h05 $
NumParams=$#
ParamVals=$@
#       Check for 0 args
if (( $NumParams < 2 ))
then
    echo "Usage: run.bash <filename> <filename>"
    exit 0
fi
#       Main Script

#       check for $1 exists
var=quick_sim
outputFile=($2)
if [[ -e $var ]]
then
    rm $var
fi
#       Compile arg1 and check for compilation success
if ! gcc $1 -o quick_sim
then
    echo "error: $1 could not be compiled!"
    exit 1
fi

#       check if output file exists
if [[ -e $2 ]]
then
    echo -n "$2 exists. Would you like to delete it? "
    read input1
    if [[ $input1 = "y" ]]
    then
        rm $2 >/dev/null
    else
        echo -n "Enter a new filename: "
        read input2
        outputFile=$input2
    fi
fi
#       Run simulation, redirect output into outputFile, calc Fastest time
fastestTime=1000000
processors=(a i)
cacheSize=1
issueWidth=1
for (( cacheSize=1; cacheSize <=32; cacheSize=cacheSize*2 ))
do
    for (( issueWidth=1; issueWidth <=16; issueWidth=issueWidth*2 ))
    do
        for processor in ${processors[*]}
        do
            var2=($(quick_sim $cacheSize $issueWidth $processor | cut -d":" -f 8,10))
            time=$(echo "$var2" | cut -d":" -f 2)
            if [[ $processor = "i" ]]
            then
                out=(Intel Core i7)
            else
                out=(AMD Opteron)
            fi
            output=$(echo "${out[*]}:$cacheSize:$issueWidth:$var2">>$outputFile)
            if (( $time <= $fastestTime ))
            then
                fastestTime=$time
                fastProcessor=$processor
                fastCache=$cacheSize
                fastWidth=$issueWidth
            fi
        done
    done
done

echo "Fastest run time achieved by ${out[*]} with cache size $fastCache and issue width $fastWidth was $fastestTime"
exit 0
