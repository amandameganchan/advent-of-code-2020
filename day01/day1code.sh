#!/bin/bash

# find two numbers that sum to 2020
# and multiply them together
if [ $# != 1 ]; then
  echo "Usage: ./day1code.sh <data-file>"
  exit 1;
fi

file=$1

# find each number's complement, and if that
# number is in the file, found the two entries
while read d; do
	num=$((10#2020 - 10#$d))
	if grep -wq "^$num$" $file
	then
		echo Numbers: $d, $num
		echo Product: $((10#$d * 10#$num))
		break
	fi
done < $file 
