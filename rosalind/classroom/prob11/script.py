#!/usr/bin/env python
"""
Author: Joris van Steenbrugge

Steps: 

1. parse file for uniprot ids
2. Retrieve the sequence from the url
3. Scan the sequence for motifs
4. Return the protein id + matching locations
"""
import requests
from sys import argv
import re

def getSequence(id):
	seq = ""
	fileContent = ""
	file_handle = requests.get("http://uniprot.org/uniprot/{}.fasta".format(id))
	for line in file_handle:
		line = str(line, 'utf-8')
		fileContent += line
	fileContent = fileContent.split("\n")[1:]
	
	seq = "".join(fileContent)
	return seq


def parseFile(fileName):
	"""
	Retrieves uniprot IDs from file
	:param fileName:  The input file path
	:return: A dictionary with {Uniprot IDs: seq}
	"""
	ids = {}
	with open(fileName) as inFile:
		for line in inFile:
			uniID = line.strip()
			seq = getSequence(uniID)
			ids[uniID] = seq
	return ids



def getMatches(ids):
	for (uniID,seq) in ids.items():
		match = r'(?=(N[^P][ST][^P]))'
		matches = re.finditer(match,seq)
		
		pos = " ".join(map(str,[i.start()+1 for i in matches]))
		if pos != "":
			print(uniID)
			print(pos)


if __name__ == "__main__":
	fileName = argv[1]
	ids = parseFile(fileName)
	getMatches(ids)

