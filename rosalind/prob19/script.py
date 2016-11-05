#!/usr/bin/env python

from difflib import SequenceMatcher
import itertools

def getOverlap(a,b):
	ahalf = len(a)/2
	bhalf = len(b)/2
	
	d = SequenceMatcher(None,a,b)
	match = max(d.get_matching_blocks(), key=lambda x:x[2])
	i,j,k = match
	max_overlap = d.a[i:i+k]
	
	if len(max_overlap) >= ahalf and len(max_overlap) >= bhalf:
		return max_overlap
	else:
		return None

def secondIt(a, prelim_superstring):
	ahalf = len(a)/2
	
	d = SequenceMatcher(None,a, prelim_superstring)
        match = max(d.get_matching_blocks(), key=lambda x:x[2])
        i,j,k = match
        max_overlap = d.a[i:i+k]

	print(max_overlap)

if __name__ == '__main__':
	a = "ATTAGACCTG"
	b = "CCTGCCGGAA"
	c = "AGACCTGCCG"
	d = "GCCGGAATAC"
	
	prelim_superstring = ""	
	for i in itertools.combinations([a,b,c,d],2):
		overlap = getOverlap(i[0],i[1])
		if overlap:
			prelim_superstring += overlap

	for i in [a,b,c,d]:
		secondIt(i, prelim_superstring)

	print("                                                 "+prelim_superstring)
