#!/bin/env python3

"""
change one jmp instruction to nop or one
nop instruction to jmp in order to fix the
instructions and let the program terminate
without getting into an infinite loop
"""

import sys
import re
from collections import defaultdict

def solution(filename):

	# read in input data as tuples of instructions:
	# (action, quantity)
	data = []
	with open(filename) as f:
		for x in f:
			data.append((x.strip()[:3],int(x.strip()[4:])))

	answer = 0

	# try changing each jmp to nop
	for d in range(len(data)):
		# temporarily change jmp to nop
		if data[d][0] == 'jmp':
			data[d] = ('nop',data[d][1])
			# use this updated dataset to see
			# if it will result in any loops
			acc_val, index = getValue(data)
			# if index indicates that it has 
			# reached the end of the instructions,
			# we have found the correct change
			if index >= len(data):
				answer = acc_val
				break
			# else, change nop back to jmp and continue
			else:
				data[d] = ('jmp',data[d][1])

	# try changing nops to jmps
		# not needed since above worked :)

	return answer


def getValue(data):

	curr_index = 0
	visitedIndices = []
	value = 0	# accumulated value
	
	# run through instructions
	while True:
		# if current instruction has already been
		# executed before, break
		if curr_index >= len(data) or curr_index in visitedIndices:
			break
		# add index of current instruction to visted list
		visitedIndices.append(curr_index)
		# execute current instruction
		if data[curr_index][0] == 'nop':
			curr_index += 1
			continue
		elif data[curr_index][0] == 'acc':
			value += data[curr_index][1]
			curr_index += 1
			continue
		elif data[curr_index][0] == 'jmp':
			curr_index += data[curr_index][1]

	return value, curr_index

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day8code2.py <data-file>")
		sys.exit(1)
	value = solution(sys.argv[1])
	print("The value of the accumulator will be {} after the program terminates.".format(value))
