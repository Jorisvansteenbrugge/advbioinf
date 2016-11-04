#!/urs/bin/env python
"""
Author: Joris van Steenbrugge
Extract various types of information from a genbank file
"""

from __future__ import division
from sys import argv


class GbEntry(object):
	"""
	Class objet to store genbank entries
	"""	
	def __init__(self, accession):
		self.accession = accession
		self.seq = ""
	def setOrganism(self, organism):
		self.organism = organism

	def addToSequence(self, sequence):
		self.seq += sequence

	def getSequence(self):
		return self.seq

	def getGCcontent(self):
		gc = self.seq.count("g") + self.seq.count("c")
		return "{0:.2f}".format((100*gc)/len(self.seq))

	def getSeqLength(self):
		return str(len(self.seq))

	def getAccession(self):
		return self.accession

	def getOrganism(self):
		return self.organism
	
	def __str__(self):
		return "{} for organism: {}".format(self.accession, self.organism)

	def __repr__(self):
		return self.accession

def parseFile(fileName):
	"""
	Parses the genbank file and retrieves the required information, 
	and store the info in GbEntry objects
	"""
	with open(fileName) as inFile:
		entries = []
		entry = None
		read = False
		for line in inFile:
			line = line.strip()
			if line.startswith("LOCUS"):
				if entry:
					entries.append(entry)
		
				accession = line.split()[1]
				entry = GbEntry(accession)

			elif line.startswith("ORGANISM"):
				organism = line.split()[1:]
				entry.setOrganism(" ".join(organism))

			elif line.startswith("ORIGIN"):
				read = True
				continue
			if read:
				if line.startswith("//"):
					read = False
				else:
					entry.addToSequence("".join(line.split()[1:]))
		entries.append(entry)

	return entries

def orderEntries(entries):
	"""
	Sort all GbEntry object based on gc content in reverse order
	"""
	return sorted(entries, key=GbEntry.getGCcontent, reverse=True)

def writeFasta(entries):
	with open("entries.fa","w") as outFile:
		for entry in entries:
			outFile.write(">{} {}\n".format(entry.getAccession(),
					entry.getOrganism()))
			outFile.write("{}\n".format(entry.getSequence()))	

def writeTabFile(entries):
	with open("info.tsv","w") as outFile:
		for entry in entries:
			outFile.write("{}\t{}\t{}\t{}\n".format(entry.getAccession(),
								entry.getOrganism(),
								entry.getGCcontent(),
								entry.getSeqLength()
								))

if __name__ == "__main__":
	entries = parseFile(argv[1])
	sortedEntries = orderEntries(entries)
	writeFasta(sortedEntries)
	writeTabFile(sortedEntries)
