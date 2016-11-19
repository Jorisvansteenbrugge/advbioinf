from sys import argv

def parseFile(file_name):
    with open(file_name) as in_file:
        arrays = []
        in_file.readline() #skip
        arrays = [line.strip().split() for line in in_file]
    return arrays



def get2Sum(array):
    for val in array:
        if "-"+val in array:
            print val

arrays = parseFile(argv[1])
get2Sum(arrays[1])
