#!/bin/env python3

"""
find the total number of distinct ways you can 
arrange the adapters to connect the charging 
outlet to your device
"""

import sys
import re
from collections import defaultdict

def solution(filename):

	# read in input data
	data = []
	with open(filename) as f:
		for x in f:
			data.append(int(x.strip()))
	# add wall outlet and my adapter
	data.append(0)
	data.append(max(data) + 3)

	return find_paths({0:1},data)[max(data)]

def find_paths(pathStarts,data):
	"""
	recursive function to count how many paths stem
	from the given path starts

	Args:
		pathStarts (dict): dict containing the adapters to
		check future paths for and their current path counts
		data (list): input data; list of voltage #s

	Returns:
		dict: dict containing adapters one step ahead of an
		adapter given in pathStarts, with their current path
		counts; if the end has been reached, dict only contains
		final adapter
	"""

	# holds current adapters + their current path counts
	newPaths = defaultdict(int)	
	
	for p in pathStarts.keys():
		# if at the end, add current # paths
		# to dict
		if p == max(data):
			newPaths[p] += pathStarts[p]
		# else, check if next three numbers
		# exist in the data; for each existing
		# one, add to newPaths dict with the 
		# current number of paths as its value
		else:
			for i in range(1,4):
				if p+i in data:
					newPaths[p+i] += pathStarts[p]
	# if the dict keys only contains the last
	# adapter, we have reached the end
	if list(newPaths.keys()) == [max(data)]:
		return newPaths
	# else, recurse with the current adapters
	else:
		return find_paths(newPaths,data)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day10code2.py <data-file>")
		sys.exit(1)
	total = solution(sys.argv[1])
	print("The total number of distinct ways you can arrange the adapters is: {}".format(total))
