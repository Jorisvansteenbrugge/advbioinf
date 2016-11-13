#!/usr/bin/env python
# coding=utf-8

from sys import argv

def find_overlaps(arr, acc=''):
    if len(arr) == 0:
        return acc

    elif len(acc) == 0:
        acc = arr.pop(0)
        return find_overlaps(arr, acc)

    else:

        for i in range(len(arr)):
            a = arr[i]
            l = len(a)

            for p in range(l / 2):
                q = l - p

                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return find_overlaps(arr, a[:p] + acc)

                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return find_overlaps(arr, acc + a[q:])

def getSequences(inFile):
    seqs = []
    seq = ""
    for line in inFile:
        if line.startswith(">"):
            if seq != "":
                seqs.append(seq)
                seq = ""
        else:
            seq += line.strip()
    seqs.append(seq)
    return seqs

if __name__ == "__main__":

    data = getSequences(open(argv[1]))
    print find_overlaps(data)

