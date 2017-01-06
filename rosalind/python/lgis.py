#!/usr/bin/env python

from sys import argv
from itertools import permutations

#possible permutations
#look for the longest increasing one
#look for the longest decreasing one
# ?????
# Profit.

def getNPie(filePath):
    with open(filePath) as inFile:
        n = inFile.readline().strip()
        pie = inFile.readline().strip().replace(" ","")

    return int(n), pie



# 5 1 4 2 3
def parse(pie):

    for idx, val in enumerate(pie):
        if idx != 0:
            prev = pie[idx-1]
        next = 
            

if __name__ == "__main__":
    n, pie = getNPie(argv[1])

    current_increasing  = None

    parse(pie)
   # for k_size in range(n, 0, -1):
    #    for i in range(len(pie) - (k_size -1)):
     #       kmer = pie[i:i+k_size]
      #      print(kmer)
