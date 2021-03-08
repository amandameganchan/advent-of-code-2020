#!/bin/bash

# checks each password for the given letter
# at either (only 1) of the specified positions
if [ $# != 1 ]; then
  echo "Usage: ./day2code2.sh <data-file>"
  exit 1;
fi

file=$1
counter=0

while read line; do
	# get first/second positions and specified character
	pos1=$(($(echo $line | grep -o '^\d*')-1))
	pos2=$(($(echo $line | grep -o '\-\d* ' | grep -oE '\d+')-1))
	char=$(echo $line | grep -oE ' .:' | grep -o '\w')
	# get password and the characters at the specified positions
	password=$(echo $line | grep -oE '\w*$')
	charAtPos1=${password:$pos1:1}
	charAtPos2=${password:$pos2:1}
	# check exactly one of the positions contains the character
	# if so, increment counter
	if [[ ( "$charAtPos1" == "$char" && "$charAtPos2" != "$char" ) \
|| ( "$charAtPos1" != "$char" && "$charAtPos2" == "$char" ) ]]; then
		counter=$(($counter+1))
	fi	
done < $file

echo Valid passwords: $counter
