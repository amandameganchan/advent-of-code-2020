#!/bin/env python3

"""
follow the instructions to navigate the ship
to its final position

find the Manhattan distance between the final 
position and the original position
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

	return computePosition(data)

def computePosition(data):
	"""
	follow the instructions to navigate the ship 
	to its final position
	return the Manhattan distance between this
	and the initial position

	Args:
		data (list): instructions in the form of
		a string containing a letter for the 
		action/direction, and a number for the value
		to advance

	Returns:
		int: Manhattan distance between current and
		initial positions of the ship
	"""
	directions = {0:'N',90:'E',180:'S',270:'W'}
	angles = {'N':0,'E':90,'S':180,'W':270}
	EW_pos = 0
	NS_pos = 0
	curr_dir = 'E'

	# for each instruction
	for i in range(len(data)):

		action = data[i][0]
		val = int(data[i][1:])

		if action == 'R':	# turn right
			c = angles[curr_dir]
			c += val
			curr_dir = directions[c%360]
			continue

		if action == 'L':	# turn left
			c = angles[curr_dir]
			c -= val
			curr_dir = directions[c%360]
			continue

		if action == 'F':	# move forward
			action = curr_dir

		if action == 'N':	# move north
			NS_pos += val

		elif action == 'S':	# move south
			NS_pos -= val

		elif action == 'E':	# move east
			EW_pos += val
			
		elif action == 'W':	# move west
			EW_pos -= val

	return abs(EW_pos)+abs(NS_pos)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day12code.py <data-file>")
		sys.exit(1)
	distance = solution(sys.argv[1])
	print("Manhattan distance between current location and ship's starting position: {}".format(distance))
