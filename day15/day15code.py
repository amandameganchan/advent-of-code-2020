#!/bin/env python3

"""
following the rules of the game, determine
the nth number spoken by the players

rules:
-begin by taking turns reading from a list of starting 
numbers (puzzle input)
-then, each turn consists of considering the most recently 
spoken number:
	-if that was the first time the number has been spoken, 
	the current player says 0
	-otherwise, the number had been spoken before; the 
	current player announces how many turns apart the number 
	is from when it was previously spoken.
"""

import sys
import re
from collections import defaultdict

def solution(filename,final_turn):

	# read in input data
	data = []
	with open(filename) as f:
		for x in f:
			data.append(x.strip().split(','))
			
	return getTurn(data,int(final_turn))

def getTurn(data,final_turn):
	"""
	simulate playing the game to 
	determine the number spoken at turn
	final_turn

	Args:
		data (list): first starting numbers
		final_turn (int): desired turn to stop at

	Returns:
		int: number spoken aloud at that turn
	"""

	finalTurns = []

	# do for each set in data
	for starterset in data:
		# get number of nums in starter set
		nums = len(starterset)
		# keep track of:
		# current turn number
		turn = 0
		# last 2 turns any number was spoken on (if any)
		lastTurn = {}
		nextTurn = {}
		lastVal = -1
		# iterate until desired turn
		while turn < final_turn: # part 1: 2020, part 2: 30000000
			# first starting numbers
			if turn < nums:	currVal = int(starterset[turn])
			# subsequent turns
			else: currVal = nextTurn[lastVal]
			if currVal in lastTurn.keys(): nextTurn[currVal] = turn-lastTurn[currVal]
			else: nextTurn[currVal] = 0
			lastTurn[currVal] = turn	
			lastVal = currVal
			turn += 1
		finalTurns.append(lastVal)

	return finalTurns[0]

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("Usage: python3 day15code.py <data-file> <turn-number>")
		sys.exit(1)
	number = solution(sys.argv[1],sys.argv[2])
	print("{} will be the {}th number spoken".format(number,sys.argv[2]))