#!/bin/bash

# checks each password for the correct 
# frequency of the given letter
if [ $# != 1 ]; then
  echo "Usage: ./day2code.sh <data-file>"
  exit 1;
fi 

file=$1
counter=0

while read line; do
	# get min and max occurrences, and specified character
	min=$(echo $line | grep -o '^\d*')
	max=$(echo $line | grep -o '\-\d* ' | grep -oE '\d+')
	char=$(echo $line | grep -oE ' .:' | grep -o '\w')
	# get number of occurrences of character in password
	num_chars=$(echo $line | grep -oE '\w*$' | tr -cd $char | wc -m)
	# check if occurrences is within the range
	# if so, increment counter
	if (($num_chars >= $min && $num_chars <= $max)); then
		counter=$(($counter+1))
	fi	
done < $file

echo Valid passwords: $counter
