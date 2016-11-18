#!/usr/bin/env python
from sys import argv

def parseFile(fileName):
    nodes = []
    dic = {}
    with open(fileName) as in_file:
        for line in in_file:
            line = line.strip().split()
            nodes += line
            if line[0] in dic.keys():
                dic[line[0]].append(line[1])
            else:
                dic[line[0]] = [line[1]]
            
    return dic, sorted(list(set(nodes)))


if __name__ == "__main__":
    dic, nodes = parseFile(argv[1])

    for node in nodes:
        count = 0
        if node in dic.keys():
            count += 1

        for x in dic.values():
            if node in x:
                count += 1

        if count > 1:
            print(count)

