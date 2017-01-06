#!/usr/bin/env python

from sys import argv
import itertools



def order(data):
    keys = data.keys()
    keys = sorted(keys)
    for key in keys:
        vals = data[key]
        vals.append(key)
        vals = sorted(vals)
        for val in vals:
            print("{}{}".format(key,val))

def combinations(coll, n):
    data = {}
    for i in itertools.permutations(coll, n):
        if i[0] not in data.keys():
            data[i[0]] = [i[1]]
        else:
            data[i[0]].append(i[1])

    return data

if __name__ == "__main__":
    infile = open(argv[1])
    coll = infile.readline().strip().split()
    n = int(infile.readline().strip())
    
    combi = combinations(coll, n)
    order(combi)
