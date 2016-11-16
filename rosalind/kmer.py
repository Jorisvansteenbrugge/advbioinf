#!/usr/bin/env python

from general import fastaToList
from sys import argv
from collections import defaultdict

import itertools


def getPossibilities(k = 4):
    kmer_counts = defaultdict(lambda: 0)

    for i in itertools.product("ATGC", repeat = k):
        kmer_counts["".join(i)]
    return kmer_counts




if __name__ == "__main__":
    k = 4
    sequence = fastaToList(argv[1])[0]
    kmer_counts = getPossibilities()


    for i in range(len(sequence) - (k -1)):
        kmer = sequence[i:i+k]
        kmer_counts[kmer] += 1


    kmer_list = sorted(kmer_counts.items(), key = lambda x:x[0])

    ordered_counts = [x[1] for x in kmer_list]
    print(" ".join(map(str, ordered_counts)))
