#!/bin/env python3

import sys
import re
from collections import defaultdict

def solution(filename):
	data = []
	with open(filename) as f:
		for x in f:
			data.append(x.strip())
	sum = 0
	for exp in data:
		subsum = evaluate(exp)
		sum += subsum
	return sum

def evaluate(expression):
	stack = []
	for char in expression:
		if char == ')':
			sub_exp = []
			current = ''
			while current != '(':
				sub_exp.append(current)
				current = stack.pop()
			sub_exp.reverse()
			stack.append(str(evalLR(''.join(sub_exp))))
		elif char != ' ': stack.append(char)
	return evalLR(''.join(stack))

def evalLR(expression):
	# assuming no parens here
	# input is a string
	stack = re.findall(r'(\d+|\+|\*)',expression)
	stack.reverse()
	current_num = eval(stack.pop()+stack.pop()+stack.pop())
	while stack:
		current_num = eval(str(current_num)+stack.pop()+stack.pop())
	return current_num

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: python3 day18code.py <data-file>")
		sys.exit(1)
	sumvalues = solution(sys.argv[1])
	print("The sum of the resulting values is {}".format(sumvalues))