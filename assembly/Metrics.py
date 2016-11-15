#!/usr/bin/env python
import sys

def getEntrySizes(fileName):
    entry_sizes = []
    with open(fileName) as inFile:
        seq = ""
        for line in inFile:
            if line.startswith(">"):
                if seq != "":
                    entry_sizes.append(len(seq))
            else:
                seq += line.strip()
    entry_sizes.append(len(seq))

    return sorted(entry_sizes, reverse=True)

def getNMetric(fileName, N=50):
    entry_sizes = getEntrySizes(fileName)
   
    total = sum(entry_sizes)
    goal = 100.0 / float(N)
    half = total/goal
    

    incrementing_size = 0
    cur_size = 0
    for size in entry_sizes:
        if incrementing_size >= half:
            return cur_size
        else:
            incrementing_size += size
            cur_size = size

    
