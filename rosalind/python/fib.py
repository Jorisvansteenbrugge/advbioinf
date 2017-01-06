#!/usr/bin/env python

from sys import argv



def calcRabbits(n,k):
    pairs = [1, 1]
    
    for i in range(2,n):
        try:
            f1 = pairs[i-1]
            f2 = pairs[i-2] * 3
            pairs.append((f1+f2))
        except IndexError:
            pass


    return pairs

if __name__ == "__main__":
    try:
        n = int(argv[1])
        k = int(argv[2])
        print(calcRabbits(n,k))
    except (IndexError, ValueError):
        print("Usage: python fib.py <intN> <intK>")


