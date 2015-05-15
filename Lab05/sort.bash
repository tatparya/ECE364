#/bin/bash
#
# $Author: ee364h05 $
# $Date: 2015-02-19 11:21:44 -0500 (Thu, 19 Feb 2015) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h05/Lab05/sort.bash $
# $Revision: 76114 $
# $Id: sort.bash 76114 2015-02-19 16:21:44Z ee364h05 $
NumParams=$#
ParamVals=$@

#	Check for args using getopts
while getopts f:-: thisopt
do
	case $thisopt in
		f)filename=$(echo $OPTARG);;
		-)val=$(echo $OPTARG | cut -d'=' -f2);;
		*)echo "Unknown Option.";;
		esac
		#	F case gives first arg that is the FILENAME
		#	- case gives the RANDOM NUMBER > 1	
done

#	MAIN Script

#	Check if sufficient details were passed to the script
if (( $# < 3 ))
then
	echo "Insufficient information."
	exit 1
fi

#	Check if column exists in file
if (( $val > 4 ))
then
	echo "Column number $val does not exist."
fi

#	Check if file to be read exists
if [[ ! -r $filename ]]
then
    echo "Error: File does not exist."
    exit 1
fi

#	Read and sort file

sortCol=$(($val+1))

sort -k$sortCol,$sortCol -n $filename >> $filename.sorted
echo File sorted.

exit 0
