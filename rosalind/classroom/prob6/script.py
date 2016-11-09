#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Function: Calcuates the hamming distance between 2 dna string
"""

import sys





def getSequences(fileName):
	a = ""
	b = ""
	with open(fileName) as infile:
		a = infile.readline().strip()
		b = infile.readline().strip()
	return a, b


def sanityCheck(a,b):
	if not len(a) == len(b):
		print("Please provide input sequences of equal size")
		sys.exit(1)
	else: 
		return True

def getHammingDistance(a,b):
	distance = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			distance +=1
	print(distance)

if __name__ == "__main__":
	fileName = sys.argv[1]
	a, b = getSequences(fileName)
	
	if sanityCheck(a,b):
		getHammingDistance(a,b)
