#!/bin/bash

# find three numbers that sum to 2020
# and multiply them together
if [ $# != 1 ]; then
  echo "Usage: ./day1code2.sh <data-file>"
  exit 1;
fi

file=$1

# loop twice, add first two numbers together
# and find their sum's complement
# if the complement is in the file, solved
while read d; do 
	while read e; do
		sum=$((10#$d + 10#$e))
		num=$((10#2020 - 10#$sum))
		if grep -wq "^$num$" $file
		then
			echo Numbers: $d, $e, $num
			echo Product: $((10#$d * 10#$e * 10#$num))
			exit 0
		fi
	done < $file
done < $file 
