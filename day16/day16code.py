#!/bin/env python3

import sys
import re
from collections import defaultdict

def solution(filename):
	data = []
	with open(filename) as f:
		for x in f:
			if ':' in x:
				data.append(re.split(':',x.strip()))
			elif ',' in x:
				data.append(x.strip().split(','))
	return getError(data,getAcceptedNums(data))

def getError(data,accepted):
	otherTickets = data[24:]
	errors = 0
	for t in otherTickets:
		for n in t:
			if int(n) not in accepted:
				errors += int(n)
	return errors

def getAcceptedNums(data):
	ranges = []
	acceptable = []
	for line in data:
		if re.search('[a-z ]+',line[0]):
			ranges.extend(re.findall(r'\d+-\d+',line[1]))	
	for r in ranges:
		ends = re.split('-',r)
		for n in range(int(ends[0]),int(ends[1])+1):
			acceptable.append(n)
	return list(set(acceptable))

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day16code.py <data-file>")
		sys.exit(1)
	error = solution(sys.argv[1])
	print("The ticket scanning error rate is: {}".format(error))
