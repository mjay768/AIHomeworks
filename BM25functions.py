import math
import pandas as pd

N = 0
L = 0
IDF = 0
k = 1.2
b = 0.75
def getLength(documentID):
    N = len(documentID)
    return N

def getAvgLength(documentID,documentL):
    N = len(documentID)
    L = sum(documentL) / N
    return L

def getIDF(DF,N):
    IDF = math.log((N - DF + 0.5) / (DF + 0.5))
    return IDF

def getBM25Score(IDF,TF,d,L):
    numerator = TF * (k + 1)
    denominator = TF + k * (1 - b + b * (d / L))
    bm = IDF * (numerator / denominator)
    return bm;

def rankScores(BM):
    arr = pd.array(BM)
    temp = arr.argsort()
    ranks = temp.argsort()
    return ranks