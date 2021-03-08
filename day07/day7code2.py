#!/bin/env python3

"""
finds how many bags my shiny gold bag must
contain according to the rules of which
coloured bags must be contained in which
other coloured bags and in what quantity
"""

import sys
import re
from collections import defaultdict

def solution(filename):
	
	# read in input data
	data = []
	with open(filename) as f:
		for x in f:
			data.append(re.split("bags contain",x.strip()))

	# clean up and better format the rules, then use
	# those to compute total bags within given colour
	tidy_rules = howManyWithin(data)
	total = computeWithin("shiny gold",tidy_rules)

	return total

def computeWithin(colour, rules):
	"""
	recursive function to find how many bags
	are within a given colour bag, and how many
	are within those bags, etc.

	Args:
		colour (string): the given colour to find how 
		many bags are within
		rules (dict): dictionary of clean formatted rules

	Returns:
		int: total number of bags that are within the
		bag of the given colour
	"""
	total = 0

	# loop through quantity/colour pairs in the rule
	containing = rules[colour]
	for ctuple in containing:
		# if bag does not contain any other bags
		# add 0
		if ctuple[0] == 0:
			total += 0
		# else, recurse on the inside bag to find how many bags are
		# within that one, and multiply by the quantity before adding
		# to the total
		else:
			total += int(ctuple[0]) * (1 + computeWithin(ctuple[1],rules))

	return total

def howManyWithin(bagData):
	"""
	tidies up each rule; formats them as a 
	dictionary with the colour as the key
	and a list of (quantity,colour) tuples
	as its value (this is its rule)

	Args:
		bagData (list): input data; list of lists- inner lists have
		two elements, bag colour and the other coloured bags within

	Returns:
		dict: dictionary of tidied up rules
	"""
	clean = defaultdict(None) # rules tidied up

	# loop through each rule
	for b in bagData:
		# add main colour to rule dictionary
		main_colour = b[0].strip()
		clean[main_colour] = []
		# loop through list of quantity/colour 
		# pairs in the rule 
		for i in re.split(",",b[1]):
			# if rule contains a digit
			if re.findall(r'\d+',i):
				# find the digit quantity and colour
				num = re.findall(r'\d+',i)[0]
				colour = re.split(r'\d+',i)[1].strip()
				# remove final period and the word bag or bags
				if '.' == colour[-1]:
					colour = colour[:-1]
				colour = colour[:-5] if 'bags' in colour else colour[:-4]
				# add (quantity,tuple) to the main colour bag's rule
				clean[main_colour].append((num,colour)) 
			# if no digit quantity, the bag does not contain any 
			# other bags; add a (0,None) tuple as the rule
			else:
				clean[main_colour].append((0,None))

	return clean	

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day7code2.py <data-file>")
		sys.exit(1)
	num_bags = solution(sys.argv[1])
	print("A shiny gold bag must contain {} bags.".format(num_bags))
