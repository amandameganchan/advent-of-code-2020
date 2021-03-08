#!/bin/env python3

"""
simulate the change in seating arrangements
according to a set of rules until the state
stabilizes and applying the rules results in
the same arrangement as before

find the number of occupied seats in the 
final arrangement
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

	# apply the rules to get the next state;
	# continue to do this until it stabilizes
	# (new state is same as previous)
	newState = applyRules(data)
	while newState != applyRules(newState):
		newState = applyRules(newState)

	# count and return the occupied seats
	return countOccupied(newState)

def countOccupied(data):
	"""
	count the number of occupied seats, 
	indicated by a '#'

	Args:
		data (list): input data; model of
		seat layout (rows and columns of chars)

	Returns:
		int: number of occupied seats
	"""
	counter = 0

	# loop through rows and columns and
	# count the number of '#'s
	for r in range(len(data)):
		for c in range(len(data[r])):
			if data[r][c] == '#':
				counter += 1

	return counter

def applyRules(data):
	"""
	apply the rules to determine the new state
	of the waiting room

	Args:
		data (list): previous state of the waiting room

	Returns:
		list: new state of the waiting room
	"""
	newState = []	# new waiting area state

	# for every row in the waiting area
	for rowIndex in range(len(data)):
		newRow = ""	# keep track of new seat states
		# for every seat in the row
		for colIndex in range(len(data[rowIndex])):
			# get adjacent seats
			arounds = getAround(rowIndex,colIndex,data)
			# apply rules to determine new seat state
			if data[rowIndex][colIndex] == '.':
				newRow += '.'
				continue
			elif data[rowIndex][colIndex] == 'L':
				if '#' not in arounds: newRow += '#'
				else: newRow += 'L'
			elif data[rowIndex][colIndex] == '#':
				if ''.join(arounds).count('#') >= 4: newRow += 'L'
				else: newRow += '#'	
		# add row to the new waiting area
		newState.append(newRow) 

	return newState

def getAround(row,col,data):
	"""
	find the seats adjacent to the given row/col

	Args:
		row (int): row number
		col (int): column number
		data (list): seating area

	Returns:
		list: list of adjacent seats
	"""

	# collect all characters immediately adjacent to the 
	# position (row,col), including the diagonal

	around = []

	if row != 0:
		around.append(data[row-1][col])
		if col != 0:
			around.append(data[row-1][col-1])
		if col != len(data[row])-1:
			around.append(data[row-1][col+1])
	if row != len(data)-1:
		around.append(data[row+1][col])
		if col != 0:
			around.append(data[row+1][col-1])
		if col != len(data[row])-1:
			around.append(data[row+1][col+1])
	if col != 0:
		around.append(data[row][col-1])
	if col != len(data[row])-1:
		around.append(data[row][col+1])

	return around

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day11code.py <data-file>")
		sys.exit(1)
	occupied = solution(sys.argv[1])
	print("The number of occupied seats is: {}".format(occupied))
