#!/usr/bin/env python
"""Alligns 2 sequences in fasta format using Needle,
and calculates different metrics based on the alignment.
This approach uses a custom class to store alignment object
Others might to it different ofcourse.
"""
from __future__ import division

__author__ = "Joris van Steenbrugge"
__version__ = "1.0"
__date__ = "11 Nov. 2016"
__email__ = "joris.vansteenbrugge@wur.nl"

from os import path
from sys import argv
import subprocess as sp

class Alignment(object):
    """Object to store needle alignments in
    """
    def __init__(self):
        """Initiates some variables.
        Seq a and b are initated as emtpy strings so sequences
        can be added line by line while parsing needle output
        """
        self.seqA = ""
        self.seqB = ""
        self.labelA = None
        self.labelB = None

    def addToSeqA(self, seq):
        self.seqA += seq
    
    def addToSeqB(self, seq):
        self.seqB += seq

    def getSeqAlen(self):
        return len(self.seqA)

    def getSeqBlen(self):
        return len(self.seqB)

    def setLabelA(self, labelA):
        """Adds the label for seqA if not already present"""
        if not self.labelA:
            self.labelA = labelA

    def getLabelA(self):
        return self.labelA

    def setLabelB(self, labelB):
        """Adds the label for seqB if not already present"""
        if not self.labelB:
            self.labelB = labelB

    def getLabelB(self):
        return self.labelB

    def getHamming(self):
        """Returns the hamming distance between seqA and B
        Uses the geHammingDistance() function
        """
        return getHammingDistance(self.seqA, self.seqB)


    def getIdent(self):
        """Returns the percentage Identity between seqA and seqB
        """
        return getIdent(self.seqA, self.seqB)

def getSequence(inFile):
        """Returns the first/only sequence in a fasta file

        Keyword arguments:
            inFile -- file object containing lines in FASTA format
        Returns:
            seqs -- A String of sequence

        Labels are not stored
        Multiple entries in a fasta file are ignored
        """
        seq = ""
        for line in inFile:
            if line.startswith('>'):
                pass
            else:           
                seq += line.strip()
        return seq


def getHammingDistance(seqA, seqB):
    """Returns the hamming distance between two sequences

    Keyword arguments:
        seqA -- A String of sequence A
        seqB -- A String of sequence B
    Returns:
        distance -- An Integer representing the hamming distance
    """
    distance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            distance +=1
    return distance

def getIdent(seqA, seqB):
    """Returns the identity score as a percentage

    Keyword arguments:
        seqA -- A String of sequence A
        seqB -- A String of sequence B
    Returns:
        distance -- An Integer representing the hamming distance
    """
    ident = 0
    for i in range(len(seqA)):
        try:
            if seqA[i] == seqB[i]:
                ident += 1
        except:
            continue

    # The try catch is probably not required as if the identity was 0
    #it would not have ended up in the alignment
    try:
        #cause of the future division import percentage is becomes a float
        percentage =  (ident/len(seqA)) * 100 
    except:
        percentage = 0
    return percentage

def runNeedle(seqA_path, seqB_path, needle_output):
    """Calls the needle alignment program from the command line

    Keyword arguments:
        seqApath -- The location of sequence A's fasta file
        seqBpath -- The location of sequence B's fasta file
        needle_output -- The name of the output file for Needle
    Returns:
         -- When the alignment output file already exists
    """
    CMD = "needle -asequence {} -bsequence {} -gapopen 8 -gapextend 0.5 -outfile out.needle".format(
            seqA_path, seqB_path, needle_output)
    if path.exists("out.needle"):
        return
    
    sp.call(CMD, shell=True)



def parseNeedleOutput(path):
    """Returns a list with Alignment objects based on needle output

    Keyword arguments:
        path -- The filepath of the needle output
    Returns:
        alignments -- A list of Alignment objects

    The function creates seperate Alignment objects at run time
    for each alignment present in the needle output. Different information
    per alignment is extracted from the output file:
        - Sequence labels (A and B)
        - Sequences (A and B)

    The counter variable is used to determine which line of the non-comment lines
    contains what information (further explained using in-line comments)
    """
    alignments = []
    alignment_object = Alignment()
    count = 0

    with open(path) as needleOutput:
        for line in needleOutput:
            #Reading will indicate if the line is a comment or a non comment
            reading = False
            if line.startswith("#"): # if not comment/meta-information
                reading = False

                # Only usefull for the first Alignment since alignment_object
                #is still empty here
                if alignment_object.getLabelA():
                    alignments.append(alignment_object)
                    alignment_object = Alignment()

            #If the line is not a comment, it can be empty, which we dont want
            else:
                if line.strip() != "":
                    reading = True


            #There might be prettier ways to do this (a result of time restriction)
            #please share ideas if you know one
            if reading:
                # Count 0 contains labelA and sequence A
                if count == 0:
                    try:
                        line = line.strip().split()
                        alignment_object.setLabelA(line[0])
                        alignment_object.addToSeqA(line[2])
                    except IndexError:
                        pass
                # Count 1 contains the alignment information which we ignore
                elif count == 1:
                    pass
                # Count 2 contains LabelB and sequence B
                elif count == 2: 
                    # Count set to -1 because a few lines down it is incremented 
                    #back to 0
                    count = -1    
                    line = line.strip().split()
                    alignment_object.setLabelB(line[0])
                    alignment_object.addToSeqB(line[2])

                #Count is incremented for each non-comment line
                count += 1
    return alignments


def report(alignments):
    """Prints calculated metrics to stdout
    
    Keyword arguments:
        alignments -- A list containing Alignment objects
    """
    print("Sequence1\tLength\tSequence2\tLength\tHamm\tIdent")
    for i in alignments:
        labelA = i.getLabelA()
        labelB = i.getLabelB()
        lengthA = i.getSeqAlen() 
        lengthB = i.getSeqBlen()
        hamm  = i.getHamming()
        ident = i.getIdent()
        
        print("{}\t{}\t{}\t{}\t{}\t{}".format(labelA, lengthA,
                                              labelB, lengthB,
                                              hamm, ident))

if __name__ == "__main__":
    #Gets file paths from the command line
    seqA_path = argv[1]
    seqB_path = argv[2]
    needleOutput = "out.needle" # always out.needle

    #Retrieve the sequences for both fasta files
    seqA = getSequence(open(argv[1]))
    seqB = getSequence(open(argv[2]))
    
    #Run the needle program using the files
    runNeedle(argv[1], argv[2], needleOutput)

    #Get alignment objects from the needle output
    alignments = parseNeedleOutput(needleOutput)

    #report Metrics
    report(alignments)

