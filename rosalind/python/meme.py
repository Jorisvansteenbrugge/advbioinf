#!/usr/bin/env python
"""
This is going to be a wild ride through python land
"""
__author__ = "Joris van Steenbrugge"
from sys import argv
from Bio import SeqIO

def sliding_windows(seq, min_size = 20):
    max_size = len(seq)
    print max_size
    for i in xrange(min_size, max_size + 1):
        for x in xrange(max_size - i + 1):
            yield seq[x:x+i] 


def shared_motif(template, sequences):
    import regex

    subisets = sliding_windows(template)
    sequences.append(template)
    for seq in sequences:
        print regex.findall(r'(?:DLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFF){s<=4}', str(seq), regex.BESTMATCH)

def get_sequences(file_name):
    sequences = []
    handle = open(file_name, "rU")
    for record in SeqIO.parse(handle, "fasta"):
        sequences.append(record.seq)

    template = sequences.pop(0)
    return template, sequences

if __name__ == "__main__":
    file_name = argv[1]
    template, sequences = get_sequences(file_name)
    shared_motif(template, sequences)
