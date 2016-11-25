#!/usr/bin/env python

from sys import argv

def parseFile(fileName):
    with open(fileName) as in_file:
        in_file.readline()
        unsorted = in_file.readline().strip().split()

    return map(int, unsorted)



unsorted = parseFile(argv[1])
count = 0
for i in range(len(unsorted)):
    if i+1 < len(unsorted):
        a = unsorted[0:i+1]
        bpos = i+1
        b = unsorted[bpos]

        for x, val in enumerate(reversed(a)):
            if  val > b:
                count += 1
                unsorted[bpos] = val
                unsorted[bpos -1] = b 
                bpos -= 1
print(count)
