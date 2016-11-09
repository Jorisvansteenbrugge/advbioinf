

from sys import argv


def fibo(n, m):
    pairs = [1, 1]
    
    for i in range(2,m):
        f1 = pairs[i-1]
        f2 = pairs[i-2] 
        pairs.append((f1+f2))

    return pairs


if __name__ == "__main__":
    n = int(argv[1])
    m = int(argv[2])

    print(fibo(n, m))
