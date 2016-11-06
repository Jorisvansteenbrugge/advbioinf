#!/usr/bin/env python

from difflib import SequenceMatcher
import itertools
import re

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

		

if __name__ == '__main__':
	a = "ATTAGACCTG"
	b = "CCTGCCGGAA"
	c = "AGACCTGCCG"
	d = "GCCGGAATAC"


	acp = a
	overlaps = []
	while(len(acp) > 0):
		substr = getOverlap(acp,b)
		overlaps.append(substr)
		acp = acp[1:]

	overlaps.sort(key=len)
	print(overlaps)
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
	superstring = pre + match + post
	print(superstring)
