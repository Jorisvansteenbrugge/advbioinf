from sys import argv
import sys
sys.setrecursionlimit(20000)
def parseFile(in_file):
    with open(in_file) as in_file:
        n = in_file.readline().strip()
        a = map(int, in_file.readline().strip().split())
        m = in_file.readline().strip()    
        b = map(int, in_file.readline().strip().split())

    return n, a, m, b



def compose(a,b,c = []):
    while len(a) != 0 or len(b) != 0:
        if len(a) != 0 and len(b) != 0:
            a_first = a[0]
            b_first = b[0]

            if a_first < b_first:
                c.append(a.pop(0))
            elif b_first < a_first:
                c.append(b.pop(0))
            else: #equal size
                c += [a.pop(0), b.pop(0)]
        elif len(a) != 0 and len(b) == 0:
            c.append(a.pop(0))
        
        else:
            c.append(b.pop(0))

    return c 

    
n,a,m,b = parseFile(argv[1])


c = compose(a,b)
print(" ".join(map(str, c)))

