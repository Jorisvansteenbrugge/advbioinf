

from sys import argv


def fibo(n, m):
    pairs = [1, 1]
    death_pairs = []
    for i in range(2, n):
        f1 = pairs[i-1]
        f2 = pairs[i-2] 
        pairs.append((f1+f2))

    for i in range( n):
        if i-3 >= 0:
            death = sum(pairs[0:i-m+1])
            death_pairs.append(pairs[i]-death)
        else:
            death_pairs.append(pairs[i])

    

    return death_pairs


if __name__ == "__main__":
    n = int(argv[1])
    m = int(argv[2])

    print(fibo(n, m))
