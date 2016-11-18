
from sys import argv




fibo = [1,1]
n = int(argv[1])


for i in range(2, n):
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[-1])
