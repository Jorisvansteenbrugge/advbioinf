#!/usr/bin/env python

from sys import argv
from general import fastaToList


def getRevComp(seq):
    comp_def = {'A': 'T', 'T': 'A',
                'G': 'C', 'C': 'G'}
    return "".join([comp_def[nuc] for nuc in seq[::-1]])

if __name__ == "__main__":
    seqs = fastaToList(argv[1])
    matching = 0
    for seq in seqs:
        if seq == getRevComp(seq):
            matching += 1

    print(matching)
