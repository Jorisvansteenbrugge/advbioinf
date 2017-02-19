#!/usr/bin/env python

from sys import argv
from itertools import permutations

def parse_infile(file_name):
    with open(file_name) as in_file:
        lenght = int(in_file.readline().strip())
        sequence = in_file.readline().strip()

    return map(int, sequence.split())

def get_ordered_subseqs(nums):
    """Given a list of numbers, find the longest increasing sequence"""
    L = [None for i in xrange(len(nums))]
    P = [None for i in xrange(len(nums))]
    for i in xrange(len(nums)):
        L[i] = 1  # longest increasing seq that ends in L[i]
        P[i] = -1 # pointer to reconstruct the sequence
        for j in xrange(i):
            if nums[j] < nums[i] and L[j] + 1 > L[i]:
                P[i] = j
                L[i] = L[j] + 1
    index = L.index(max(L))
    seq = [nums[index]]
    while P[index] > -1:
        index = P[index]
        seq.append(nums[index])
    seq.reverse()
    return seq


if __name__ == "__main__":
    seq = parse_infile(argv[1])
    assert type(seq) == list, "Seq is not a list"
    assert type(seq[0]) == int, "Seq items are not integers"
    print " ".join(map(str, get_ordered_subseqs(seq)))
    seq.reverse()
    rev = get_ordered_subseqs(seq)
    rev.reverse()
    print " ".join(map(str, rev))
