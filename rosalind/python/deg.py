#!/usr/bin/env python
from sys import argv

def parseFile(fileName):
    nodes = {}
    with open(fileName) as in_file:
        header = in_file.readline()
        for line in in_file:
            line = line.strip().split()
            

            try:
                nodes[line[0]].append(line[1])
            except:
                nodes[line[0]] = [line[1]]

            try:
                nodes[line[1]].append(line[0])
            except:
                nodes[line[1]] = [line[0]]

    return nodes


if __name__ == "__main__":
    nodes = parseFile(argv[1])



    out = []
    for key in sorted(nodes.keys()):
        vals = list(set(nodes[key]))

        out.append(len(vals))

    print(len(nodes.keys()))
    print(str(sum([len(x) for x in nodes.values()])))
    #print " ".join(map(str, out))
         
