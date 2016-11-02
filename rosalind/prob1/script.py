from sys import argv




def getHypoSquare(a,b):
	return a**2+b**2


def getAB(fileName):
	with open(fileName) as infile:
		a, b = infile.readline().strip().split()
		return int(a), int(b)


if __name__ == "__main__":
	fileName = argv[1]
	a, b = getAB(fileName)
	print(getHypoSquare(a,b))
