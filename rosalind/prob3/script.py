#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Function: Translateds RNA to DNA
"""

from sys import argv


def transcribe(dna):
	return dna.replace("T", "U")

def getDNAseq(fileName):
	seq = ""
	with open(fileName) as infile:
		for line in infile:
			seq+= line.strip()

	return seq

if __name__ == "__main__":
	fileName = argv[1]
	dna = getDNAseq(fileName)
	print(transcribe(dna))
