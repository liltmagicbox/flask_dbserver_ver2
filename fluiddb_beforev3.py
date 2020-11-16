'''
chrome can bear 40MB. fine.
dict db system designed handle 100000 of articles.

sortlist of 100000 is 4MB
articles of 10000 is 4MB
novels of 1000 is 50MB

articles 400B for 1?. yeah. since having full img list.

articles,
300 for 150KB.
200 100, 2000 for 1MB..
10000 for 5MB,,
100000 for 50MB..!

novels,
100 of novel, 10MB...
45MB for 2000 of small novels.
yeah, we can't directly send it. it's for fetch..
100KB for major novel. 1MB to full book.
100 book, 100MB. bear it... no we cant..
NO! we can't see a book in the imgbox!

-------------
{제목: 어쩌구저쩌구최대20자는넘겠나,
날짜: 20202033,
번호: _2332302200,
imgs=6,
thumbs=6,
gifs=[3,4]}
썸넬은 이후 확장용인데, 보내는실시간생성이니 이후 추가하자;?

new articles 100000 for 10MB.fine.
imgs: id_1 .x.
-------------

for 1000,000 of int list/array

py sort 0.05s
py int() sort 0.5s

JS sort 0.5s.
JS parseint sort 0.5s.
js sort seems already attached func, 100 0000 /0.5s.

py sort  2000 0000/1s.
py for in a+=1 400 0000/1s
JS 1s for(i=0;i<300000000;i++){true}



'''
datas={}
fluid={}
logue=[]
print('fluiddb loading.. use','fluidset( id )' )

#-----------------------fluid set
# set and even update. it can dual..job.
def fluidset(id):
    id = str(id)# for int easy use
    try:
        if fluid.get(id) == None:
            fluid[id]={}
            #raise Exception(' id already was. in fluid')
        intlist = ['숨','조','추','좋']
        for i in intlist:
            if fluid[id].get(i) == None:
                fluid[id][i] = 0

        dictlist = ['캐릭터태그','유저태그','댓글','요청']
        for i in dictlist:
            if fluid[id].get(i) == None:
                fluid[id][i] = {}

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
    deletes all values in fluid.
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


#was for tag. byebye.
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
