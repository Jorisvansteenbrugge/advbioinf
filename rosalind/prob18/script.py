#!/usr/bin/env python
"""
Author: Joris van Steenbrugge
Finding a Spliced Motif
"""


import re


if __name__ == "__main__":
	s = "ACGTACGTGACG"
	t = "GTA"

	pattern = r'(?=())'


	orfs = ['ATG', 'ATGGGGA', 'ATGGGGATGACCCCGCGACTTGGAT', 'ATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAA', 'ATGACCCCGCGACTTGGAT', 'ATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAA', 'ATGATCCGAG']
	
	cleanList = [] #or whatever name
	for i in range(len(orfs)):
		issub = False
		for y in orfs:
			if orfs[i] in y:
				if orfs[i] == y:
					continue
				else:
					issub = True
					print(orfs[i])
		if issub == False:
                        cleanList.append(orfs[i])
		
	print(cleanList)
