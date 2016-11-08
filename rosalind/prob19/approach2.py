#!/usr/bin/env python

from sys import argv
import difflib
import re


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


def magic(template, sequences):
	skipped = []
	for i in range(len(sequences)):
                longestOverlap = ""
                longest = ""
                size = 0
                for seq in sequences:
                        overlap = getOverlap(template, seq)
                        if len(overlap) > size:
                                longestOverlap = overlap
                                longest = seq
                                size = len(overlap)


                if size > 0:
                        pre = ""
                        post = ""
                        for y in [template, longest]:
                                substr, prepos = getNonMatching(y, longestOverlap)
                                if prepos:
                                        pre = substr
                                else:
                                        post = substr

                        template = pre+post
                        sequences.remove(longest)

	return template, sequences

if __name__ == "__main__":
	sequences = getSequences(open(argv[1]))
	template = sequences.pop(0)

	count = 1
	while len(sequences) >= 1:
		print("Iteration {}".format(str(count)))
		print("Current size {}".format(str(len(sequences))))
		template, sequences = magic(template, sequences)	
		count += 1
	print(len(sequences))


	
