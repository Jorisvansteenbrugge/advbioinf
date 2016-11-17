#!/urs/bin/env python

from sys import argv

if __name__ == "__main__":
    ints = map(int, argv[1:])

    freq = ints[0] + ints[1] + ints[2] + 0.75*ints[3] + 0.5*ints[4] 

    print(freq * 2) 
