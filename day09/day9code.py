#!/bin/env python3

"""
find the first number in the list that is not 
the sum of two of the previous 25 numbers (not 
including the first 25 numbers)

find a sequence of numbers in the list that sum
to the number found in part 1; return the sum
of the smallest and largest number in this sequence
"""

import sys
import re
from collections import defaultdict

def solution(filename):

	# read in input data
	data = []
	with open(filename) as f:
		for x in f:
			data.append(x.strip())

	# loop through numbers starting with the
	# one at index 25 and check its validity
	# (sum of two of the previous 25 #s)
	invalid = -1
	for i in range(25,len(data)):
		if not checkValid(i,data):
			invalid = data[i]
			break

	# find sequence of numbers that sum to the
	# invalid one; take the sum of the smallest
	# and largest ones in the range
	found = findSequence(invalid,data)
	answer = (min(found) + max(found))

	return invalid, answer

def findSequence(num,data):
	"""
	for each number in the list, create a sequence
	starting at that number and keep adding subsequent
	numbers until the target number is reached or gone 
	over; if reached, return sequence; if overshot, 
	start again at next number in list

	Args:
		num (int): target number
		data (list): input data, list of all numbers

	Returns:
		list: sequence of numbers that sum to target #
	"""
	sequence = []

	# loop over all numbers in the list to start the sequence
	for i in range(len(data)):
		# sequence of only the target number does not count
		if int(data[i]) == int(num):
			continue
		# create a sequence starting at data[i] and keep adding
		# numbers until sum of sequence is greater than or equal
		# to the target num
		counter = i
		while sum(sequence) < int(num):
			sequence.append(int(data[counter]))
			counter += 1
		# if sum of sequence is equal to target num, found solution
		if sum(sequence) == int(num):
			break
		# else, clear sequence for next test
		else:
			sequence = []

	return sequence

def checkValid(numIndex,data):
	"""
	checks validity by iterating over all pairs
	within the previous 25 numbers and comparing
	their sum to the current value; if equal, 
	number is valid; if no pair equals the current
	value, number is invalid

	Args:
		numIndex (int): current index
		data (list): input data, list of all numbers

	Returns:
		bool: validity of current number
	"""

	valid = False
	pool = data[numIndex-25:numIndex]	# previous 25 integers in list

	# loop through all pair combinations within the previous
	# 25 numbers to check if the current number is valid
	for i in range(25):
		for j in range(25):
			if i != j and (int(pool[i]) + int(pool[j]) == int(data[numIndex])):
				valid = True

	return valid	

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day9code.py <data-file>")
		sys.exit(1)
	invalid, answer = solution(sys.argv[1])
	print("The first invalid number is: {}".format(invalid))
	print("The sum of least and greatest #s in the sequence is: {}".format(answer))
