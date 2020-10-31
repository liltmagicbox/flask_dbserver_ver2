import json
def saveJson(parsedDict,jsonFile):
    dump = json.dumps(parsedDict,ensure_ascii=False,indent = 4)
    f=open(jsonFile,'w',encoding='utf-8')
    f.write(dump)
    f.close()
#a=[1,2,3,'ha','11']

def loadJson( filename = 'datas.json'):
    f=open( filename,'r',encoding='utf-8')
    a=f.read()
    f.close()
    b=json.loads(a)
    return b

def addn(user,no,key):
    if not str(fluid[no][key]).isdigit():
        return False
    fluid[no][key]+=1    
    logue.append( "addn('{}','{}','{}')".format(user,no,key) )
    return True

def subn(user,no,key):
    if not str(fluid[no][key]).isdigit():
        return False
    fluid[no][key]-=1
    logue.append( "subn('{}','{}','{}')".format(user,no,key) )
    return True

#logue=[]
#fluid={}
def test(no='11',key='추수',user='하나요'):
    fluid[no]={}
    fluid[no][key]=1
    addn(user,no,key)
    addn(user,no,key)
    addn(user,no,key)
    print(fluid[no][key])
    print(logue)

if __name__ == "__main__":
    logue=[]
    fluid={}
    test()
    #saveJson( logue ,'haha.t')
    ll=loadJson( 'haha.t')
    print(ll)
    print(fluid)
    
    for i in ll:
        exec(i)
    for i in ll:
        exec(i)

    for i in ll:
        exec(i.replace('add','sub'))
    print(fluid)
    for f in logue:
        if f.split("'")[1] == '마키':
            print(25252)

def rollbackN(user):
    for f in logue:
        if f.split("'")[1] == user:
            if f.split("'")[0]=='add':
                exec(i.replace('add','sub'))
            else:
                exec(i.replace('sub','add'))

#-------------------------

#additional jsons.

# ver1 fluid[no][key][user]= time,text
# ver2 fluid[no][key].append( user={ 시간:time , 내용:text} )
# ver3 fluid[no][key][시간] = {유저=user, 내용:text}
# finally [댓글].append( {작성자:user, '시간': 오전 6:43 2020-10-29, '내용':'235236236236'} )

#..exported to fluiddb
