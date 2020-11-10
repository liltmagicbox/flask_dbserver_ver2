'''
from fluiddb import *
for global use fluid,logue.. became fluiddb.fluid

fluidset(no)
noexist(no)

datestr()

itername(head,fullname)
backupfluid()
backuplogue()

addn(user,no,key) keys=[조,추,좋]
addtext(user,no,key,text) keys=[캐릭터태그,유저태그,댓글]

#structure
fluid[no][textkey]={ '1':{}, '2':{}, } #all str rule
#del
del fluid[no][key][item][idx]
#len
len(fluid[133][태그]) #is only for num.fine.
#search
for idx in fluid[133][태그]:
    tag = fluid[133][태그][idx][text]#1

    if fluid[133][태그][idx][see]==3:
        tag=fluid[133][태그][idx][text]#2
    taglist.append(tag)

'''




fluid={}
logue=[]
print('fluiddb loading.. use','fluidset( id )' )

def fluidset(no):
    no = str(no)
    try:
        if fluid.get(no) == None:
            fluid[no]={}
            #raise Exception(' no already was. in fluid')
        intlist = ['숨','조','추','좋']
        for i in intlist:
            if fluid[no].get(i) == None:
                fluid[no][i] = 0
        textlist = ['캐릭터태그','유저태그','댓글','요청']
        for i in textlist:
            if fluid[no].get(i) == None:
                fluid[no][i] = {}
        return True
    except Exception as e:
        print(e)
        return False

def fluiddel(key):
    try:
        key = str(key)
        for no in fluid:
            if fluid[no].get(key) != None :
                del fluid[no][key]
    except Exception as e:
        print(e)
        return False


#oldman. ithink it may not used.
def noexist(no):
    #if str(no) in fluid.keys():
    print('the ghost appears.!')
    if fluid.get(str(no)) != None:
        return True
    else:
        return False

#not use, since it left no log.
def fluidadd(key,value):
    key = str(key)
    for k in fluid:
        #if not key in fluid[k].keys():
        if fluid[k].get(key) == None :
            fluid[k][key] = value

#----------too many! we change ver 2.0.seeya.



from jsonio import *
'''
loadJson( jsonFile = 'datas.json')
saveJson(parsedDict,jsonFile)
'''

#need global use. if server in america..
import datetime
def datestr():
    now = datetime.datetime.now()
    return now.strftime("%Y.%m.%d %H:%M:%S")

import os
def itername(filename,ext):
    flist = os.listdir()
    no=0
    isok = "{}_backup{}.{}".format(filename,no,ext)
    while isok in flist:
        no+=1
        isok = "{}_backup{}.{}".format(filename,no,ext)
    print('backup no:',no)
    return isok

def backupfluid():
    filename = itername('fluid','txt')
    saveJson(fluid,filename)

def backuplogue():
    filename = itername('logue','txt')
    saveJson(logue,filename)


def log( *loglist ):
    #logue.append( [time,whatdid,user,no,key,text] )
    logue.append( list(loglist) )

def strcheck(*inputlist):
    for text in inputlist:
        if not type(text)==type('s'):
            ermsg = 'input {} is not str'.format(text)
            raise Exception(ermsg)

#please dont strcheck in canaddtag..ha ha!
def isonlyone(no,key,text):
    if len(fluid[no][key])==0:
        return 'onlyone'
    for i in fluid[no][key].values():
        if i['text'] == text:
            ermsg = 'fail add {} {} ,already in {}'.format(key,text,no)
            raise Exception(ermsg)

#can only concatenate str (not "int") to str
#unsupported operand type(s) for +=: 'dict' and 'int'
['조','추','좋']
def addn(user,no,key):
    try:
        whatdid='addn'
        strcheck(user,no,key)
        time = datestr()
        fluid[no][key] += 1
        log(time,whatdid,user,no,key)
        return True
    except Exception as e:
        print(e)
        return False
def subn(user,no,key):
    try:
        whatdid='subn'
        strcheck(user,no,key)
        time = datestr()
        fluid[no][key]-=1
        log(time,whatdid,user,no,key)
        return True
    except Exception as e:
        print(e)
        return False

import sys

['캐릭터태그','유저태그','댓글','요청']
onlyonelist = ['캐릭터태그','유저태그','댓글','요청']
def addtext(user,no,key,text):
    try:
        whatdid='addtext'
        strcheck(user,no,key,text)
        time = datestr()
        if key in onlyonelist: isonlyone(no,key,text)

        klist = list( fluid[no][key].keys() )
        if len( klist )==0:
            idx=1 #idx starts 1,2,3..
        else:
            intlist = list(map( int ,klist))
            #print(intlist)
            idx =  max(intlist)+1 #max() arg is an empty sequence
            #max( fluiddb.fluid['10231527']['캐릭터태그'].keys() )+1 ERROR?
        idx=str(idx) # savejson found. it's not value, so should be str. gotit!
        fluid[no][key][idx] = { 'user':user, 'text':text, 'time':time, 'see':'all' }
        #no see, error when [see]=='hidden'
        log(time,whatdid,user,no,key,text)
        return True
    except Exception as e:
        exc_info = sys.exc_info()#below except.
        print(exc_info[1],':at line',exc_info[2].tb_lineno,)
        #print(e)
        return False

def retext(user,no,key):
    try:
        whatdid='retext'
        strcheck(user,no,key)
        time = datestr()
        del fluid[no][key]
        fluid[no][key]={}
        log(time,whatdid,user,no,key)
        return True
    except Exception as e:
        print(e)
        return False

#pickup delete.
def subtext(user,no,key,text):
    try:
        whatdid='subtext'
        strcheck(user,no,key,text)
        time = datestr()
        keys = fluid[no][key]
        for i in keys:
            if fluid[no][key][i]['text']==text:
                del fluid[no][key][i] #dictionary changed size during iteration
                log(time,whatdid,user,no,key,text)
                #return True#this accurs 1 shot out.
        return True
    except Exception as e:
        print(e)
        return False

# def subtext(user,no,key,idx):
#     try:
#         whatdid='subtext'
#         strcheck(no,key)#idx is int.
#         intcheck = idx*10
#         time = datestr()
#         del fluid[no][key][idx]
#         log(time,whatdid,user,no,key)
#         return True
#     except Exception as e:
#         print(e)
#         return False

if __name__ == "__main__":
   #fluid={}
   #logue=[]
   #print( 'fluidset(id)' )
   print( 'fluid run as main' )
