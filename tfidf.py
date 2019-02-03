# Pythonic way of implementing TF-IDF
# TF - Term Frequency
# IDF - Inverse Document Frequency
# TF-IDF - TF*IDF

def computeTF(wordDict, bow):
    """
        wordDict - word dictionary
        bow - bag of words
    """
    tfDict = {}
    # Calculating total number of words
    bowCount = len(bow)
    for word, count in wordDict.items():
        # count corresponds to occurence of the word in the Doc
        tfDict[word] = count/float(bowCount)
    return tfDict

def computeIDF(docList):
    """
        docList -  list of all the documents, basically a dictionary of words
    """
    import math
    idfDict = {}
    # total number of documents
    N = len(docList)
    # initializing the count of a word in all docs to zero
    idfDict = dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            # if the word exists in document, incrementing its count
            if val > 0:
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N/float(val))
    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf