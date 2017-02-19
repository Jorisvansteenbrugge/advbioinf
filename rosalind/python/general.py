#!/usr/bin/env python

def fastaToList(fileName):
    """ Parses a fasta file and retrieves the sequences
    fileName: The filepath of the fasta file
    return: A list object with fasta sequences
    """

    inFile = open(fileName)
    sequences = []
    seq = ""
    for line in inFile:
        if line.startswith('>'):
            if seq != "":
                sequences.append(seq)
                seq = ""
        else:
            seq += line.strip()

    sequences.append(seq)
    return sequences

def parseNonFasta(fileName):
    """Parses a non-fasta file and retrieves the sequence.

    fileName: The filepath of the non-fasta file
    return: A string with only the sequence
    """

    inFile = open(fileName)
    seq = ""
    for line in inFile:
        seq += line.strip()

    return seq


def hamming(seqA, seqB):
    if len(seqA) != len(seqB):
        raise ValueError("Strings should be of equal length" )

    count = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            count += 1

    return count

    
