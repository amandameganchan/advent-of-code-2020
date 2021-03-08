#!/bin/env python3

""" 
following the instructions, find the value 
of the accumulator immediately before any 
instruction is executed for a second time
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

	curr_index = 0
	visitedIndices = []
	value = 0	# accumulated value

	# run through instructions
	while True:
		# if current instruction has already been
		# executed before, break
		if curr_index in visitedIndices:
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
	
	return value

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day8code.py <data-file>")
		sys.exit(1)
	value = solution(sys.argv[1])
	print("The value of the accumulator will be {} immediately before \
any instruction is executed a second time.".format(value))
