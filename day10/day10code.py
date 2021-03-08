#!/bin/env python3

"""
adapters can be connected to other adapters with a
difference in voltage of 1-3; find a chain that uses 
all of the adapters given and find the number of 
1-jolt differences multiplied by the number of 3-jolt 
differences 

I assume the chain will just be all given adapters in
sorted order since they would have to be in ascending order
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

	dist = getDistribution(data)

	return dist[1] * dist[3]

def getDistribution(data):
	"""
	counts the frequency of differences between adjacent
	voltages, returns a dict with differences as keys and
	frequencies as values

	Args:
		data (list): input data; list of voltage #s

	Returns:
		dict: distribution of differences between adjacent voltages
	"""
	
	dist = defaultdict(lambda: 0)
	prev = 0
	
	# for each number in (sorted) list,
	# calculate the difference between 
	# the previous number and this one;
	# increment the frequency count for
	# this difference
	for d in sorted(data):
		diff = d - prev
		dist[diff] += 1
		prev = d

	dist[3] += 1	# add one more for my adapter

	return dist

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day10code.py <data-file>")
		sys.exit(1)
	answer = solution(sys.argv[1])
	print("The number of 1-jolt differences multiplied by the number of 3-jolt differences is {}".format(answer))
