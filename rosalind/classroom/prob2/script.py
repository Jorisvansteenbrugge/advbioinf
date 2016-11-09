from sys import argv




def getNucString(fileName):
	with open(fileName) as infile:
		return infile.readline().strip()

def getCounts(nucString):
	ca = str(nucString.count("A"))
	cc = str(nucString.count("C"))
	cg = str(nucString.count("G"))
	ct = str(nucString.count("T"))

	print("{} {} {} {}".format(ca,cc,cg,ct))
if __name__=="__main__":
	fileName = argv[1]
	nucString = getNucString(fileName)
	getCounts(nucString)

