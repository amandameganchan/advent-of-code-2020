#!/bin/env python3

"""
finds how many coloured bags can eventually
contain my shiny gold bag according to the rules
of which coloured bags must be contained in
which other coloured bags
"""

import sys
import re

def solution(filename):

	# read in input data
	input_data = []
	with open(filename) as f:
		for x in f:
			# split on the phrase 'bags contain' to get the
			# main bag colour and then the containing bags
			input_data.append(re.split("bags contain",x.strip()))

	bags = findContainingBags("shiny gold", input_data)
	return len(set(bags))

def findContainingBags(colour, bagData):
	"""
	recursive function to find bags that contain a given
	colour and bags that contain those colours, etc.

	Args:
		colour (string): given colour to search for containing bags
		bagData (list): input data; list of lists- inner lists have
		two elements, bag colour and the other coloured bags within

	Returns:
		list: list of colours that contain the given colour
	"""
	containedIn = [] # colours that contain bags of given colour

	# loop through rules; if given colour is present inside 
	# a bag, add that bag colour to containedIn
	for b in bagData:
		if colour in b[1]:
			containedIn.append(b[0].strip())
	# return empty list if given colour is not contained
	# in any other bags
	if not containedIn:
		return []
	# else recurse on each bag that contains the given colour
	# to find bags that contain those colours
	else: 
		for ci in containedIn:
			containedIn.extend(findContainingBags(ci,bagData))
		return containedIn

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day7code.py <data-file>")
		sys.exit(1)
	num_bags = solution(sys.argv[1])
	print("A shiny gold bag can be contained in {} other coloured bags.".format(num_bags))
