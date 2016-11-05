#!/usr/bin/env python
import re
#steps
# 1: getsequence
# 2: getRevcomp
# 3: get kmers of revcomp
# 4: match them back on the template
# ??????
# Profit

from sys import argv

def extract_kmers(seq, k=4):
    """
    Return list of kmers
    seqs: String of dna sequence
    k: int, specifying k-mer size
    """
    kmer_size = k
    ch = {} #dict to store characters
    res = [] #list to store k-mers

    for c in seq:
        if c not in ch:
            ch[c] = 0
        ch[c] += 1
    for i in range(len(seq)-kmer_size+1):
        kmer = seq[i:i+kmer_size]
        res.append(kmer)
    assert len(res) == len(seq)-kmer_size+1, "Not all k-mers were called"
    return res

def getMatch(kmer, seq, total):
    """
    Returns the matching positions for the current kmer
    :param kmer: The current kmer, derrived from the revcomp sequence
    :param seq: The DNA sequence
    :param total: a dictionary
    :return:
    """
    match = r'(?=(' + re.escape(kmer) + r'))'
    matches = re.finditer(match, seq)
    for i in matches:
        start = i.start()
        kmerLen = len(kmer)

        # Check if we already have the longest kmer on the starting position
        if start in total.keys():
            if kmerLen <= total[start]:
                continue
        total[start] = kmerLen

    return total

def getRevComp(dna):
    """
    Convert a DNA sequence into it's reverse complement conterpart
    :param dna: dna sequence as a String
    :return: the complementary sequence in reverse order as String
    """
    switcher = {"A":"T","T":"A","C":"G","G":"C","X":"X"}
    comp = ""
    for nuc in dna:
        comp += switcher[nuc]
    return comp[::-1]

def getSequence(fileName):
    """
    Single entry fasta parser
    :param fileName: inpute fasta file with only 1 entry
    :return: the dna sequence as a String
    """
    ID = ""
    seq = ""
    with open(fileName) as inFile:
        for line in inFile:
            line = line.strip()
            if line.startswith(">"):
                ID = line.replace(">", "").split()[0]
                seq = ""
            else:
                seq += line
    return seq

def printOut(total):
    for (i,y) in total.items():
        print(i, y)

def process(dna, revcomp):
    total = {}
    for i in [4,5,6,7,8,9,10,11,12]:
        kmers = extract_kmers(revcomp, k=i)
        for kmer in kmers:
            if kmer in dna:
                getMatch(kmer, dna, total)

    printOut(total)

if __name__ == "__main__":
    fileName = argv[1]
    dna = getSequence(fileName)
    revcomp = getRevComp(dna)


    print(dna)
    print(revcomp)

    process(dna, revcomp)

