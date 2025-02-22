#!/usr/bin/env python

from sys import argv
from itertools import product


def parseFile(fileName):
    with open(fileName) as inFile:
        s_list = inFile.readline().strip().split()
        k = int(inFile.readline().strip())

    return s_list, k

def getOrder(s_list):
    order = {}
    count = 1
    for x in s_list:
        order[x] = count
        count += 1

    return order

if __name__ == "__main__":
    s_list, k = parseFile(argv[1])
    order = "".join(s_list) 
    combinations = []

    count = k
    while count > 0:
        for i in product("".join(s_list), repeat = count):
            combinations.append("".join(i))
        count -= 1



    
    print("\n".join(sorted(combinations, key = lambda word: [order.index(x) for x in word])))



        
