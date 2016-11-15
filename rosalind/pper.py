#!/usr/bin/env python

import itertools
from sys import argv

n = int(argv[1])
k = int(argv[2])


n_list = "".join([str(x) for x in range(n)])


count = 0
for i in range(len(n_list)-k+1):
    count +=1


print count
