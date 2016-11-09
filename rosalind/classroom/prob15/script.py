#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Enumerating Gene Order
"""

from sys import argv
import itertools

def getPermMutations(n):
	combinations = []
	x = [str(i) for i in range(1,n+1)]
	return list(itertools.permutations(x, 6))


if __name__ == "__main__":
	n = int(argv[1])
	combinations = getPermMutations(n)

	print(len(combinations))
	for i in combinations:
		print(" ".join(i))
