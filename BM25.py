import BM25functions as bf



if __name__ == '__main__':
    documentID = []
    documentL = []
    freqOfWord1 = []
    freqOfWord2 = []
    DF1 = 0
    DF2 = 0
    BM25Scores = []
    with open("data.txt") as f:
        for line in f:
            data = line.split()
            documentID.append(int(data[0]))
            documentL.append(int(data[1]))
            freqOfWord1.append(int(data[2]))
            freqOfWord2.append(int(data[3]))
        N = bf.getLength(documentID)
        L = bf.getAvgLength(documentID,documentL)
        print("N -> ",N)
        print("Avg Length -> ",L)
        for i in range(len(documentID)):
            if freqOfWord1[i] > 0:
                DF1 = DF1 + 1
            if freqOfWord2[i] > 0:
                DF2 = DF2 + 1
        w1IDF = bf.getIDF(DF1,N)
        w2IDF = bf.getIDF(DF2,N)
        print("IDF -> ",w1IDF)
        print("IDF2 -> ",w2IDF)

    for i in range(len(documentID)):
        print("Document #",i+1,":","Term Frequency 1 = ",freqOfWord1[i], "Term Frequency 2 = ",freqOfWord2[i])
        BM25Scores.append(bf.getBM25Score(w1IDF,freqOfWord1[i],documentL[i],L) + bf.getBM25Score(w2IDF,freqOfWord2[i],documentL[i],L))
        print("BM25 ",BM25Scores[i])
    ranks = []
    ranks = bf.rankScores(BM25Scores)
    print("Ranking ->",ranks)





