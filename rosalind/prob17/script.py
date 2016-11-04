#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
RNA Splicing
"""
from sys import argv

def getSequences(inFile):
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

def spliceIntrons(dna, seqs):
	for i in seqs:
		dna = dna.replace(i,"")

	return dna
def getRNA(dna):
	rna = ""
	for nuc in dna:
		if nuc == "T":
			rna += "U"
		else:
			rna += nuc

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

	return prot

if __name__ == "__main__":
	fileName = argv[1]
	seqs = getSequences(open(fileName))
	
	dna = seqs.pop(0)	
	spliced_dna = spliceIntrons(dna, seqs)
	rna = getRNA(spliced_dna)
	rna_codons = getCodons(rna)

	prot = translate(rna_codons)
	print(prot)

