#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Consensus and Profile
"""
from sys import argv

def getMatrix(inFile):
	"""
	Parses a fasta file 
	lines: list of lines in FASTA format
	return matrix of dna sequences
	"""
	seqs = []
	seq = ""
	for line in inFile:
		if not line.strip():
			continue
		if line.startswith('>'):
			if seq != "":
				seqs.append(seq)
				seq = ""
		else:
			seq += line.strip()
	seqs.append(seq)
	return seqs

def getProfile(seqs):
	a = [0 for i in range(len(seqs[0]))]
	t = [0 for i in range(len(seqs[0]))]
	g = [0 for i in range(len(seqs[0]))]
	c = [0 for i in range(len(seqs[0]))]

	for seq in seqs:
		for i,j in enumerate(seq):
			if j == "A":
				a[i]+=1
			elif j == "T":
				t[i]+=1
			elif j == "G":
				g[i]+=1
			elif j == "C":
				c[i]+=1
	print(getMax(a,t,g,c))
	print("A: "+" ".join(map(str, a)))
	print("C: "+" ".join(map(str, c)))
	print("G: "+" ".join(map(str, g)))
	print("T: "+" ".join(map(str, t)))

def getMax(a, t, g, c):
	consensus = ""
	for i in range(len(a)):
		dic = {a[i]:"A", t[i]:"T", g[i]:"G", c[i]:"C"}
		maxi = max(dic.keys())
		consensus += dic[maxi]
	return consensus

if __name__ == "__main__":
	fileName = argv[1]
	seqs = getMatrix(open(fileName))
	

	getProfile(seqs)
