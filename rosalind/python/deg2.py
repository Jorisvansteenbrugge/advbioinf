#!/usr/bin/env python3

from sys import argv


def parseFile(fName):
    combs = []
    with open(fName) as inFile:
        nsize, esize= inFile.readline().strip().split()
        for line in inFile:
            combs.append(line.strip().split())
    return combs, nsize

if __name__ == '__main__':
    combs, nsize =  parseFile(argv[1])
    for i in range(1, int(nsize)+1):
        i = str(i)
