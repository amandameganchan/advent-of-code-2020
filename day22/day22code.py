#!/bin/env python3

import sys
import re
from collections import defaultdict

def solution(filename):
	data = {1:[],2:[]}
	with open(filename) as f:
		player = -1
		for x in f:
			if 'Player 1' in x: player = 1
			elif 'Player 2' in x: player = 2
			elif x.strip() != '': data[player].append(int(x.strip()))
	return calculateScore(playGame(data))

def playGame(decks):
	while len(decks[1]) > 0 and len(decks[2]) > 0:
		decks = playTurn(decks)
	return decks[1] if len(decks[1]) > 0 else decks[2]

def playTurn(decks):
	player1 = decks[1].pop(0)
	player2 = decks[2].pop(0)
	if player1 > player2:
		decks[1].extend([player1,player2])
	elif player2 > player1:
		decks[2].extend([player2,player1])
	return decks

def calculateScore(winningDeck):
	score = 0
	multiplier = len(winningDeck)
	for index in range(len(winningDeck)):
		score += winningDeck[index] * multiplier
		multiplier -= 1
	return score

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day22code.py <data-file>")
		sys.exit(1)
	score = solution(sys.argv[1])
	print("The winning player's score is {}".format(score))
