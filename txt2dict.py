#!/usr/bin/env python3
"""
    parseTxt()
    file = .txt, utf8.
    parseKeys = list of factor names. ex:'item_value'
    multiLine = a factor that contains multi line. the only one.

"""

import locale
ansicode = locale.getpreferredencoding()
#for each contry. ex: japanese to ansi txt, encoding='cp932'
def doubleOpen(txtFile):
    #hope ansi - 16 - 8 is best..
    try:
        with open(txtFile,'r',encoding=ansicode) as f:
            readList = f.readlines()
    except:
        readList = None
    if readList == None:
        try:
            with open(txtFile,'r',encoding='utf-16') as f:
                readList = f.readlines()#what if err while err??
        except:
            readList = None
    if readList == None:
        with open(txtFile,'r', encoding = 'utf-8' ) as f:
            readList = f.readlines()#what if err while err??

    return readList


def removeEnters( targetstr ):
    returnstr = ''  #''[0] error! use ''[-1:].
    for i in targetstr:
        if i == '\n':
            if returnstr[-2:] == '\n\n':
                continue#jump if  n + n.
        returnstr += i
    return returnstr


def parseTxt(txtFile, parseKeys, multiLine ):
    """
    dosent return ''
    file = .txt, utf8.
    parseKeys = list of factor names. ex:'item_value'
    multiLine = a factor that contains multi line. the only one.
    """
    #UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte


    #first n line check. if i in keys, dict[i].
    parseDict = {}
    readList = doubleOpen(txtFile)

    #caution for  index slicer.
    #if len(readList) >= len(parseKeys): # a[90] err, a[:90] not err.
    for i in readList[0:len(parseKeys)]:
        key = i[:i.find('=')].strip()
        value = i[i.find('=')+1:].strip()
        if key in parseKeys:
            parseDict[key] = value

    #if all keys match:
    if len(parseDict) == len(parseKeys):
        for i in readList[len(parseKeys) :]:
            parseDict[multiLine] += i

    if len(parseDict) != len(parseKeys):
        parseDict[multiLine] = ""
        for i in readList:#full str list
            parseDict[multiLine] += i

    #remove enters. how clever!
    parseDict[multiLine] = removeEnters( parseDict[multiLine] )

    return parseDict


def checkDict(parseDict):
    e=1
    for i in parseDict.keys():
        print( 'line',e, i, parseDict[i] )
        e+=1


from jsonio import *#includs json as well

def saveVarjson(parsedDict,jsonFile,varName='datas'):
    dump = json.dumps(parsedDict,ensure_ascii=False,indent = 4)
    with open(jsonFile,'w',encoding='utf-8') as f:
        f.write('var '+varName+' = ')
        f.write(dump)

if __name__ == '__main__':
    file= '크롤링결과버전0.7.txt'
    parseKeys = ['번호','제목','작성자','날짜','태그','본문']
    multiLine = '본문'

    #result = parseTxt(file,parseKeys,multiLine)
    #checkDict(result)
    #print('result',result)
    txtfile = input('txtfilename :')
    for i in parseTxt( txtfile, parseKeys, multiLine ).items():
        print(i)
    input('press to exit')
