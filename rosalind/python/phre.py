#!/usr/bin/env python

from __future__ import division
from sys import argv
from Bio import SeqIO


def parseFQ(file_name, qval):
    in_file = open(file_name)
    handle = SeqIO.parse(in_file, "fastq")
    count = 0

    for record in handle:
        phred_vals =  record.letter_annotations["phred_quality"]
        avg_phred = sum(phred_vals) / float(len(phred_vals))
        if avg_phred < qval:
            count += 1
    return count

print parseFQ(argv[1], int(argv[2]))
