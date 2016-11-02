#!/usr/bin/env python
import re

def findMotif(s,t):
	q = re.compile(t)
	found = [item.start(0) for item in q.finditer(s, overlapped=True)]
	print(found)
	"""
	a = True
	while a:
		pos = s.find(t)
		if pos == -1:
			a = False
		else:
			print(pos)
			s = s[:pos] + s[pos+1:]
		
	"""
	

if __name__ == "__main__":
	s = "GATATATGCATATACTT"
	t = "ATA"
	findMotif(s,t)
