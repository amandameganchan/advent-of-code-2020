#!/bin/env python3

import sys
import re
from copy import deepcopy
from collections import defaultdict

def solution(filename):
	data = {1:[],2:[]}
	with open(filename) as f:
		player = -1
		for x in f:
			if 'Player 1' in x: player = 1
			elif 'Player 2' in x: player = 2
			elif x.strip() != '': data[player].append(int(x.strip()))
	return calculateScore(playGame(data)[0])

def playGame(decks):
	previous_rounds = []
	while len(decks[1]) > 0 and len(decks[2]) > 0:
		if decks in previous_rounds:
			return (decks[1],1)
		previous_rounds.append(deepcopy(decks))
		decks = playTurn(decks)
	return (decks[1],1) if len(decks[1]) > 0 else (decks[2],2)

def playTurn(decks):
	player1 = decks[1].pop(0)
	player2 = decks[2].pop(0)
	winner = -1
	if len(decks[1]) >= player1 and len(decks[2]) >= player2:
		r_deck = {1:decks[1].copy()[:player1],2:decks[2].copy()[:player2]}
		winner = playGame(r_deck)[1]
	else:
		if player1 > player2: winner = 1
		elif player2 > player1: winner = 2
	if winner == 1: decks[1].extend([player1,player2])
	elif winner == 2: decks[2].extend([player2,player1])
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
		print("Usage: python3 day22code2.py <data-file>")
		sys.exit(1)
	score = solution(sys.argv[1])
	print("The winning player's score is {}".format(score))
