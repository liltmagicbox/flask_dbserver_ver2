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

#-----------------------fluid set
# set and even update. it has dual..act.
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

        dictlist = ['캐릭터태그','유저태그','댓글','요청']
        for i in dictlist:
            if fluid[no].get(i) == None:
                fluid[no][i] = {}

        # datelist = ['최근태그','최근댓글','최근요청']# 유저태그 rec.
        # for i in datelist:
        #     if fluid[no].get(i) == None:
        #         fluid[no][i] = '0'
        #use instead:  fluid[no][key][max(fluid[no][key])].date

        return True
    except Exception as e:
        print(e)
        return False

def fluiddel(key):
    '''
    deletes key-value in fluid.
    '''
    try:
        key = str(key)
        for no in fluid:
            if fluid[no].get(key) != None :
                del fluid[no][key]
    except Exception as e:
        print(e)
        return False

#remain
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



def isonlyone(no,key,text):
    if len(fluid[no][key])==0:
        return 'onlyone'
    for i in fluid[no][key].values():
        if i['text'] == text:
            ermsg = 'fail add {} {} ,already in {}'.format(key,text,no)
            raise Exception(ermsg)

onlyonelist = ['캐릭터태그','유저태그']
def addtext(user,no,key,text):
    try:
        whatdid='addtext'
        strcheck(user,no,key,text)
        time = datestr()

        if key in onlyonelist:
            isonlyone(no,key,text)#err if not only one.fine.

        if len( fluid[no][key] ) ==0:
            idx = '001'
        else:
            #klist = list( fluid[no][key].keys() )
            #intlist = list(map( int ,klist))
            #idx = max(intlist)+1
            stridx = str( int(max( fluid[no][key] ))+1 )
            buff = 3-len( stridx )#'999' max idx.
            idx = '0'*buff + stridx
        fluid[no][key][idx] = { 'user':user, 'text':text, 'time':time, 'see':'all'}
        log(time,whatdid,user,no,key,text,idx)
        return True
    except Exception as e:
        exc_info = sys.exc_info()#below except.
        print(exc_info[1],':at line',exc_info[2].tb_lineno,)
        #print(e)
        return False

#use only for char.tag. not usertag.
def cleartext(user,no,key):
    try:
        whatdid='retext'
        strcheck(user,no,key)
        time = datestr()
        fluid[no][key]={}
        log(time,whatdid,user,no,key)
        return True
    except Exception as e:
        print(e)
        return False

#we believe idx shall be ..fine.
def subtext(user,no,key,idx):
    try:
        whatdid='subidx'
        strcheck(user,no,key,idx)
        time = datestr()
        del fluid[no][key][idx] # we didn't if is,del. since ..for true.
        log(time,whatdid,user,no,key,idx)
        return True
    except Exception as e:
        print(e)
        return False


import sys

'''
https://brownbears.tistory.com/356
https://spoqa.github.io/2019/02/15/python-timezone.html
'''
import datetime

tzinfo=datetime.timezone(datetime.timedelta(seconds=32400))
def datestr():
    now = datetime.datetime.now()
    now=now.astimezone(tzinfo)
    return now.strftime("%Y.%m.%d %H:%M:%S")
    #believe 09 < 11.. and 09 not 9.

def strcheck(*inputlist):
    for text in inputlist:
        if not type(text)==type('s'):
            ermsg = 'input {} is not str'.format(text)
            raise Exception(ermsg)

#-----------------------backup feature
from jsonio import *
'''
loadJson( jsonFile = 'datas.json')
saveJson(parsedDict,jsonFile)
'''

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



if __name__ == "__main__":
   #fluid={}
   #logue=[]
   #print( 'fluidset(id)' )
   print( 'fluid run as main' )
