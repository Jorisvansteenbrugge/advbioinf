#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Calculates the amount of possible transcripts based on a protein sequence
"""

from sys import argv


def calculatePossibility(seq):
	possibilities = 1 # we ignore atg
	chanceTable = {"F":2, "L":6, "I":3, "M":1, "V":4, "S":6, "P":4, "T":4, "A":4, "Y":2,
			"*":3, "H":2, "Q":2, "N":2, "K":2, "D":2, "E":2, "C":2, "W":1, "R":6,
			"G":4}
	for aa in seq:
		possibilities *= chanceTable[aa]
	return possibilities

def parseFile(fileName):
	seq = ""
	with open(fileName) as inFile:
		for line in inFile:
			seq += line.strip()

	return seq[1:] + "*" #removes atg as it is always expected

if __name__ == "__main__":
	fileName = argv[1]
	seq = parseFile(fileName)
	print(calculatePossibility(seq)%1000000)
