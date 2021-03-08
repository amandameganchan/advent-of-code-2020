#!/bin/env python3

"""
find the number of questions asked by anybody
in the group; sum over all groups
find the number of questions asked by everybody
in the group; sum over all groups

groups are delimited by blank lines
group members are delimited within groups by newlines
"""

import sys

def solution(filename):
	# read in input data
	input_data = [] 
	with open(filename) as f:
		# ensure people stay within their groups
		group = []
		for x in f:
			# at empty lines, flush the previous group
			if not x.strip():
				input_data.append(group)
				group = []
			# else continue to add to the group
			else:
				group.append(x.strip())
		input_data.append(group)

	return find_any(input_data), find_all(input_data)

def find_any(data):
	"""
	find total number of any questions that appear in 
	a group by joining all people in a group and taking
	the length of their set of questions

	Args:
		data (list): list of groups where each group contains 
		a list of people (each person is represented by
		a string of characters representing their questions)
	Returns:
		int: sum over all groups
	"""
	total = 0
	for group in data:
		total += len(set(''.join(group)))
	return total

def find_all(data):
	"""
	find total number of all common questions that appear in 
    a group by taking the set intersections of all people 
    and finding the length

	Args:
		data (list): list of groups where each group contains 
		a list of people (each person is represented by
		a string of characters representing their questions)
	Returns:
		int: sum over all groups
	"""
	total = 0
	for group in data:
		common_qs = set(group[0])
		for person in group[1:]:
			common_qs = common_qs.intersection(set(person))
		total += len(common_qs)
	return total

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day6code.py <data-file>")
		sys.exit(1)
	any_qs, all_qs = solution(sys.argv[1])
	print("Sum of questions answered by anyone in the group: ", any_qs)
	print("Sum of questions answered by everyone in the group: ", all_qs)
