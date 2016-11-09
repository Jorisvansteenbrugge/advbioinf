
from __future__ import division
from sys import argv



if __name__ == "__main__":
    k = int(argv[1])
    m = int(argv[2])
    n = int(argv[3])

    total = k+m+n

    prob = ((k*k - k) + 2*(k*m) + 2*(k*n) + (.75*(m*m - m)) + 2*(.5*m*n))/((k + m + n)*(k + m + n -1))
