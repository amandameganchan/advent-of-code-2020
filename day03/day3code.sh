#!/bin/bash

# counts the number of trees encountered by traversing
# the given steps right and downwards
if [ $# != 3 ]; then
  echo "Usage: ./day3code.sh <data-file> <right-#> <down-#>"
  exit 1;
fi 

file=$1
right=$2
down=$3

# set up an array for the forest
getArray() {
    array=() # Create array
    while IFS= read -r line # Read a line
    do
	array+=($(printf $line%.0s {1..100})) # Append line to the array
    done < "$1"
}
getArray "$file"

tree_count=0
right_position=0
down_position=0

# traverse the forest
for l in "${array[@]}"
do
	line=$(echo $l)
	# if on a down step, get char at right step
	if ! (( $down_position % $down )); then
		char=${line:$right_position:1}
		# if char is a '#' then it's a tree
		if [[ "$char" == "#" ]]; then
			tree_count=$(($tree_count+1))
		fi
		right_position=$(($right_position+$right)) 
	fi
	down_position=$(($down_position+1))
done

echo Tree count: $tree_count
