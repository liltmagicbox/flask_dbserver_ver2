'''
loadJson( jsonFile = 'datas.json')
saveJson(parsedDict,jsonFile)
'''
import json

def loadJson( jsonFile = 'datas.json'):
    f=open( jsonFile,'r',encoding='utf-8')
    a=f.read()
    f.close()
    b=json.loads(a)
    return b

def saveJson(parsedDict,jsonFile):
    dump = json.dumps(parsedDict,ensure_ascii=False,indent = 4)
    f=open(jsonFile,'w',encoding='utf-8')
    f.write(dump)
    f.close()
