import numpy
import scipy
import scipy.cluster.hierarchy as sch
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from sys import argv

def fileToDict(file_name):
    with open(file_name) as in_file:
        dic = {}
        header = in_file.readline().strip().split(",")
        for idx in header:
            header[idx]  = "\"" + header[idx] + "\""
            dic[header[idx]] = []

        for line in in_file:
            line = line.strip().split(",")
            for idx in range(len(line)):
                dic[header[idx]].append(line[idx])
            
    return dic
            




if __name__ == "__main__":
    fileDic = fileToDict(argv[1])
    df = pd.DataFrame(fileDic)

    df = df.transpose()
    distances = sch.distance.pdist(df, metric="euclidean")
    print distances.shape
