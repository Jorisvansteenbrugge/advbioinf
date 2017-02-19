from sys import argv
from Bio import Entrez

Entrez.email = "jorisvansteenbrugge@hotmail.com"

TERM = '(Anthoxanthum[All Fields]) AND ("2003/07/25"[PDAT] : "2005/12/27"[PDAT])'

handle = Entrez.esearch(db="nucleotide", 
    term = TERM)

record = Entrez.read(handle)
print(record["Count"])
