#!/usr/bin/env python


from general import fastaToList, hamming
from sys import argv


def func(a, b):
    c=0
    for j in range(32,41):
        for i in range(len(a)-j):
            c1=0
            for k in range(len(b)-j):
                if hamming(a[i:i+j], b[k:k+j])<=3:
                    c1+=1
                    if c1>c:
                        c=c1
    return c

seqA, seqB = fastaToList(argv[1])
print func(seqA, seqB)
print func(seqB, seqA)




