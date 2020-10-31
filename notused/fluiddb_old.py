'''
from fluiddb import *
for global use fluid,logue.. became fluiddb.fluid

datestr()
fluidset(no)
noexist(no)
itername(head,fullname)
backupfluid()
backuplogue()

addn(user,no,'조')
subn(user,no,'조')
addn(user,no,'추')
subn(user,no,'추')
addn(user,no,'좋')
subn(user,no,'좋')
addtagm(user,no,text)
subtagm(user,no,text)
addtag(user,no,text)
subtag(user,no,text)
addcomm(user,no,text)
subcomm(user,no,text)
'''

fluid={}
logue=[]
print('fluiddb loading.. use','fluidset( strid )' )

#from datetime import datetime
#str(datetime.now())[:19]
#'2020-10-29 21:25:57'
#https://docs.microsoft.com/ko-kr/dotnet/api/system.datetime.tostring?view=netcore-3.1
##def gettime():
##        #return str(datetime.now())[:19].replace('-',' ').replace(':',' ').split(' ')
##        #['2020', '10', '29', '21', '22', '44']
##        #timelist = str(datetime.now())[:19].replace('-',' ').replace(':',' ').split(' ')
##        return str(datetime.now())[:-7]# fixed well before happen.. 11-11 vs 1-1.got.

#import time
#int(time.time()) as timeid.
# def timestr():
#     rawsec = int(time.time())#can used as id.
#     tk = time.localtime( rawsec )#gmtime for gmt
#     timestr=''
#     tx=['년','월','일','시','분','초']
#     for i in range(6):
#         timestr+= str(tk[i])+tx[i]
#     return timestr

import datetime
def datestr():
    now = datetime.datetime.now()
    return now.strftime(g"%Y.%m.%d %H:%M:%S")


from jsonio import *
'''
loadJson( jsonFile = 'datas.json')
saveJson(parsedDict,jsonFile)
'''

#sub을 그거로바꿀까싶지만,규칙에의해고정됨.ㅇㅋ.

#for no in fluid:#no shall be int, not str.-??? id is not int. ok.
# since id in datas is parsed txt, id shall be str, not int.

#remember, no strint, not int.
def fluidset(no):
    no = str(no)
    try:
        #no + 'str'#if type(no) == type(1):
        if no in fluid.keys():
            raise Exception(' no already was. in fluid')
        fluid[no]={}
        # fluid[no]['조']=0
        # fluid[no]['좋']=0
        # fluid[no]['추']=0

        #fluid[no]['캐']=0
        #fluid[no]['태']=0#2 used sort.. for fast.
        #fluid[no]['댓']=0#2 used sort.. for fast.

        fluid[no]['조회']=[]
        fluid[no]['좋아요']=[]
        fluid[no]['추천']=[]
        fluid[no]['비추천']=[]

        fluid[no]['캐릭터태그']=[]
        fluid[no]['유저태그']=[]
        fluid[no]['댓글']=[]
        #fluid[no]['뮤슬람댓글']=[]
        #fluid[no]['뮤슬람태그']=[]
        fluid[no]['요청']=[]
        return True
    except Exception as e:
        print(e)
        return False
def fluidadd(key,value):
    for k in fluid:
        if not key in fluid[k].keys():
            fluid[k][key]=[value]
def noexist(no):
    if str(no) in fluid.keys():
        return True
    else:
        return False

['캐릭터태그','유저태그','댓글','요청',]
def addn(no,user,key,text=''):
    try:
        whatdid='addn'
        inputcheck(no,user,key,text)
        time = datestr()
        #canaddtag(no,text,key,text)
        fluid[no][key].append([user,text,time])
        log(whatdid,no,user,key,text,time)
        return True
    except Exception as e:
        print(e)
        return False

['캐릭터태그','유저태그','댓글','요청',]
def addtext(no,user,key,text):
    try:
        whatdid='addtext'
        inputcheck(no,user,key,text)
        time = datestr()
        canaddtag(no,text,key,text)
        fluid[no][key].append([user,text,time])
        log(whatdid,no,user,key,text,time)
        return True
    except Exception as e:
        print(e)
        return False


#addn input key is born here, so can trust.
def inputcheck(no,user,text):
    if not type(user)==type(no)==type(text)==type('s'):
        ermsg = 'input type error'
        raise Exception(ermsg)
#please dont inputcheck in canaddtag..ha ha!
def canadd(no,text,key):
    if text in fluid[no][key]:
        ermsg = 'fail add tag {} ,already in {}'.format(text,no)
        raise Exception(ermsg)
def cansub(no,text,key):
    if not text in fluid[no][key]:
        ermsg = 'fail sub tag {} ,not in {}'.format(text,no)
        raise Exception(ermsg)
#comm can be same text.fine.
#now all tags became dict. fine.
#20201031 3am, now all dict. append is so- simple. can access[-1]



def addn(no,user,key):
    try:
        whatdid='addn'
        inputcheck(no,user,text)#note text changed key here.
        time = datestr()
        fluid[no][text]+=1
        log(whatdid,no,user,key, time)
        return True
    except Exception as e:
        print(e)
        return False
def subn(no,user,text):
    try:
        whatdid='subn'
        inputcheck(no,user,text)
        time = datestr()
        fluid[no][text]-=1
        log(whatdid,no,user,key, time)
        return True
    except Exception as e:
        print(e)
        return False



#태그는 일단 개수가 없다...인데 나중에 인기캐릭터도나올테지.할까?
#이것도나름경쟁될듯.ㅇㅋ.

#['캐릭터태그','캐']
['캐릭터태그','유저태그','댓글','요청',]
def addtag(no,user,key,text):
    try:
        whatdid='addtag'
        inputcheck(no,user,text)
        time = datestr()
        key='태그'
        canaddtag(no,text,key)
        fluid[no][key].append(text)
        log(whatdid,no,user,text,time)
        return True
    except Exception as e:
        print(e)
        return False

# def addtag(no,user,text):
#     try:
#         whatdid='addtag'
#         inputcheck(no,user,text)
#         time = datestr()
#         key='태그'
#         canaddtag(no,text,key)
#         fluid[no][key].append(text)
#         log(whatdid,no,user,text,time)
#         return True
#     except Exception as e:
#         print(e)
#         return False
# def subtag(no,user,text):
#     try:
#         whatdid='subtag'
#         inputcheck(no,user,text)
#         time = datestr()
#         key='태그'
#         cansubtag(no,text,key)
#         fluid[no][key].remove(text)
#         log(whatdid,no,user,text,time)
#         return True
#     except Exception as e:
#         print(e)
#         return False
#
# def addtagu(no,user,text):
#     try:
#         whatdid='addtagu'
#         inputcheck(no,user,text)
#         time = datestr()
#         key='유저태그'
#         canaddtag(no,text,key)
#         fluid[no][key].append(text)
#         log(whatdid,no,user,text,time)
#         if addn(no,user,'태') == True:
#             return True
#     except Exception as e:
#         print(e)
#         return False
# def subtagu(no,user,text):
#     try:
#         whatdid='subtagu'
#         inputcheck(no,user,text)
#         time = datestr()
#         key='유저태그'
#         cansubtag(no,text,key)
#         fluid[no][key].remove(text)
#         log(whatdid,no,user,text,time)
#         if subn(no,user,'태') == True:
#             return True
#     except Exception as e:
#         print(e)
#         return False
#
#
# def addcomm(no,user,text):
#     try:
#         whatdid='addcomm'
#         inputcheck(no,user,text)
#         time = datestr()
#         key='댓글'#fluid[no][key]=[]
#         canaddtag(no,text,key)
#         fluid[no][key].append( [user,text,time] )
#         log(whatdid,no,user,text,time)
#         #logue.append( ["addcomm('{}','{}','{}')".format(no,user,text),time] )
#         if addn(no,user,'댓') == True:
#             return True
#     except Exception as e:
#         print(e)
#         return False
# def subcomm(no,user,text):
#     try:
#         whatdid="subcomm"
#         inputcheck(no,user,text)
#         time = datestr()
#         key='댓글'#fluid[no][key]=[]
#         cansubtag(no,text,key)
#         fluid[no][key].remove( [user,text,time] )
#         log(whatdid,no,user,text,time)
#         if subn(no,user,'댓') == True:
#             return True
#     except Exception as e:
#         print(e)
#         return False

'''
loadJson( jsonFile = 'datas.json')
saveJson(parsedDict,jsonFile)
'''

#def log(no,user,text,time):
#logue.append( [whatdid,no,user,text,time] )
def log(whatdid,no,user,text,time):
    logue.append( [whatdid,no,user,text,time] )

def backupfluid():
    filename = itername('fluid','txt')
    saveJson(fluid,filename)

def backuplogue():
    filename = itername('logue','txt')
    saveJson(logue,filename)


import os
def itername(filename,ext):
    #'b_','fluid.txt'
    flist = os.listdir()
    no=0
    isok = "{}_backup{}.{}".format(filename,ext)
    while isok in flist:
        no+=1
        isok = "{}_backup{}.{}".format(filename,ext)
    print('backup no:',no)
    #datasdictPath = './b_datas.json'
    #datasdictPath = './b{}_datas.json'.format(no)
    return isok

##if __name__ == "__main__":
##    fluid={}
##    logue=[]
##    print( 'fluidset(id)' )

##def addn(user,no,key):
##    try:
##        fluid[no][key]+=1
##        logue.append( "addn('{}','{}','{}')".format(user,no,key) )
##        return True
##    except:
##        return False

##def addn(user,no,key):
##    try:
##        fluid[no][key]+=1
##        k=1
##        logue.append( "addn('{}','{}','{}')".format(user,no,key) )
##        return True
##    except:
##        if k: fluid[no][key]-=1
##        return False

##def subcomm(user,no,text,time):
##    try:
##        key='댓글'#fluid[no][key]=[]
##        fluid[no][key].remove( {'작성자':user, '내용':text, '시간': time } )
##        logue.append( "subcomm('{}','{}','{}','{}')".format(user,no,text,time) )
##        k=1
##        if subn(user,no,'댓') == True:
##            return True
##    except:
##        if k:fluid[no][key].remove( {'작성자':user, '내용':text, '시간': time } )
##        return False



#-----------below worklog.. not usful maybe.


"addn('하나요','11','추수')"
"subn('마키','115125','조회수')"
"addn('마키','115125','조회수',-1)"
"addn('마키','115125','조회수',1)"#seems fine.
"addtag('마키','115125','태그','한적함',1)"
"addtag('마키','115125','태그','한적함',-1)"#???
#seems bad..

#str(1).isdigit()
#n should be N. int. so +=1.
#saveJson(parsedDict,jsonFile):
#loadJson( filename = 'datas.json'):
#loadJson,saveJson,subn,addn
#addn(user,no,key)


##for no in fluid:#no shall be int, not str. id is not int. ok.
##    no['조회수'] =3

##tagsort={}
##for no in fluid:#no shall be int, not str. id is not int. ok.
##    tagsort[no] = len(no['유저태그'])
##tagsortList = list(tagsort.values())
##tagsortList.sort()???
#thanks for using addn and '태' . no need like this! haha!

##commsortList = list(commsort.values())
##commsortList = list(commsort.keys())
##commsortList.sort()
#lol... it tested. fine.  we use dict[key]= value

#commlen = len(fluid[no]['댓글'])
#replaced by '댓'

#writer = fluid[no]['댓글'][n]['작성자']
#we get directly.. not this way..
# com = fluid[no]['댓글'][n]
# write ( com['작성자'],com['시간'],com['내용'])
