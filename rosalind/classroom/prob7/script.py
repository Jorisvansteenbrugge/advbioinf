#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Function: COnverts a RNA sequence into a protein sequence
"""
from sys import argv


def getRNAseq(fileName):
	rna = ""
	with open(fileName) as infile:
		for line in infile:
			rna += line.strip()

	return rna

def getCodons(rna):
	n = 3
	triplets = [rna[i:i+n] for i in range(0, len(rna), n)]
	return triplets

def translate(triplets):
	prot = ""
	codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    		"UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    		"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
		"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
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
			if aa == "STOP":
				pass
			else:
				prot += aa.upper()

	print(prot)
			
if __name__ == "__main__":
	fileName = argv[1]
	rna = getRNAseq(fileName)
	triplets = getCodons(rna)
	translate(triplets)
