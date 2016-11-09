#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Finding motifs in DNA

"""

import re
from sys import argv

def findMotif(s, t):
    match = r'(?=('+re.escape(t)+ r'))'
    matches = re.finditer(match, s)
    matches = [str(i.start()+1) for i in matches]
    print(" ".join(map(str, matches)))


def getSequences(fileName):
    with open(fileName) as inFile:
        s = inFile.readline().strip()
        t = inFile.readline().strip()
    return s, t

if __name__ == "__main__":
    s, t = getSequences(argv[1])

    findMotif(s, t)
