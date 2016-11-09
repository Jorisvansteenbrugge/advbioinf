#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Finding a Spliced Motif
"""

from sys import argv
import re

def getMatches(t, s):
	"""
	Uses regular expressions to find a match
	t: the motif
        s: the "full" dna string
	
	return: the matchobject
	"""
	pattern = r'(?=(G[ATGC]*T[ATGC]*A))'
	matches = re.findall(pattern,s)
	return matches


def getMatchingPositions(t,s, match):
	"""
	Calculate the positions of the characters from t in s, based on the matched string
	t: the motif
	s: the "full" dna string
	match: the match object	

	return: a list of positions
	"""
	if matches: # checks if a match was found
		match = matches[0] #We can take any match, so just take the first one
		positions = []
		prev = 0 # previous is set at 0 by default

		# Lets determine the locations of the characters of t in s
		for i in t:
			for pos, char in enumerate(s):
				if char == i:
					# Checks if matches are found in order
					if pos > prev:
						positions.append(str(pos+1))
						prev = pos
						break
					else:
						pass
	return positions

def getST(fileName):
	with open(fileName) as inFile:
		seqs = []
		seq = ""
		for line in inFile:
			if line.startswith('>'):
				if seq != "":
					seqs.append(seq)
					seq = ""
			else:
				seq += line.strip()

		seqs.append(seq)
	return seqs

if __name__ == "__main__":
	seqs = getST(argv[1])
	assert len(seqs) == 2, "Exactly 2 fasta entries need to be present"
	s = seqs[0]
	t = seqs[1]
	matches = getMatches(t,s)
	print(" ".join(getMatchingPositions(t,s,matches)))

			
	
