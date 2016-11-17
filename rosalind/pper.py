#!/usr/bin/env python

import itertools
from sys import argv

n = int(argv[1])
k = int(argv[2])

ran = [x for x in range(n)]
count = 0
for i in itertools.permutations(ran, k):
    count +=1 

print(count % 1000000)

