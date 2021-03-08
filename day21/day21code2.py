#!/bin/env python3

import sys
import re
from itertools import chain
from collections import defaultdict

def solution(filename):
	data = []
	with open(filename) as f:
		for x in f:
			line = re.split(r' \(contains ',x)
			allergens = line[1].strip()[:-1].split(', ')
			data.append((allergens,line[0].split()))
	return determineAllergens(data)

def removeAllergen(allergen, name, data):
	# remove all occurrences of allergen from the dictionary
	for d in data:
		# remove allergens 
		if allergen in d[0]:
			d[0].remove(allergen)
		# remove names 
		if name in d[1]:
			d[1].remove(name)
	return data

def determineAllergens(data):
	allergen_map = {}
	# get list of allergens
	allergens = list(set(list(chain.from_iterable([[a for a in k[0]] for k in data]))))
	# for each allergen: get all ingredients that have that allergen and see which is common to all
	while len(allergen_map.keys()) < len(allergens):
		to_find = [al for al in allergens if al not in allergen_map.keys()]
		for a in to_find:
			n = getCommonAllergens(a, data)
			# if only one common to all, assign as name
			if len(n) == 1: 
				allergen_map[a] = n[0]
				data = removeAllergen(a,n[0],data)
	names = []
	for i in sorted(allergen_map):
		names.append(allergen_map[i])
	return ','.join(names)

def getCommonAllergens(allergen, data):
	# find common name in all ingredients listed with allergen
	ing_lists = [a[1] for a in data if allergen in a[0]]
	common = set(ing_lists[0])
	for ing in ing_lists[1:]:
		common.intersection_update(ing)
	return list(common)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day21code2.py <data-file>")
		sys.exit(1)
	ingredients = solution(sys.argv[1])
	print("Canonical dangerous ingredient list: {}".format(ingredients))
