#!/usr/bin/env python

from __future__ import division
from sys import argv
from Bio import SeqIO

#Trim on the end


asc = {0:33,1:34,2:35,3:36,4:37,5:38,6:39,7:40,8:41,9:42,10:43,11:44,12:45,13:46,14:47,15:48,16:49,17:50,18:51,19:52,20:53,21:54,22:55,23:56,24:57,25:58,26:59,27:60,28:61,29:62,30:63,31:64,32:65,33:66,34:67,35:68,36:69,37:70,38:71,39:72,40:73,41:74, 42:75}

def parseFQ(file_name, qval):
    global asc
    in_file = open(file_name)
    handle = SeqIO.parse(in_file, "fastq")
    for record in handle:
        seq = list(record.seq)
        phred_vals =  record.letter_annotations["phred_quality"]
        
        changed = True
        while changed:
            changed = False
            assert type(phred_vals[0]) == int, "phred_val not an int"
            if phred_vals[0] < qval:
                phred_vals.pop(0)
                seq.pop(0)
                changed = True


        seq = seq[::-1]
        phred_vals = phred_vals[::-1]

        changed = True
        while changed:
            changed = False
            if phred_vals[0] < qval:
                phred_vals.pop(0)
                seq.pop(0)
                changed = True

        seq = seq[::-1]
        phred_vals = phred_vals[::-1]

        asci = map(chr, [asc[x] for x in phred_vals])
        print("@{}".format(record.name))
        print("".join(seq))
        print("+")
        print("".join(asci))
parseFQ(argv[1], int(argv[2]))
