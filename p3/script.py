#!/usr/bin/env python
"""
Calculates different metrics (min/max/avg read length, avarage quality per position. 
And compares these metrics between raw reads and trimmed reads
"""

from __future__ import division
from sys import argv
import subprocess as sp
import os

__author__ = "Joris van Steenbrugge (950416798110)"
__version__ = "1.0"
__date__ = "07 November 2016"
__maintainer__ = "Joris van Steenbrugge"
__email__ = "joris.vansteenbrugge@wur.nl"
__licence__ = "GPL"
__status__ = "Development"



class Read(object):
	"""
	Class object to store a sequence read in.
	"""
	
	def setLabel(self, label):
		self.label = label

	def setSeq(self, seq):
		self.seq = seq

	def setQuality(self, quality):
		"""
		Accepts the quality line from the fastq entry, additionally calculates
		the illumina 1.5 int version of the quality scores.
		"""
		self.quality = quality
		self.translated_quality = [ord(i)-64 for i in self.quality]
	
	def getSeqLength(self):
		return len(self.seq)

	def getTranslatedQuality(self):
		return self.translated_quality

def ParseFQ(fileName):
	"""
	Parses a fastq file in illumina 1.5 format.
	"""
	with open(fileName) as inFile:
		read_list = []
		
		while(True):
			current_read = Read()	

			label = inFile.readline().strip()
			seq = inFile.readline().strip()
			plusLine = inFile.readline().strip()
			quality = inFile.readline().strip()
			
			# Stops iterating when the file buffer is empty
			if label == "" and seq == "" and plusLine == "" and quality == "":
				break
			else:
				current_read.setLabel(label)
				current_read.setSeq(seq)
				current_read.setQuality(quality)

			read_list.append(current_read)
		return read_list

def getAVGqualities(sorted_read_list):
	"""
	Calculates the avarage nucleotide quality per position. 
	Uses the longest read to indicate the number of positions that need to be checked
	
	sorted_read_list: Read objects sorted on sequence length from lowest to highest
	return: String with the avarage qualities for the max read length
	"""

	longest_read = sorted_read_list[-1].getSeqLength()
	consensus_quality = []
	
	for i in range(longest_read):
		total = 0
		count = 0
	
		for q in sorted_read_list:
			q = q.getTranslatedQuality()
			try:
				total += q[i]
				count += 1
			
			except IndexError:
				pass
		consensus_quality.append(total / count)

	return consensus_quality

def trimQualities(inputName, threshold = 30, Q = 64, output = "trimmed.fq"):
	"""
	Trims read qualites using the fastq_quality_trimmer command line utility.
	inputName: fastq file to be trimmed
	threshold: quality score minimum (default = 30)
	Q: Specifies the quality scale (default = 64 for illumina 1.5)
	output: output file for the trimmed reads to be stored (default= trimmed.fq)
	"""

	# Checks if the output file exists, if yes skips the trimming process
	if os.path.exists(output):
		return
	# Command line arguments
	cmd = "fastq_quality_trimmer -t {} -Q {} -i {} -o {}".format(threshold, Q, 
								inputName, output)
	# Runs on the command line using subprocess
	sp.call(cmd, shell=True)

def reportMinMaxAvg(sorted_read_list, name):
	"""
	Prints the minimum, maximum and avarage read lenghts to the shell
	sorted_read_list: list of Read objects sorted based on sequence length from low to high
	name: name to be printed in the shell (ORIGINAL or TRIMMED)
	"""

	#first way of doing this	
	minimum = sorted_read_list[0].getSeqLength()
	maximum = sorted_read_list[-1].getSeqLength()
	
	#second way of doing this
	avg = sum([i.getSeqLength() for i in sorted_read_list]) / float(len(sorted_read_list))
	
	print("{}: min={}, max={}, avg={:.2f}".format(name, str(minimum), str(maximum), avg))

def reportQualities(original, trimmed):
	"""
	Prints a tab seperated output of the comparison of positional avarage quality between
	the original and trimmed reads
	"""
	assert len(original) == len(trimmed), "Length between orignal and trimmed should be identical"
	
	for i in range(len(original)):
		diff = trimmed[i] - original[i]
		print("{}\t{:.2f}\t{:.2f}\t{:.2f}".format(i+1, original[i], trimmed[i], diff))


if __name__ == "__main__":
	# Original reads
	read_list = ParseFQ(argv[1])
	sorted_read_list = sorted(read_list, key = Read.getSeqLength)

	# Trimmed reads
	trimQualities(argv[1])	
	trimmed_read_list = ParseFQ("trimmed.fq")
	sorted_trimmed_read_list = sorted(trimmed_read_list, key = Read.getSeqLength)
	
	# Positional quality scores
	trimmed_avg_quality = getAVGqualities(sorted_trimmed_read_list)
	avg_quality = getAVGqualities(sorted_read_list)


	# Reporting output
	reportMinMaxAvg(sorted_read_list, "ORIGINAL")
	reportMinMaxAvg(sorted_trimmed_read_list, "TRIMMED")
	reportQualities(avg_quality, trimmed_avg_quality)

