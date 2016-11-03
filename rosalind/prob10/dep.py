#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Function: returns the reverse complement of a DNA sequence
"""
from sys import argv






def getCom(dna):
	switcher = {"A": "T", "T":"A", "G":"C","C":"G"}
	complement = ""
	for nuc in dna:
		complement += switcher[nuc]
	return complement

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
def getSubStrings(dna, dna_comp):
	#possible sizes defined in the excercise
	lengths = [4,5,6,7,8,9,10,11,12]
	for n in lengths:
		al = []
		#copy of dna that gets modified
		workingList = list(dna)
		while len(workingList) >= n:
			#Gets the n sized chunks of the string (non overlapping)
			kmers = [workingList[i:i+n] for i in range(0, len(workingList), n)]
			
			#last line is often not of n-size
			if kmers[-1] != n:
				kmers.pop(-1)
			for kmer in kmers:
				kmer = "".join(kmer)
				if getCom(kmer) in dna_comp:
					print(getCom(kmer))
					al.append(kmer)
			workingList.pop(0)
		print(list(set(al)))
		break
if __name__ == "__main__":
	fileName = argv[1]
	dna = parseSequences(fileName)
	dna_comp = getCom(dna)

	dna_revcomp = dna_comp[::-1]
	print(dna_comp)
	print(dna)
	#print(dna_revcomp)
	getSubStrings(tuple(dna), dna_comp)
