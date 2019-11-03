import pyrebase
import os
from .textTreatment import *
config = {
  "apiKey": "AIzaSyAX7wN_9jX64GHyuuU4nLUSADFBxtNFtf8",
  "authDomain": "games-e547f.firebaseapp.com",
  "databaseURL": "https://games-e547f.firebaseio.com/",
  "storageBucket": "games-e547f.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("zenetoshl@outlook.com", "123456")
db = firebase.database()

dic = {}
localDic = {}
idf = db.child('idf').get().val()
tfs = db.child('tfs').get().val()
tfidfs = db.child('tfidfs').get().val()

def visitOneFile(name):
    nameTreated = name.replace('.txt', '').replace('_', ' ')
    localDic[nameTreated] = treatText(name)


def newText(text):
    path = os.getcwd() 
    txtpath = path + '/' + 'texts'
    os.chdir(txtpath)
    title = text.partition('\n')[0]
    f = open(title + '.txt','w')
    f.write(text)
    f.close()
    visitOneFile(title+ '.txt')
    os.chdir(path)

def fileLen(dic):
    lenght = 0
    for w in dic:
        lenght += dic[w]
    return lenght


def createDic(docList):
    dicti = {}
    for a in docList:
        for word, val in docList[a].items():
            if word not in dic:
                dicti[word] = 0 
    return dicti

def tfComputer(words):
    tfDict = {}
    countW = fileLen(words)
    for w, count in words.items():
        tfDict[w] = count/float(countW)
    return tfDict
    

def idfComputer(docList):
    import math
    idfDict = {}
    N = len(docList)
    idfDict = createDic(docList)
    for a in docList:
        for word, val in docList[a].items():
            if val > 0:
                if word in idfDict:
                    idfDict[word] += 1
                else:
                    idfDict[word] = 1
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N/float(val))
    return idfDict

def tfidfComputer(tfDict, idfDict):
    tfidfDict = {}
    for word, val in tfDict.items():
        tfidfDict[word] = val * idfDict[word]
    return tfidfDict

def loadDict():
    dicts = db.child('global').child('indexes').get()
    dic = dicts.val()

def loadLocalDict():
    allDicts = db.child('individual').get()
    allDicts = allDicts.val()
    for dic in allDicts:
        localDic[dic] = allDicts[dic]

def loadTfs():
    tf = db.child('tfs').get().val()

def loadIdf():
    idf = db.child('idf').get().val()

def loadTfidfs():
    return db.child('tfidfs').get().val()

def saveDict():
    print(dic)
    db.child('global').child('indexes').set(dic)

def saveLocalDict(name, dic):
    db.child('individual').child(name).set(dic)

def saveTfs(name, tf):
    db.child('tfs').child(name).set(tf)

def saveIdf(idf):
    db.child('idf').set(idf)

def saveTfIdfs(name, tfidf):
    db.child('tfidfs').child(name).set(tfidf)

def tfidfHandler():
    idf = idfComputer(localDic)
    saveIdf(idf)
    tfs = {}
    tfidfs = {}
    for a in localDic:
        tf = tfComputer(localDic[a])
        tfs[a] = tf
        saveTfs(a, tf)
        tfidf = tfidfComputer(tf,idf)
        tfidfs[a] = tfidf
        saveTfIdfs(a, tfidf)
        saveLocalDict(a, localDic[a])


def readArchive(fileName):
    allWords = []
    with open(fileName, 'r') as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            allWords = allWords + words
    return allWords

def returnText(filename):
    with open(filename, 'r') as f:
        data = f.read()
        return data

def toDicLocal(words):
    dicti = {}
    for word in words:
        if (word in dicti):
            dicti[word] += 1
        else:
            dicti[word] = 1
    return dicti


def toDicGlobal(words):
    global dic
    for word in words:
        if (word in dic):
            dic[word] += 1
        else:
            dic[word] = 1

def treatText(fileName):
    allWords = readArchive(fileName)
    allWords = removePonctuation(allWords)
    allWords = stemming(allWords)
    toDicGlobal(allWords)
    dicti = toDicLocal(allWords)
    return dicti

def visitAllFiles():
    global localDic
    localDic = {}
    fileNames = os.listdir()
    print(fileNames)
    for name in fileNames:
        nameTreated = name.replace('.txt', '').replace('_', ' ')
        localDic[nameTreated] = treatText(name)


def initFiles():
    from .article import saveDict, tfidfHandler
    path = os.getcwd() 
    txtpath = path + '/' + 'texts'
    os.chdir(txtpath)
    print(path)
    visitAllFiles()
    saveDict()
    tfidfHandler()
    os.chdir(path)

    

 