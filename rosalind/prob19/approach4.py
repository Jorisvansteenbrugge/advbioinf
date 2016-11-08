import itertools as it
from sys import argv

def getSequences(inFile):
        """Return dictionary of {label:dna_seq}
        lines: list of lines in FASTA format
        """
        seqs = []
        seq = ""
        for line in inFile:
                if line.startswith('>'):
                        if seq != "":
                                seqs.append(seq)
                                seq = ""
                else:
                        seq  += line.strip()
        seqs.append(seq)
        return seqs




SEQUENCES = getSequences(open(argv[1]))


from collections import defaultdict

def dykSuperstring(originalSeqs):
  paths = defaultdict(set)
  paths[0] =  { '' }
  while paths:
    minLength = min(paths.keys())
    while paths[minLength]:
      candidate = paths[minLength].pop()
      seqAdded = False
      for seq in originalSeqs:
        if seq in candidate:
          continue
        seqAdded = True
        for i in reversed(range(len(seq)+1)):
          if candidate.endswith(seq[:i]):
            newCandidate = candidate + seq[i:]
            paths[len(newCandidate)].add(newCandidate)
      if not seqAdded:  # nothing added, so all present?
        return candidate
    del paths[minLength]

print dykSuperstring(getSequences(open(argv[1])))
