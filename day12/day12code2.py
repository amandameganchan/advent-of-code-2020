#!/bin/env python3

"""
follow the instructions to navigate the ship
to its final position

now most of the instructions refer to moving
a waypoint rather than the ship; but the ship 
is always located relative to the waypoint

find the Manhattan distance between the final 
and original ship position
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

def getRotation(direction,x,y,val):
	"""
	rotate the waypoint around the ship the
	given direction and value

	Args:
		direction (char): direction of rotation
		x (int): waypoint's east/west position
		y (int): waypoint's north/south position
		val (int): amount to rotate

	Returns:
		(int,int): waypoint's new position
	"""

	# find current direction
	curr_dir = ''
	if x < 0:
		if y < 0: curr_dir = 'S'
		else: curr_dir = 'W'
	else: 
		if y < 0: curr_dir = 'E'
		else: curr_dir = 'N'

	# find target direction
	directions = {0:'N',90:'E',180:'S',270:'W'}
	angles = {'N':0,'E':90,'S':180,'W':270}	
	c = angles[curr_dir]
	c += val if direction == 'R' else val*-1
	tar_dir = directions[c%360]

	# return reflected coordinates of waypoint
	
	if curr_dir == 'N':
		if tar_dir == 'E':
			return y,-x
		elif tar_dir == 'S':
			return -x,-y
		elif tar_dir == 'W':
			return -y,x

	elif curr_dir == 'E':
		if tar_dir == 'N':
			return -y,x
		elif tar_dir == 'S':
			return y,-x
		elif tar_dir == 'W':
			return -x,-y

	elif curr_dir == 'S':	
		if tar_dir == 'N':
			return -x,-y
		elif tar_dir == 'E':
			return -y,x
		elif tar_dir == 'W':
			return y,-x

	elif curr_dir == 'W':
		if tar_dir == 'N':
			return y,-x
		elif tar_dir == 'E':
			return -x,-y
		elif tar_dir == 'S':
			return -y,x

def computePosition(data):
	"""
	follow the instructions to navigate the ship 
	and the waypoint
	all actions now move the waypoint instead of
	the ship, except for 'F'
	return the Manhattan distance between the final
	and the initial ship position

	Args:
		data (list): instructions in the form of
		a string containing a letter for the 
		action/direction, and a number for the value
		to advance

	Returns:
		int: Manhattan distance between current and
		initial positions of the ship
	"""
	EW_pos = 0
	NS_pos = 0
	WP_EW = 10
	WP_NS = 1

	# for each instruction
	for i in range(len(data)):

		action = data[i][0]
		val = int(data[i][1:])

		if action == 'R' or action == 'L':	# rotate the waypoint
			WP_EW,WP_NS = getRotation(action,WP_EW,WP_NS,val)

		elif action == 'F':	# move the ship forward towards the waypoint
			moveLat = val*(WP_EW)
			moveLon = val*(WP_NS)
			EW_pos += moveLat
			NS_pos += moveLon

		elif action == 'N':	# move waypoint north
			WP_NS += val

		elif action == 'S':	# move waypoint south
			WP_NS -= val

		elif action == 'E':	# move waypoint east
			WP_EW += val

		elif action == 'W':	# move waypoint west
			WP_EW -= val

	return abs(EW_pos)+abs(NS_pos)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day12code2.py <data-file>")
		sys.exit(1)
	distance = solution(sys.argv[1])
	print("Manhattan distance between current location and ship's starting position: {}".format(distance))

