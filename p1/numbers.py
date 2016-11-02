#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Function: Counts up command line arguments
"""
from sys import argv

if __name__ == "__main__":
	numbers = argv[1:]
	print(" + ".join(map(str,numbers))+ " = "+ str(sum(map(int, numbers))))
