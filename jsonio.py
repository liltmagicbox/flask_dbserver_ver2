'''
loadJson( jsonFile = 'datas.json')
saveJson(parsedDict,jsonFile)
'''
import json

def loadJson( jsonFile = 'datas.json'):
    with open( jsonFile,'r',encoding='utf-8') as f:
    a=f.read()
    b=json.loads(a)
    return b

def saveJson(parsedDict,jsonFile):
    dump = json.dumps(parsedDict,ensure_ascii=False,indent = 4)
    with open(jsonFile,'w',encoding='utf-8') as f:
    f.write(dump)    
