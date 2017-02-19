#!/usr/bin/env python

from sys import argv

def get_seq(file_name):
    with open(file_name) as in_file:
        seq = ""
        for line in in_file:
            seq += line.strip()

    return seq


from Bio import Seq
import regex as re
startP = re.compile('ATG')
nuc = get_seq(argv[1])
longest = (0,)
for m in startP.finditer(nuc, overlapped=True):
    if len(Seq.Seq(nuc)[m.start():].translate(to_stop=True)) > longest[0]:
        pro = Seq.Seq(nuc)[m.start():].translate(to_stop=True)
        longest = (len(pro), 
                   m.start(), 
                   str(pro),
                   nuc[m.start():m.start()+len(pro)*3+3])
print(longest)
