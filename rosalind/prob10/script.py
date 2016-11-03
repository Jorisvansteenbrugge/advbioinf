#!/usr/bin/env python

"""
Author: Joris van Steenbrugge & D.E. Bug ;)
"""

from sys import argv
import subprocess
import re

def parse_fasta(lines):
    """Return dictionary of {label:dna_seq}
    
    lines: list of lines in FASTA format
    """
    seqs = {}
    for line in lines:
        if not line.strip():
            continue
        if line.startswith('>'):
            label = line.strip()[0:]
            seqs[label] = ""
        else:
            seqs[label] += line.strip()[0:]
    return seqs

def getRevComp(dna):
    """
    dna = Dictionary of {label: dnaseq}
    Returns the reverse compliment of the sequence in a dictionary of {label: revComp}
    """

    switcher = {"A":"T", "T":"A", "G":"C", "C":"G"}
    dna_revcomp = {}
    for (i,y) in dna.items():
        comp = "".join([switcher[x] for x in y])
        dna_revcomp[i] = comp[::-1]
    
    return dna_revcomp

def extract_kmers(seqs, k=15, skip_unknown=True):
    """
    Return dict of {kmer_seq: kmer_count}
    seqs: dict of {label:dna_seq}
    k: int, specifying k-mer size
    skip_unknown: bool, specifying wheter k-mers containing non-TGAC characters
        should be skipped
    """
    kmer_size = k
    ch = {} #dict to store characters
    res = [] #list to store k-mers
    for label, seq in seqs.items():
        for c in seq:
            if c not in ch:
                ch[c] = 0
            ch[c] += 1
        for i in range(len(seq)-kmer_size+1):
            kmer = seq[i:i+kmer_size]
            count = True
            for c in kmer:
                if c not in "TGAC":
                    count = False
            if skip_unknown is True and count is False:
                continue
            res.append(kmer)
    return res

def revPalingdrome(kmer, dna_seqs):
    for (i,seq) in dna_seqs.items():
        match = r'(?=(' + re.escape(kmer) + r'))'
        matches = re.finditer(match, seq)
        [print(str(i.start()+1)+" "+str(len(kmer))) for i in matches]
        

if __name__ == "__main__":

    # parse input data
    inp_fn = argv[1]
    dna_seqs = parse_fasta(open(inp_fn))
    revcomp = getRevComp(dna_seqs)
    assert type(dna_seqs) == dict , "Seq is no dict"
    
    #Extract k-mers  
    for kmerSize in [4,5,6,7,8,9,10,11,12]:
        kmer_len = kmerSize
        kmers = extract_kmers(revcomp, skip_unknown=True, k=kmer_len)
        assert type(kmers) == list, "kmers is no list"
        
        for kmer in set(kmers):
            revPalingdrome(kmer, dna_seqs)	
