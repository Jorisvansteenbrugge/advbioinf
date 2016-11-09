#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Function: Accepts a fasta formatted file and returns the id of the entry with the highest GC content
"""

from __future__ import division
from sys import argv


def calcGC(seq):
	total = len(seq)
	c = seq.count("C")
	g = seq.count("G")
	gc = c+g
	return (gc*100) / total
	

def parseSequences(fileName):
	contents = {}
	handle = open(fileName)

	ID = ""
	seq = ""
	for line in handle:
		line = line.strip()
		if line.startswith(">"):
			if seq != "":
				contents[calcGC(seq)] = ID
			ID = line.replace(">","").split()[0]
			seq = ""
			
		else:
			seq+=line

	contents[calcGC(seq)] = ID
	return contents

def getHighestGCid(contents):
	highest = max(contents.keys())
	print(contents[highest])
	print(highest)

if __name__ == "__main__":
	fileName = argv[1]
	contents = parseSequences(fileName)
	getHighestGCid(contents)
