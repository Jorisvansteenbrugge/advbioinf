#!/usr/bin/env python

from sys import argv
import difflib
import re


def getSequences(inFile):
        """
	Extracts dna sequences of a fasta file
	return: List of dna_seq
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

def getNonMatching(a, match):
	"""
	Calculates the string present before or after the match (the overlap that was found between 2 seqs
	"""
        pattern = re.escape(match)

        for i in re.finditer(pattern, a):
                start = i.start()
		
		# If the match starts not at the start of a
                if start != 0:
                        pre = a[0:start]
                        return pre, True
		# If it does start at the start of a
                else:
                        post = a[start:]
                        return post, False


def getOverlap(template, newSeq):
	"""
	Calculates the maximum overlap between 2 sequences. Coded this myself as well in another script but shorter code give more overview.
	"""
	s = difflib.SequenceMatcher(None, template, newSeq)
	pos_a, pos_b, size = s.find_longest_match(0, len(template), 0, len(newSeq))
	return template[pos_a:pos_a+size]


def process(template, sequences):
	"""
	Gets the overlap between the template and the other sequences
	"""
	for seq in sequences:
		overlap = getOverlap(template, seq)
		if len(overlap) > len(seq)/2:

			for y in [template, seq]:
				substr, prepos = getNonMatching(y, overlap)
				if prepos:
					pre = substr
				else:
					post = substr

			template = pre+post

	return template

if __name__ == "__main__":
	sequences = tuple(getSequences(open(argv[1])))
	superstrings = []

	#template = magic(template, sequences)


	# This is designed that each sequence is used as template once, so multiple possible superstrings
	#are create
	for i in range(len(sequences)):
                seqs = list(sequences)
                superstr = seqs.pop(i)
                superstr = process(superstr,seqs)
                superstrings.append(superstr)


	#possible superstrings sorted on length
	superstrings = sorted(superstrings, key=len)

	#get longest
	print(superstrings[-1])
