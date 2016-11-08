#!/usr/bin/env python

"""
Author: Joris van Steenbrugge & D.E. Bug ;)
"""

from sys import argv
import subprocess
import re

def getMax(palindromes):
	pass

def parse_fasta(lines):
    """Return dictionary of {label:dna_seq}
    
    lines: list of lines in FASTA format
    """
    seqs = {}
    for line in lines:
        if not line.strip():
            continue
        if line.startswith('>'):
            label = line.strip()
            seqs[label] = ""
        else:
            seqs[label] += line.strip()
    #yolo
    dnastring = "".join(seqs.values())
    return dnastring

def getComp(dna):
    """
    dna = Dictionary of {label: dnaseq}
    Returns the reverse compliment of the sequence in a dictionary of {label: revComp}
    """

    switcher = {"A":"T", "T":"A", "G":"C", "C":"G"}
    comp = ""
    for nuc in dna:
	comp += switcher[nuc] 
    return comp

       
def extract_kmers(seq, ksize):
    palindromes = {}
    for i in range(0, len(seq)-1,1):
#        print("{} {} {}".format(str(i), str(i+ksize), seq[i:i+ksize]))
        dna_kmer = seq[i:i+ksize]
        comp_kmer = getComp(dna_kmer)[::-1] 

        if len(dna_kmer) < ksize:
            continue
        else:
            if comp_kmer == dna_kmer:
                print("{} {}".format(i+1, ksize,))
#            else:
#                print("{} {}".format(dna_kmer, comp_kmer))

if __name__ == "__main__":
    # parse input data
    inp_fn = argv[1]
    dna_seq = parse_fasta(open(inp_fn))
    assert type(dna_seq) == str , "Seq is no string"
    
    #Extract k-mers  
    for kmerSize in [4, 6, 8, 10, 12]:
         kmers = extract_kmers(dna_seq, kmerSize)
      
        
