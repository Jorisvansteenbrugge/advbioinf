#!/usr/bin/env python

from sys import argv
from Bio import SeqIO
from itertools import combinations

def getSequences(file_name):
    sequences = {}
    handle = SeqIO.parse(open(file_name), 'fasta')
    for entry in handle:
        sequences[entry.id] = str(entry.seq)
    return sequences

def filterGood(sequences):
	from general import revcomp

	keysToDel = []
	for key in sequences.keys():
		seq = sequences[key]
		seq_revc = revcomp(seq)
		for other in sequences.keys():
			if key == other:
				break
			if seq == sequences[other] or seq == revcomp(sequences[other]) or seq_revc == sequences[other] or seq_revc == revcomp(sequences[other]):
			#debug this step
				for vals in [key, other]:
					if vals not in keysToDel:
						keysToDel.append(vals)

	#removestep
	for remKey in keysToDel:
		del sequences[remKey]
	return sequences


def cycleBads(sequences):
	from general import hamming, revcomp


	for key in sequences.keys():
		for other in sequences.keys():
			if key == other:
				break
			for comb in combinations((sequences[key], revcomp(sequences[key]),
				sequences[other], revcomp(sequences[other])), 2):
				hammingdist = hamming(comb[0], comb[1])
				if hammingdist == 1:
					print("{}->{}".format(sequences[key], sequences[other]))		
			

sequences =  getSequences(argv[1])
bad_sequences = filterGood(sequences)
print bad_sequences
cycleBads(bad_sequences)
