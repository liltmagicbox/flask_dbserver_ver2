#!/usr/bin/env python3
"""
    parseTxt()
    file = .txt, utf8.
    parseKeys = list of factor names. ex:'item_value'
    multiLine = a factor that contains multi line. the only one.

"""
def parseTxt(txtFile, parseKeys, multiLine ):
    """
    file = .txt, utf8.
    parseKeys = list of factor names. ex:'item_value'
    multiLine = a factor that contains multi line. the only one.
    """
    f = open(txtFile,'r',encoding='utf-8')
    readList = f.readlines()
    f.close()

    parseDict = {}

    for i in readList:


        key = i[:i.find('=')].strip()
        value = i[i.find('=')+1:].strip()
        #print(key)
        if key in parseKeys:
            parseDict[key] = value
        else:
            if multiLine in parseDict.keys():
                if parseDict[multiLine][-1] == '\n':
                    if i == '\n':
                        continue
                parseDict[multiLine] += i # assume not-in-list are multiline body.

    return parseDict


def checkDict(parseDict):
    e=1
    for i in parseDict.keys():
        print( 'line',e, i, parseDict[i] )
        e+=1


from jsonio import *#includs json as well

def saveVarjson(parsedDict,jsonFile,varName='datas'):
    dump = json.dumps(parsedDict,ensure_ascii=False,indent = 4)
    f=open(jsonFile,'w',encoding='utf-8')
    f.write('var '+varName+' = ')
    f.write(dump)
    f.close()

if __name__ == '__main__':
    file= '크롤링결과버전0.7.txt'
    parseKeys = ['번호','제목','작성자','날짜','태그','본문']
    multiLine = '본문'
    result = parseTxt(file,parseKeys,multiLine)
    #checkDict(result)
    print('result',result)
