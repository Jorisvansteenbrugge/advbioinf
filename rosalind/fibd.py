#!/usr/bin/env python
from sys import argv


def fibo(n, m):
    count = 2
    pairs = [1, 1]
    while count < n:
        if count < m:
            pairs.append(pairs[-2] + pairs[-1])
        elif count == m or count == m+1:
            pairs.append(pairs[-2] + pairs[-1] - 1)
        else:
            pairs.append((pairs[-2] + pairs[-1]) - pairs[-(m+1)])
        count += 1
 

    return pairs


if __name__ == "__main__":
    n = int(argv[1])
    m = int(argv[2])

    print(fibo(n, m))
