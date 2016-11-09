#!/usr/bin/env python

from __future__ import division
from sys import argv




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

def parseSeq(seqa, seqb):
	transitions = 0
	transversions = 0

	switcher = {"T": ["G", "A", "T"], "G": ["T", "G", "C"], "A": ["A", "C", "T"], "C": ["G", "A", "C"]}

	for a,b in zip(seqa, seqb):
		if b in switcher[a]:
			if b == a:
				pass
			else:
				transversions += 1
		else:
			transitions += 1 	
	
	print(transitions)
	print(transversions)
	print(transitions/transversions)
if __name__ == "__main__":
	seqs = getSequences(open(argv[1]))
	seqa = seqs[0]
	seqb = seqs[1]
	parseSeq(seqa, seqb)
