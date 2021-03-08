#!/bin/env python3

import sys
import re
import math
from collections import defaultdict

def solution(filename):
	data = {}
	with open(filename) as f:
		tile = []
		tile_num = -1
		for x in f:
			if re.search('Tile',x): 
				if tile_num == -1:
					tile_num = re.findall(r'\d+',x)[0]
					continue
				else:
					data[int(tile_num)] = tile
					tile = []
					tile_num = re.findall(r'\d+',x)[0]
			elif len(x) > 1:
				tile.append(x.strip())
		data[int(tile_num)] = tile
	return counter(matchSides(getSides(data)))

def counter(matches):
	num_matches = {}
	corners = []
	for tile in matches:
		remaining = 0
		for side in matches[tile]:
			if len(matches[tile][side]) > 1:
				remaining += 1
		num_matches[tile] = remaining
		if remaining == 2: corners.append(tile)
	return num_matches, corners

def matchSides(side_data):
	corresponds = {'T':'B','B':'T','L':'R','R':'L'}
	# check every tile in set
	for tile in side_data.keys():
		sides = side_data[tile]
		# check every side of tile
		for side in sides.keys():
			# compare with all other tiles in set
			othertiles = list(side_data.keys())
			if tile in othertiles: othertiles.remove(tile)
			for o in othertiles:
				for c in corresponds.keys():
					if sides[side] == side_data[o][c] or sides[side][::-1] == side_data[o][c]:
						side_data[tile][side] = ''
						side_data[o][c] = ''
						break
				else:
					continue
				break
	return side_data

def getSides(data):
	for tile in data.keys():
		sides = {}
		sides['T'] = data[tile][0] #top
		sides['B'] = data[tile][-1] #bottom
		sides['L'] = ''.join([x[0] for x in data[tile]]) #left
		sides['R'] = ''.join([x[-1] for x in data[tile]]) #right
		data[tile] = sides
	return data

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day20code.py <data-file>")
		sys.exit(1)
	val1, val2 = solution(sys.argv[1])
	print("Product of four corner tiles: {}".format(math.prod(val2)))
