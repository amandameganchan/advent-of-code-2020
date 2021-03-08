#!/bin/env python3

import sys
import re
from collections import defaultdict

def solution(filename):
	data = []
	with open(filename) as f:
		for x in f:
			data.extend(list(x.strip()))
	data = list(map(int, data))
	return collectLabels(playGame(data))

def collectLabels(final_cups):
	# start at 1 and collect cups clockwise
	# do not include 1 and remember to wrap
	final_string = final_cups[final_cups.index(1)+1:]
	final_string.extend(final_cups[:final_cups.index(1)])
	return ''.join(list(map(str,final_string)))

def playGame(cups):
	current_cup = cups[0]
	for _ in range(100):
		current_cup, cups = makeMove(current_cup,cups)
	return cups

def makeMove(current_cup, cups):
	# pop next 3 cups starting from after index of current cup
	pop_cups = [cups.pop((cups.index(current_cup)+1)%len(cups)),
				cups.pop((cups.index(current_cup)+1)%len(cups)),
				cups.pop((cups.index(current_cup)+1)%len(cups))]
	# select destination cup: current_cup's label - 1
	dest_cup = current_cup - 1 if current_cup > 1 else 9
	# if this cup is one of the removed, subtract 1 again and repeat
	# note if number goes below 1, wrap aroud to 9
	while dest_cup not in cups:
		dest_cup = dest_cup - 1 if dest_cup > 1 else 9
	# place the removed cups next to the destination cup
	# in the same order and immediately next to dest cup
	cups[cups.index(dest_cup)+1:cups.index(dest_cup)+1] = pop_cups
	# select new current_cup: cup immediately clockwise next to current cup
	new_index = cups.index(current_cup)+1 if cups.index(current_cup) < 8 else 0
	new_current = cups[new_index]
	return new_current, cups

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day23code.py <data-file>")
		sys.exit(1)
	labels = solution(sys.argv[1])
	print("Labels on the cups after cup 1: {}".format(labels))