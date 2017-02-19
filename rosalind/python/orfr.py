#!/usr/bin/env python

from sys import argv

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

def get_seq(file_name):
    with open(file_name) as in_file:
        seq = ""
        for line in in_file:
            seq += line.strip()

    return seq


def read_frame(seq_frame):
    triplets = [seq_frame[x:x+3] for x in range(0,len(seq_frame), 3)] 
    amino = ""
    aminos = []   
    read = False
    for trip in triplets:
        if trip == "ATG":
            read = True 
        elif trip == "TAA" or trip == "TAG" or trip == "TGA":
            read = False
            if amino != "":
                aminos.append(amino)
            amino = ""
        if read:
            amino += codontable[trip]
    return aminos


if __name__ == "__main__":
    seq = get_seq(argv[1])

    print read_frame(seq[0:])
    print read_frame(seq[1:])
    print read_frame(seq[2:])

