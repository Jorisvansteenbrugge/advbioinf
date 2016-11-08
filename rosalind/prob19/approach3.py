#!/usr/bin/env python

from sys import argv
import difflib
import re
import itertools

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

def getNonMatching(a, match):
        pattern = re.escape(match)

        for i in re.finditer(pattern, a):
                start = i.start()
                if start != 0:
                        pre = a[0:start]
                        return pre, True
                else:
                        post = a[start:]
                        return post, False

def getOverlap(template, newSeq):
	s = difflib.SequenceMatcher(None, template, newSeq)
	pos_a, pos_b, size = s.find_longest_match(0, len(template), 0, len(newSeq))
	return template[pos_a:pos_a+size]


def magic(sequences):
	overlaps = []
	for x in itertools.combinations(sequences,2):
		print(x)
                match = getOverlap(x[0], x[1])

		pre = ""
		post = ""
		for i in [x[0], x[1]]:
			substr, prepos = getNonMatching(i, match)
                	if prepos:
                        	pre += substr
                	else:
                        	post += substr

        	superstring = pre +  post
        	overlaps.append(superstring)
	return overlaps

if __name__ == "__main__":
	sequences = getSequences(open(argv[1]))
	overlap = magic(sequences)
	print(overlap)
	overlap = magic(overlap)
	print(overlap)
