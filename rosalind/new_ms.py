from sys import argv

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

def parseFile(in_file): 
    with open(in_file) as in_file: 
        n = in_file.readline().strip() 
        a = map(int, in_file.readline().strip().split()) 
 
    return a 



array = parseFile(argv[1])
mergesort(array)
print(count)
