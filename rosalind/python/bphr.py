#!/usr/bin/env python

from __future__ import division
from sys import argv
from Bio import SeqIO


def parseFQ(file_name, qval):
    in_file = open(file_name)
    handle = SeqIO.parse(in_file, "fastq")
    count = 0

    phreds = []
    for record in handle:
        phred_vals =  record.letter_annotations["phred_quality"]
        phreds.append(phred_vals)

    pos_count = 0
    for i in range(len(phreds[0])):
        avg_phred = sum([x[i] for x in phreds]) / float(len(phreds))
       
        if avg_phred < qval:
            count += 1
    return count

print parseFQ(argv[1], int(argv[2]))
