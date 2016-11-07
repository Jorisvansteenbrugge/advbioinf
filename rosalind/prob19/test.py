#!/usr/bin/env python

"""
Author: Joris van Steenbrugge (adaptations from Stephen S. Montanus)
"""


import itertools
from sys import argv

def getSequences(inFile):
        """Return list of dna_seq
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


def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. 
    """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match


def scs(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length 
    """
    shortest_sup = None
    scs_list = [] # List of equal shortest common superstrings
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]  # superstring starts as first string

        for i in range(len(ss)-1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup  # found shorter superstring
            scs_list = [] # Replace list with new shorter superstring
            scs_list.append(sup)
        elif len(sup) == len(shortest_sup):
            scs_list.append(sup)
    return shortest_sup, scs_list  # return shortest

if __name__ == "__main__":
	strings = getSequences(open(argv[1]))
	s, shortestList = scs(strings)

	print "Length of Shortest Common Superstring:", len(s)
	print "Number of Shortest Common Superstrings:", len(shortestList)
	print "Shortest Common Superstrings:", sorted(shortestList)

