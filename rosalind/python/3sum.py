from sys import argv
from itertools import combinations

def parseFile(file):
    with open(file) as in_file:
        arrays = []
        in_file.readline()
        for line in in_file:
            arrays.append(map(int, line.strip().split()))

    return arrays




def combi(array):
    for i in combinations(array, 3):
        if sum(i) == 0:
            idxs = [array.index(x)+1 for x in i]
            return " ".join(sorted(map(str, idxs)))
        
    return str(-1)



arrays = parseFile(argv[1])

index = map(combi, arrays)

print("\n".join(index))
