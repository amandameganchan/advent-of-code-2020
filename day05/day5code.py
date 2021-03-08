#!/bin/env python3

"""
determine the seat ID of each boarding pass
and: 1.find the highest one, and 2. find the
only one missing (somewhere in the middle)
 
there are 0-127 rows and 0-7 columns on the plane
F indicates front half (towards 0) 
B indicates back half (towards 127)
L indicates lower half (towards 0)
R indicates upper half (towards 7)
seat ID is computed by: row*8 + col
"""

import sys

def solution(filename):

	input_data = []
	highest = 0
	all_passes = []
	
	# read in input data
	with open(filename, 'r') as f:
		for x in f:
			input_data.append(x.strip())
	# compute ID for each pass
	for p in input_data:
		row = getRow(p[:7]) # use first 7 chars of pass
		col = getCol(p[7:]) # use last 3 chars of pass
		currentID = (row*8) + col
		# update highest seat ID
		if (currentID > highest):
			highest = currentID 
		all_passes.append(currentID)

	return highest, find_missing(all_passes)

def getRow(p):
	"""
	find row number according to the rules
	iteratively halve the range until left
	with one number

	Args:
		p (string): string of Fs and Bs to indicate
		front and back half
	Returns:
		int: row number
	"""
	rows = list(range(128))
	for char in p:
		mid = int((len(rows)/2))
		if char == 'F':
			rows = rows[:mid]
		elif char == 'B':
			rows = rows[mid:]	
	return rows[0]

def getCol(p):
	"""
	find column number according to the rules
	iteratively halve the range until left
	with one number

	Args:
		p (string): string of Ls and Rs to indicate
		upper and lower half
	Returns:
		int: column number
	"""
	cols = list(range(8))
	for char in p:
		mid = int((len(cols)/2))
		if char == 'L':
			cols = cols[:mid]
		elif char == 'R':    
			cols = cols[mid:]
	return cols[0]

def find_missing(all_passes):
	"""
	loop through sorted IDs to find the
	one pass that is not equal to 1 plus
	the last one (meaning there is a 
	missing one in between)

	Args:
		all_passes (list): list of all seat IDs
	Returns:
		int: missing ID number
	"""
	all_passes.sort()
	prev = all_passes[0]
	for p in all_passes[1:]:
		if p != (prev+1):
			return p-1
		else:
			prev = p


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day5code.py <data-file>")
		sys.exit(1)
	highest, missing = solution(sys.argv[1])
	print("Highest seat ID: ", highest)
	print("My seat (missing one): ", missing)
