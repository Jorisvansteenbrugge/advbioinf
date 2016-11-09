#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Calculates the O3 overlap graph as an adjacency list
"""

from sys import argv
import itertools




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

def getOverlap(a, b, k=3):
	"""
	Gets the overlap between a and b
	a: dna sequence a
	b: dna sequence b
	returns: true for a match and true for a reverse
	"""

	astart = a[0:k]
	aend = a[len(a)-k:len(a)]
	
	bstart = b[0:k]
	bend = b[len(b)-k:len(b)]

	match = False
	rev = False
	
	if astart == bend:
		rev = True
		match = True
	if  aend == bstart:
		rev =  False
		match = True
	return match, rev
	



def combine(seq):
	"""
	Gets the O3 overlap between sequences
	seq: Dictionary of the sequences {label:dna_seq}
	return: the adjecency list
	"""

	for a,b in itertools.combinations(seq.keys(), 2):
		match, rev = getOverlap(seq[a],seq[b])
		if match:
			if rev:	
				print("{} {}".format(b, a))
			else:
				print("{} {}".format(a, b))

if __name__ == "__main__":
	fileName = argv[1]
	seq = getSequences(open(fileName))
	combine(seq)	
