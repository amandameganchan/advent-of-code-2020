#!/bin/env python3

"""
apply a bitmask to every value below it and
save the resulting values in the specified
memory addresses

find the sum of all values left in memory after 
applying all bitmasks
"""

import sys
import re
from collections import defaultdict

def solution(filename):

	# read in input data; store bitmasks
	# and their corresponding assignments 
	# separately
	masks = []
	assignments = []
	
	with open(filename) as f:
		assnmts = {} # temporary holder for assignments
		for x in f:
			if "mask" in x:
				# add mask
				masks.append(x.strip()[7:])
				# flush assignment block
				if assnmts: assignments.append(assnmts)
				assnmts = {}
			else:
				# split memory address and value
				temp = re.split(r"\D+",x)	
				assnmts[temp[1]] = temp[2]
		assignments.append(assnmts)

	# zip bitmasks and corresponding assignments together
	data = list(zip(masks,assignments))
	# apply the bitmasks
	memory = initializeMemory(data)

	# sum all of the final values
	memsum = 0
	for key in memory.keys():
		memsum += memory[key]

	return memsum

def initializeMemory(data):
	"""
	apply all bitmasks to their corresponding
	values; save all results in 'memory'

	Args:
		data (list): input data; bitmasks and
		their corresponding assignments

	Returns:
		dict: 'memory' (final values (after applying the bitmask) 
		at specified memory addresses)
	"""

	# define mem dictionary to store vals
	memory = {}

	# for each mask+assignments block:
	for block in data:
		# load mask as list
		mask = list(block[0])
		# iterate through assignments
		for assignment in block[1].keys():	
			# for each assignment: convert val to 36 bits (list)
			val = list('{0:036b}'.format(int(block[1][assignment])))
			# loop through list of bits: for each index that is 0 or 1 in mask, change to that
			for i in range(len(val)):
				if mask[i] != 'X':
					val[i] = mask[i]
			# convert list of bits back to integer
			# assign to mem dictionary
			memory[assignment] = int(''.join(val),2)
	
	return memory

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day14code.py <data-file>")
		sys.exit(1)
	finalsum = solution(sys.argv[1])
	print("Sum of all values left in memory after completion: {}".format(finalsum))
