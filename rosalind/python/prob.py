#!/usr/bin/env python

from __future__ import division
from math import log10
from sys import argv

def calc_gc(dna):
    gc = 0
    for nuc in dna:
        if nuc == 'G' or nuc == 'C':
            gc += 1
    return gc / len(dna)

def calc_prob(dna, array):
    chances = []
    assert type(array[0] ) == float, "not float"
    for perc in array:
        chance = 1.0
        gc = perc*0.5
        at = (1-(gc*2))*0.5

        for nuc in dna:
            if nuc == 'A' or nuc == 'T':
                chance *= at
            if nuc == 'G' or nuc == 'C':
                chance *= gc
        chances.append(log10(chance))


    return chances

def read_file(filename):
    with open(filename) as in_file:
        seq = in_file.readline().strip()
        probs = map(float, in_file.readline().strip().split())
    return seq, probs

seq, probs = read_file(argv[1])

print " ".join(map(str, calc_prob(seq, probs)))

#print " ".join(map(str, calc_prob("ACGATACAA", [0.129, 0.287, 0.423, 0.476, 0.641, 0.742, 0.783])))
