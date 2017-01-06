#!/usr/bin/env python

from sys import argv
import itertools

def parseFile(fileName):
    with open(fileName) as inFile:
        s_list = inFile.readline().strip().split()
        k = int(inFile.readline().strip())

    return s_list, k


if __name__ == "__main__":
    s_list, k = parseFile(argv[1])

    for x in s_list: 
        for i in range(1,k+1):
            print(x*i)
        
