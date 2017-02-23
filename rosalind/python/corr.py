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
				print seq
				for vals in [key, other]:
					if vals not in keysToDel:
						keysToDel.append(vals)

	#removestep
	print "remove {}".format(" ".join(keysToDel))
	for remKey in keysToDel:
		del sequences[remKey]
	return sequences


def cycleBads(bad, good):
	from general import hamming, revcomp


	for key in bad.keys():
		for other in good.keys():
			if key == other:
				break
			
			normal_hammingdist = hamming(bad[key][1], good[other][1])
			rev_hammingdist = hamming(bad[key][1], revcomp(good[other][1]))
				
			print(normal_hammingdist)				
			print(rev_hammingdist)
			if normal_hammingdist == 1:
				print("{}->{}".format(bad[key], good[other]))		
			elif rev_hammingdist ==1:
				print("{}->{}".format(bad[key], revcomp(good[other])))		

sequences =  getSequences(argv[1])
bad_sequences = filterGood(sequences)
print bad_sequences
cycleBads(bad_sequences, sequences)
