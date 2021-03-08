#!/bin/env python3

import sys
import re
import copy
from collections import defaultdict

def solution(filename):
	data = []
	with open(filename) as f:
		dim0 = []
		for x in f:
			dim0.append(list(x.strip()))
		data.append(dim0)
	cycles = 6
	state = data
	for _ in range(cycles):
		state = simulateCycle(padDim(state))
	return countActive(state)

def countActive(state):
	active = 0
	for z in state:
		for y in z:
			for x in y:
				if x == '#': active += 1
	return active

def padDim(data):
	x_len = len(data[0][0]) + 2
	y_len = len(data[0]) + 2
	for dim_z in range(len(data)):
		for dim_y in range(y_len-2):
			new_x = ['.'] + data[dim_z][dim_y] + ['.']
			data[dim_z][dim_y] = new_x
		data[dim_z].insert(0,['.'] * x_len)
		data[dim_z].append(['.'] * x_len)
	blank_dim = [[['.'] * x_len] * y_len]
	new_data = copy.deepcopy(blank_dim)
	new_data.extend(data)
	new_data.extend(blank_dim)
	return new_data

def simulateCycle(data):
	newState = [[[0 for x in range(len(data[0][0]))] for y in range(len(data[0]))] for z in range(len(data))]
	for z in range(len(data)):
		for y in range(len(data[0])):
			for x in range(len(data[0][0])):
				newState[z][y][x] = getStateChange([x,y,z],getCubesAndStates(data))
	return newState

def getCubesAndStates(state):
	# note: data is organized as [z,y,x]
	cubes_states = {}
	zs = len(state)
	ys = len(state[0])
	xs = len(state[0][0])
	for x in range(xs):
		for y in range(ys):
			for z in range(zs):
				cubes_states[(x,y,z)] = state[z][y][x]
	return cubes_states

def getNeighbours(coords): # coords = [x,y,z]
	neighbours = []
	for x in [coords[0]-1,coords[0],coords[0]+1]:
		for y in [coords[1]-1,coords[1],coords[1]+1]:
			for z in [coords[2]-1,coords[2],coords[2]+1]:
				neighbours.append([x,y,z])
	neighbours.remove(coords)
	return neighbours

def getStateChange(coords,cubes_states): # coords = [x,y,z]
	current_cube = cubes_states[tuple(coords)] if tuple(coords) in cubes_states.keys() else '.'
	active_neighbours = 0
	for n in getNeighbours(coords):
		if tuple(n) in cubes_states.keys() and cubes_states[tuple(n)] == '#':
			active_neighbours += 1
	# If a cube is active and exactly 2 or 3 of its neighbors are also active, 
	# the cube remains active. Otherwise, the cube becomes inactive.
	if (current_cube == '#' and not (active_neighbours == 2 or active_neighbours == 3)):
		current_cube = '.'
	# If a cube is inactive but exactly 3 of its neighbors are active, 
	# the cube becomes active. Otherwise, the cube remains inactive.
	elif current_cube == '.' and active_neighbours == 3:
		current_cube = '#'
	return current_cube

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day17code.py <data-file>")
		sys.exit(1)
	active = solution(sys.argv[1])
	print("{} cubes are left in the active state".format(active))