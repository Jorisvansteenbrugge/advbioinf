#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Finds a shared motif in multiple sequences
"""

from sys import argv



def getSequences(inFile):
	"""
	Parses a fasta file 
	lines: list of lines in FASTA format
	return dictionary of {label:dna_seq}
	"""
	seqs = {}
	for line in inFile:
		if not line.strip():
			continue
		if line.startswith('>'):
			label = line.strip().replace(">","")
			seqs[label] = ""
		else:
			seqs[label] += line.strip()
	return seqs

def long_substr(data):
	substr = ''
	if len(data) > 1 and len(data[0]) > 0:
		for i in range(len(data[0])):
			for j in range(len(data[0])-i+1):
				if j > len(substr) and all(data[0][i:i+j] in x for x in data):
					substr = data[0][i:i+j]
	return substr



if __name__ == "__main__":
	fileName = argv[1]
	seqs = getSequences(open(fileName))
	print(long_substr(list(seqs.values())))
