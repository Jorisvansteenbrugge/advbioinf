#!/usr/bin/env python

from sys import argv

def parse_infile(file_name):
    with open(file_name) as in_file:
        lenght = int(in_file.readline().strip())
        sequence = in_file.readline().strip()

    return map(int, sequence.split())


def get_ordered_subseqs(seq):
    s_size = len(seq)
    for i in range(s_size):
        print(seq[i:])

if __name__ == "__main__":
    seq = parse_infile(argv[1])
    assert type(seq) == list, "Seq is not a list"
    assert type(seq[0]) == int, "Seq items are not integers"
    get_ordered_subseqs(seq)
