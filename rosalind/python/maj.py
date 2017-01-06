from sys import argv

def parseFile(file_name):
    arrays = []
    with open(file_name) as in_file:
        k, n = in_file.readline().strip().split()
        for line in in_file:
            arrays.append(line.strip().split())

    return arrays




def countElements(array):
    dic = {}
    for val in array:
        if val in dic.keys():
            dic[val] += 1
        else:
            dic[val] = 1
    return dic

def getMajorityElement(array):
    dic = countElements(array)
    
    major = max(dic.items(), key= lambda x : x[1])

    if major[1] > (len(array) / 2):
        return str(major[0])
    else:
        return str(-1)




arrays = parseFile(argv[1])

result = map(getMajorityElement, arrays)
print(" ".join(result))    
