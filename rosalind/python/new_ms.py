from sys import argv

<<<<<<< HEAD
count = 0

def mergesort(array):
    global count
    count += 1
    # array is a list
    #base casee
    if len(array) <= 1:
        return array
    else:
        split = int(len(array)/2)
        #left and right will be sorted arrays
        left = mergesort(array[:split])
        right = mergesort(array[split:])

        sortedArray  = [0]*len(array)

        #sorted array "pointers"
        l = 0
        r = 0

        #merge routine
        for i in range(len(array)):

            try:
                #Fails if l or r excede the length of the array
                if left[l] < right[r]:
                    sortedArray[i] = left[l]
                    l = l+1
                else:
                    sortedArray[i] = right[r]
                    r = r+1
            except:
                if r < len(right):
                    #sortedArray[i] = right[r]
                    #r = r+1
                    for j in range(len(array) - r-l):
                        sortedArray[i+j] = right[r+j]
                    break
                else:
                    #sortedArray[i] = left[l]
                    #l = l+1
                    for j in range( len(array) - r-l):
                        sortedArray[i+j] = left[l+j]
                    break

        return sortedArray
=======
>>>>>>> ce036ca8d145d36aa58673676a9ff1dde7c7890a

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
<<<<<<< HEAD
mergesort(array)
print(count)
=======
print(" ".join(map(str, merge_sort(array))))
>>>>>>> ce036ca8d145d36aa58673676a9ff1dde7c7890a
