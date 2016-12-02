#!/usr/bin/env python

from __future__ import division

__author__ = "Joris van Steenbrugge"


from sys import argv
import subprocess as sp
import os
def parseFasta(file_name):
    with open(file_name) as in_file:
        sequences = []
        seq = "" 
        for line in in_file:
            if line.startswith(">"):
                if seq != "":
                    sequences.append(seq)

            else:
                seq += line.strip()
        sequences.append(seq)

    return sequences

def Nvalue(seq_array, N=50):
    seq_array = sorted(seq_array, reverse=True)
    n_size = 0
    total = sum([len(i) for i in seq_array])
    half = (total/100) * N
 

    idx = 0
    while n_size < half:
        n_size += len(seq_array[idx])
        idx += 1

    return total, n_size, idx

def runLastz(fasta, contigs, form="general", output="outlastz.txt"):
    if not os.path.exists(output):
        CMD = "lastz {} {} --format={} --output={}".format(fasta, contigs,
                                                    form, output)
        sp.call(CMD, shell=True)

    else:
        return

def parseLastOutput(output="outlastz.txt"):
    with open(output) as in_file:
        regions = []
        #skip header
        in_file.readline()

        for line in in_file:
            line = line.strip().split()
            regions.append((int(line[4]), int(line[5])))

    return sorted(regions, key = lambda x: x[0])


def mergePositions(positions, changed = True):
    if not changed:
        return positions

    changed = False
    merged = []
    idx = 0
    while idx < len(positions):
        try:
            a = positions[idx]
            b = positions[idx+1] 
            if a[0] <= b[1] and b[0] <= a[1]:
                changed = True
                mini = min(a[0], b[0])
                maxi = max(a[1], b[1])
                idx += 1
                merged.append((mini, maxi))
            else:
                merged.append(a) 

        except IndexError:
            merged.append(positions[idx])
        
        idx += 1
    return mergePositions(merged, changed)

def getUncovered(merged_positions, lenFasta):
    uncov_list = []
    for i in xrange(len(merged_positions)):
        start = merged_positions[i][0]
        prev_end = merged_positions[i-1][1]
        if i == 0:
            uncov = (0, start)
        else:
            uncov = (prev_end, start)
        
        uncov_list.append(uncov)

    uncov_list.append((merged_positions[-1][1], lenFasta))

    return uncov_list

def getSequences(fasta, uncov_list):
    print("Uncovered regions")
    total = 0
    for pos in uncov_list:
        start = pos[0]
        end = pos[1]
        sequence = fasta[0][start:end]
        total += len(sequence)
        print("{}:{}\n{}".format(str(start), str(end), sequence))
    return total

if __name__ == "__main__":
    f1, f2 = argv[1], argv[2] 
    fasta = parseFasta(f1)
    contigs = parseFasta(f2)
    runLastz(f1, f2)

    positions =  parseLastOutput()
    merged_pos = mergePositions(positions)

    uncov_list =  getUncovered(merged_pos,len(fasta[0]) )

    fasta_n50 = map(str, Nvalue(fasta))
    contig_n50 = map(str, Nvalue(contigs))

    print("{}: TOTAL={}; N50 SIZE={}; N50 INDEX={}".format(f1, fasta_n50[0], fasta_n50[1], fasta_n50[2]))
    print("{}: TOTAL={}; N50 SIZE={}; N50 INDEX={}".format(f2, contig_n50[0], contig_n50[1], contig_n50[2]))
    
    total = getSequences(fasta, uncov_list)

    print("Number of uncovered regions: {}".format(str(len(uncov_list))))
    print("Number of uncovered bases {}".format(str(total)))
