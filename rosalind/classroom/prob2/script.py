from sys import argv




def getNucString(fileName):
    a = 0
    c = 0
    g = 0
    t = 0
    with open(fileName) as infile:
        for line in infile:
            line = line.strip()
            counts = getCounts(line)
            a += counts[0]
            c += counts[1]
            g += counts[2]
            t += counts[3]
    return "{} {} {} {}".format(a,c,g,t)

def getCounts(nucString):
    ca = nucString.count("A")
    cc = nucString.count("C")
    cg = nucString.count("G")
    ct = nucString.count("T")

    return (ca,cc,cg,ct)
if __name__=="__main__":
    fileName = argv[1]
    nuc_string = getNucString(fileName)
    print nuc_string

