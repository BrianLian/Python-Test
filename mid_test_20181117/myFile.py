import csv
import os

def readFile(fieldName, fileName):
    try:
        lst = []
        f = open(fileName, "r", encoding='utf-8')
        for row in csv.reader(f):
            lst.append(dict(zip(fieldName, row)))
        f.close()
        return lst
    except:
        print("讀取失敗")

def writeFile(fileName, writeMsg):
    try:
        f = open(fileName, "a", encoding='utf-8')
        f.write(writeMsg)
        f.close()
    except:
        print("寫入失敗")

def readFolder(folder,findType):
    lst = []
    for f in os.listdir(folder):
        if (f.endswith(findType)):
            lst.append(f)
    return lst
