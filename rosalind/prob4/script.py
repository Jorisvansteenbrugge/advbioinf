#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Function: returns the reverse complement of a DNA sequence
"""
from sys import argv



def getSequence(fileName):
	seq = ""
	with open(fileName) as infile:
		for line in infile:
			seq += line.strip()
	return seq



def getRevCom(dna):
	switcher = {"A": "T", "T":"A", "G":"C","C":"G"}
	complement = ""
	for nuc in dna:
		complement += switcher[nuc]
	return complement[::-1]



if __name__ == "__main__":
	fileName = argv[1]
	dna = getSequence(fileName)
	print(getRevCom(dna))
