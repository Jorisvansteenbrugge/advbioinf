#!/usr/bin/env python

from itertools import permutations
from sys import argv

def permute(num):
    array = [int(x) for x in range(1, num+1)]
    permutated = []
    first_permute = list(permutations(array, num))
    for val in first_permute:
        permutated.append(val)
        permutated.append(tuple(map(lambda x: x*-1, val)))
        for i in range(1, len(val)):
            second_permute = permutations(val,i)
            for sec_val in second_permute:
                adjustable_val = list(val)
                for sep_val in sec_val:
                    idx = val.index(sep_val)
                    adjustable_val[idx] = val[idx] * -1
                permutated.append(adjustable_val)                    
               
    return permutated
           

if __name__ == "__main__":
    sample = int(argv[1])
    permutated = permute(sample)


    import itertools
    permutated.sort()
    new_list = list(permutated for permutated,_ in itertools.groupby(permutated)) 

    print(len(new_list))
    for val in new_list:
        print(" ".join(map(str, val)))


