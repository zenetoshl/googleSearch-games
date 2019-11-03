import collections
from .textTreatment import *
from .article import *

def treatSearch(search):
    text = search.lower().split(' ')
    text = removePonctuation(text)
    text = removeStopWords(text)
    text = stemming(text)
    return text

def sortDict(dic):
    dicR = {}
    dicT = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
    dicR = sorted_dict = collections.OrderedDict(dicT)
    return dicR

def findFile(name):
    for dicName in article.localDic:
        if name == dicName:
            return dicName

    return null

def searchOR(words):
    global tfidfs
    result = {}
    relevance = {}
    sortedResult = []
    text = treatSearch(words)
    for word in text:
        for f in tfidfs:
            if word in tfidfs[f]:
                if f not in result:
                    result[f] = tfidfs[f]
                    relevance[f] = 0
    for word in text:
        for r in result:
            if word in result[r]:
                relevance[r] += result[r][word]
    relevance = sortDict(relevance)
    for w in relevance:
        for r in result:
            if r == w:
                sortedResult.append(r) #TODO: retornar dicionario
    arrayDict = []
    path = os.getcwd() 
    txtpath = path + '/' + 'texts'
    os.chdir(txtpath)
    fileNames = os.listdir()
    for r in sortedResult:
        for name in fileNames:
            if r == name.replace('.txt', '').replace('_', ' '):
                arrayDict.append({'titulo': r, 'texto': returnText(name)})
    os.chdir(path)
    print(arrayDict)
    return arrayDict
'''
def searchAND(words):
    results = []
    result = []
    sortedResult = []
    relevance = {}
    noOfWords = {}
    text = treatSearch(words)
    size = len(text)
    for word in text:
        result = []
        for f in article.localDic:
            if word in article.localDic[f]:
                result.append(f)
                relevance[f.name] = 0
                if f.name not in noOfWords:
                    noOfWords[f.name] = 1
                else:
                    noOfWords[f.name] += 1
        results.append(result)
    for k in noOfWords:
        if noOfWords[k] == size:
            f = findFile(k)
            if f not in result:
                result.append()
    for word in text:
        for r in result:
            if word in r.tfidfDict:
                relevance[r.name] += r.tfidfDict[word]
    relevance = sortDict(relevance)
    for w in relevance:
        for r in result:
            if r.name == w:
                sortedResult.append(r)
    return sortedResult
'''