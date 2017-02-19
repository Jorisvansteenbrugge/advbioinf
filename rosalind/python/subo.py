#!/usr/bin/env python


from general import fastaToList, hamming
from sys import argv
import regex as re

r="TGCAACGGCGGTATTTACTTTACCTCTAGATC"


def findMatches(seq):
    matches = re.findall(r'(?:'+r+'){s<=3}', seq)
    print(len(matches))


seqA, seqB = fastaToList(argv[1])
findMatches(seqA)
findMatches(seqB)


