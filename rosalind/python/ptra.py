#!/usr/bin/env python

from sys import argv
from Bio.Seq import translate


def parse_file(file_name):
    with open(file_name) as in_file:
        dna_seq = in_file.readline().strip()
        prot_seq = in_file.readline().strip()

    return dna_seq, prot_seq


def all_codings(dna_seq):
    tables = [1,2,3,4,5,6,9,10,11,12,13,14,15]
    return [translate(dna_seq, table = x, stop_symbol = '') for x in tables]


def compare(translations, prot_seq):
    for i, seq in enumerate(translations):
        if seq == prot_seq:
            idx = i+1
            if idx > 6:
                print idx+2
            else:
                print idx
            break    

if __name__ == "__main__":
    file_name = argv[1]
    dna_seq, prot_seq = parse_file(file_name)
    translations =  all_codings(dna_seq)
    compare(translations, prot_seq)
