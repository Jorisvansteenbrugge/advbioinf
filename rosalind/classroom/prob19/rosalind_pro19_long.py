#!/usr/bin/env python

from __future__ import division

__author__ = "Joris van Steenbrugge"
__version__ = "2.0"
__date__ = "11 November 2016"
__email__ = "joris.vansteenbrugge@wur.nl"
__status__ = "Development"

from sys import argv
import re
import itertools


def getSequences(inFile):
    """Parses a fasta file and retrieves the labels and sequences

    Keyword arguments:
        inFile -- open file object containing lines in FASTA format
    Returns:
        seqs -- A dictionary of {label:dna_seq}
    """
    seqs = {}
    for line in inFile:
        if not line.strip():
            continue
        if line.startswith('>'):
            label = line.strip()[1:]
            seqs[label] = ""
        else:
            seqs[label] += line.strip()
    return seqs

def getHeadTailOverlap(seqA, seqB):
    """Returns the maximum overlap between seqA and seqB 
    
    The overlap is determined from start/end to somewhere in the middle,
    or from the middle to the start/end. No overlaps in the center.

    Keyword arguments:
        seqA -- The first sequence to overlap as a string
        seqB -- The second sequence to overlap as a str

    This function should be more modular
    The re pattern testing could be replaced
    Returns a None type object if no overlap was found
    """
    possible_overlaps = []

    a = seqA
    b = seqB
        
    for i in range(len(a)):
        fragment = a[0:i+1]
        start_pat = "(^{})".format(fragment)
        end_pat = "({}$)".format(fragment)
        if re.match(start_pat, b) or re.match(end_pat, b):
            possible_overlaps.append(fragment)


        # This could be more modular
    for i in range(len(a)-1, -1, -1):
        fragment = a[i:]
        start_pat = "(^{})".format(fragment)
        end_pat = "({}$)".format(fragment)
        if re.match(start_pat, b) or re.match(end_pat, b):
            possible_overlaps.append(fragment)
    try:
        if max(possible_overlaps, key=len) == 0:
            print(possible_overlaps)
        return max(possible_overlaps, key=len)
    except ValueError:
        return None



def getSuperstring(start, overlaps, sequences):
    """Return the calculated superstring
    
    Keyword arguments:
        start -- The label of the starting string
        overlaps -- A dictionary of {label:[connecting_label, overlap_start, overlap_length]}
        sequences -- A dictionary of {label:sequence}
    
    Based on the overlap dictionary structure the superstring is created in steps.
    
    There might be some mistake here
    """
    superstring = sequences[start]
    next = start
    while next:
        try: 
            
            nextstr = sequences[next]
            connected_with = overlaps[next]
    
            if connected_with:
                b = connected_with[0]
                
                #This approach does not require start
                start = connected_with[1]
                length = connected_with[2]
                seqB = sequences[b]

                # The overlap should already be present in the superstring
                #so the tailing part of seqB is added 
                superstring+= seqB[length:]
                next = b
            else:
                next = None
        except:
            next = None

    return superstring

            
        
if __name__ == "__main__":
    sequences = getSequences(open(argv[1]))

    overlaps = {}

    print("Making Combinations")
    for seqs in itertools.permutations(sequences.keys(), 2):
        seqA = sequences[seqs[0]]
        seqB = sequences[seqs[1]]
        overlap = getHeadTailOverlap(seqA, seqB)

        #overlap exists
        if overlap:
            #overlap covers at least half of both sequences
            if len(overlap) >= (len(seqA) / 2.0) and len(overlap) >= (len(seqB) / 2.0):
                #print("{}\t{}\t{}".format(seqs[0],seqs[1],sequences[seqs[0]].index(overlap))) 
                overlaps[seqs[0]] = [seqs[1], sequences[seqs[0]].index(overlap), len(overlap)]


    # Defining the starting position of the "network"
    values = [x[0] for x in overlaps.values()]
    start = [x for x in overlaps.keys() if x not in values]

    print(overlaps)   
#    print("CreatingSuperString")
#    print(getSuperstring(start[0],overlaps,sequences))

