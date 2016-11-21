from sys import argv


def parseFile(in_file): 
    with open(in_file) as in_file: 
        n = in_file.readline().strip() 
        a = map(int, in_file.readline().strip().split()) 
 
    return a 


def merge_sort(m):
    if len(m) <=1:
        return m

    half = len(m) / 2
    left = m[0:half]
    right = m[half:]

    #recursion
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        
    #Either left or right could have elements left

    while len(left) > 0:
        result.append(left.pop(0))

    while len(right) > 0:
        result.append(right.pop(0))

    return result


array = parseFile(argv[1])
print(" ".join(map(str, merge_sort(array))))
