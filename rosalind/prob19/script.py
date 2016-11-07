#!/usr/bin/env python

from sys import argv
from difflib import SequenceMatcher
import itertools
import re



def getSequences(inFile):
	"""Return dictionary of {label:dna_seq}
	lines: list of lines in FASTA format
	"""
	seqs = []
	seq = ""
	for line in inFile:
		if line.startswith('>'):
			if seq != "":
				seqs.append(seq)
				seq = ""
		else:
			seq  += line.strip()
	seqs.append(seq)
	return seqs

def getOverlap(a,b):
	matches = []
	match = ""
	prev = ""
	count = 0
	read = True
	while (read == True):
		if count != len(a):
			val = a[count]
			prev = match
			match = match + val

			if match in b:
				pass

			else:
				matches.append(prev)
				match = ""

		else:
			read = False
			matches.append(match)
		count += 1
    
	if len(matches[0]) > len(matches[-1]):
		return matches[0]
	else:
		return matches[-1]

def getNonMatching(a, match):
	pattern = re.escape(match)

	for i in re.finditer(pattern, a):
		start = i.start()
		if start != 0:
			pre = a[0:start]
			return pre, True
		else:
			post = a[start:]
			return post, False

		
def getSuperString(a,b):
	acp = a
	
	overlaps = []
	while(len(acp) > 0):
		substr = getOverlap(acp,b)
		overlaps.append(substr)
		acp = acp[1:]

	overlaps.sort(key=len)
	
	match = overlaps[-1]
	superstring = ""

	pre = ""
	post = ""
	for i in [a,b]:
		substr, prepos = getNonMatching(i,match)
		if prepos:
			pre = substr
		else:
			post = substr
	superstring = pre +  post
	return superstring

if __name__ == '__main__':
	a = "ATTAGACCTG"
	b = "CCTGCCGGAA"
	c = "AGACCTGCCG"
	d = "GCCGGAATAC"
	
	sequences = getSequences(open(argv[1]))
	print(sequences)
	superstr = sequences.pop(0)

	for seq in sequences:		
		superstr = getSuperString(superstr,seq)

	print(superstr)



