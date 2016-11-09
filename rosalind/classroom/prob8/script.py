#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Function: Accepts a fasta formatted file and returns the id of the entry with the highest GC content
"""

from __future__ import division
from sys import argv
import re

def getCodingRegions(prot):
	matches = re.finditer(r'(?=(M[A-Z]*\*))', prot)
	matchList = []

	if matches:
		for i in matches:
			match = i.group(1)
			m = match.count("M")
			if m > 1:
				matchList.append(match.strip("*"))
				index = match.index("M")
				match = match[0:index] + match[index-1:]
				matchList.append(match.strip("*"))
			else:
				out = match.strip("*")
				if out != "":
					matchList.append(out)
	return matchList
	
def getFullProt(triplets):
	prot = ""
	codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
                "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
                "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
                "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
                "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
                "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
                "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
                "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
	for i in triplets:
                if len(i) == 3:
                        aa = codons[i]
                        if aa == "*":
				prot += aa
                        else:
                                prot += aa.upper()
	return getCodingRegions(prot)
	
def getCodons(rna):
        n = 3
        triplets = [rna[i:i+n] for i in range(0, len(rna), n)]
	return triplets

def parseSequences(fileName):
	handle = open(fileName)

	ID = ""
	seq = ""
	for line in handle:
		line = line.strip()
		if line.startswith(">"):
			if seq != "":
				contents[calcGC(seq)] = ID
			ID = line.replace(">","").split()[0]
			seq = ""
			
		else:
			seq+=line
	return seq

def getRevCom(dna):
        switcher = {"A": "T", "T":"A", "G":"C","C":"G"}
        complement = ""
        for nuc in dna:
                complement += switcher[nuc]
        return complement[::-1]

def setFrames(rnas):
	protList = []
	for i in rnas:
		f1 = i
		f2 = i[1:]
		f3 = i[2:]

		c1 = getCodons(f1)
		c2 = getCodons(f2)
		c3 = getCodons(f3)
		

		protList += getFullProt(c1) + getFullProt(c2) +  getFullProt(c3)
	for i in list(set(protList)):
		if i != "" or i != " ":
			print(i)
	

if __name__ == "__main__":
	fileName = argv[1]
	dna = parseSequences(fileName)
	dna_revcomp = getRevCom(dna)

	rna = dna.replace("T","U")
	rna_revcomp= dna_revcomp.replace("T","U")
	setFrames([rna, rna_revcomp])
