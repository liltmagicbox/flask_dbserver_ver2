'''
from fluiddb import *
for global use fluid,logue.
addn(user,no,'조')
subn(user,no,'조')
addn(user,no,'추')
subn(user,no,'추')
addn(user,no,'좋')
subn(user,no,'좋')
addtagu(user,no,text)
subtagu(user,no,text)
addtag(user,no,text)
subtag(user,no,text)
addcomm(user,no,text,time)
subcomm(user,no,text,time)
'''

fluid={}
logue=[]
print('fluiddb loading.. use','fluidset( strid )' )

from jsonio import *
'''
loadJson( jsonFile = 'datas.json')
saveJson(parsedDict,jsonFile)
'''

#for no in fluid:#no shall be int, not str.-??? id is not int. ok.
# since id in datas is parsed txt, id shall be str, not int.

#remember, no strint, not int.
def fluidset(no):
    try:
        no + 'str'#if type(no) == type(1):
        if no in fluid.keys():
            raise Exception(' no already was. in fluid')
        fluid[no]={}
        fluid[no]['조']=0
        fluid[no]['좋']=0
        fluid[no]['추']=0
        fluid[no]['태']=0#2 used sort.. for fast.
        fluid[no]['댓']=0#2 used sort.. for fast.
        fluid[no]['태그']=[]
        fluid[no]['유저태그']=[]
        fluid[no]['댓글']=[]
        return True
    except:
        return False

def noexist(no):
    if no in fluid.keys():
        return True
    else:
        return False


def addn(user,no,key):
    try:
        fluid[no][key]+=1
        logue.append( "addn('{}','{}','{}')".format(user,no,key) )
        return True
    except:
        return False
def subn(user,no,key):
    try:
        fluid[no][key]-=1
        logue.append( "subn('{}','{}','{}')".format(user,no,key) )
        return True
    except:
        return False


def inputcheck(user,no,text):
    if not type(user)==type(no)==type(text)==type('s'):
        ermsg = 'input type error'
        raise Exception(ermsg)

def canaddtag(no,text,key):
    if text in fluid[no][key]:
        ermsg = 'try++ {} already in {}'.format(text,no)
        raise Exception(ermsg)
def cansubtag(no,text,key):
    if not text in fluid[no][key]:
        ermsg = 'try-- {} not in {}'.format(text,no)
        raise Exception(ermsg)
#comm can be same text.fine.

def addtagm(user,no,text):
    try:
        inputcheck(user,no,text)
        key='태그'
        canaddtag(no,text,key)
        fluid[no][key].append(text)
        logue.append( "addtagm('{}','{}','{}')".format(user,no,text) )
        return True
    except:
        return False
def subtagm(user,no,text):
    try:
        inputcheck(user,no,text)
        key='태그'
        cansubtag(no,text,key)
        fluid[no][key].remove(text)
        logue.append( "subtagm('{}','{}','{}')".format(user,no,text) )
        return True
    except:
        return False

def addtag(user,no,text):
    try:
        inputcheck(user,no,text)
        key='유저태그'
        canaddtag(no,text,key)
        fluid[no][key].append(text)
        logue.append( "addtag('{}','{}','{}')".format(user,no,text) )
        if addn(user,no,'태') == True:
            return True
    except:
        return False
def subtag(user,no,text):
    try:
        inputcheck(user,no,text)
        key='유저태그'
        cansubtag(no,text,key)
        fluid[no][key].remove(text)
        logue.append( "subtag('{}','{}','{}')".format(user,no,text) )
        if subn(user,no,'태') == True:
            return True
    except:
        return False

    
def addcomm(user,no,text,time):
    try:
        inputcheck(user,no,text)
        key='댓글'#fluid[no][key]=[]
        fluid[no][key].append( {'작성자':user, '내용':text, '시간': time } )
        logue.append( "addcomm('{}','{}','{}','{}')".format(user,no,text,time) )
        if addn(user,no,'댓') == True:
            return True
    except:
        return False
def subcomm(user,no,text,time):
    try:
        inputcheck(user,no,text)
        key='댓글'#fluid[no][key]=[]
        fluid[no][key].remove( {'작성자':user, '내용':text, '시간': time } )
        logue.append( "subcomm('{}','{}','{}','{}')".format(user,no,text,time) )
        if subn(user,no,'댓') == True:
            return True
    except:
        return False

'''
loadJson( jsonFile = 'datas.json')
saveJson(parsedDict,jsonFile)
'''

def backuplogue():
    itername('b_','logue.txt')
    filename = saveJson(fluid,filename)

def backupfluid():
    filename = itername('b_','fluid.txt')
    saveJson(logue,filename)

import os
def itername(A,B):
    #'b_','fluid.txt'
    flist = os.listdir()
    no=0
    while A + str(no) + B in flist:
        no+=1
    print('backup no:',no)
    #datasdictPath = './b_datas.json'
    #datasdictPath = './b{}_datas.json'.format(no)
    return A + str(no) + B

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

