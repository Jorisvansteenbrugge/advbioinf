from Bio import Entrez
from Bio import SeqIO

Entrez.email = "jorisvansteenbrugge@hotmail.com"
handle = Entrez.efetch(db="nucleotide", id=["NM_001159758", "JQ762396", "JF927165", "NM_001197168", "JX308819", "NM_001003102", "JQ712981", "JX475045", "JQ290344", "JX428803"], rettype="fasta")
records = SeqIO.parse(handle, "fasta")

dic = {}
for rec in records:
    dic[rec.seq] = rec.description

idx = dic.keys()
idx = sorted(idx, key = lambda x: len(x))


print [len(x) for x in idx]
print(">{}\n{}".format(dic[idx[0]],idx[0]))

