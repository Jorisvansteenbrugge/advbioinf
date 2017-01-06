#!/usr/bin/env python
from math import factorial
from sys import argv

n = int(argv[1])
k = int(argv[2])


print((factorial(n) / factorial(n-k)) % 1000000)


