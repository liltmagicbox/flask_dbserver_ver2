'''
chrome can bear 40MB. fine.
dict db system designed handle 100000 of articles.

sortlist of 100000 is 8MB
articles of 10000 is 4MB
novels of 1000 is 50MB

-------------
articles 400B for 1?. yeah. since having full img list.
{제목: 어쩌구저쩌구최대20자는넘겠나,
날짜: 20202033,
번호: _2332302200,
imgs=6,
thumbs=6,
gifs=[3,4]}
썸넬은 이후 확장용인데, 보내는실시간생성이니 이후 추가하자;?

new articles 100000 for 10MB.fine.
imgs: id_1 .x.
'''


postbox={} #global all message from users.
pastebin={} #global all bin. dict, even article!
box={} # means it's for box.
print('fluiddb loading..')

from jar import parseKeys
idkey,titlekey,writerkey,datekey,bodykey = parseKeys

userkey, textkey, timekey, seekey=("유저","내용","시간","보기")
#box={}
#box[id]={}
nlist = ["조","좋"]
taglist = ["주연","태그"]
textlist = ["댓글"]
def setbox(id):
    id = str(id)# insure str. for jsonsave.
    box[id]={}

    for i in nlist:
        box[id][i] = 0
    for i in taglist:
        box[id][i] = {}
    for i in textlist:
        box[id][i] = {}

#fluid.box.addtag(no,user,key,text)
def settag(user,no,key,text):
    try:
        text=str(text)#insure new key-val is str.for jsonsave
        time = millisec()
        box[no][key][text] = {userkey:user, textkey:text, timekey:time, seekey:'all'}
        return True
    except Exception as e:
        errlog(e)
        return False

def settext(user,no,key,text):
    try:
        if len( box[no][key] ) ==0:
            idx = '001'
        else:
            stridx = str( int(max( box[no][key] )) +1 )
            buff = 3-len( stridx )#'999' max idx.
            idx = '0'*buff + stridx
        time = millisec()
        box[no][key][idx] = {userkey:user, textkey:text, timekey:time, seekey:'all'}
        return True
    except Exception as e:
        errlog(e)
        return False

def postmsg(user,no,text):
    try:
        time = millisec()
        postbox[time] = "{}:{}".format(user,text)
    except Exception as e:
        errlog(e)
        return False

def paste(no,key,idx):#note pastebinis vari.
    try:
        time = millisec()
        pastebin[time] = {"no":no,"key":key,"idx":idx,"val":box[no][key][idx] }
        del box[no][key][idx]#hope pasbin remained. atleast 1,'1'can. or deepcopy.
    except Exception as e:
        errlog(e)
        return False
def unpaste(time):
    try:
        no,key,idx,val = pastebin[time]
        box[no][key][idx] = val
    except Exception as e:
        errlog(e)
        return False


import time
def millisec():
    return str(int(time.time()*1000))


#-----------------------backup feature
import datetime
tzinfo=datetime.timezone(datetime.timedelta(seconds=32400))
def datestr():
    now = datetime.datetime.now()
    now=now.astimezone(tzinfo)
    return now.strftime("%Y%m%d_%H%M%S")

from jsonio import *
'''
loadJson( jsonFile = 'datas.json')
saveJson(parsedDict,jsonFile)
'''


backupdir = "backup"
staticdir = 'static'
import os
try:
    backuppath = "./{}/{}".format(staticdir,backupdir)
    os.mkdir( backuppath )
    print('backupdir created')
except:
    pass

def backup():
    try:
        filename = "./{}/{}.{}".format(backupdir,datestr(),"txt")
        mega=[box,postbox,pastebin]
        saveJson(mega,filename)
    except Exception as e:
        errlog(e)
        return False

def backdown():
    global box
    global postbox
    global pastebin
    try:
        filename = "./{}/{}.{}".format(backupdir,datestr(),"txt")
        box,postbox,pastebin = loadJson(filename)
    except Exception as e:
        errlog(e)
        return False

#-------------errlog
errtxtname = "./{}/{}.{}".format(staticdir,'err_fluid',"txt")
def errlog(e):
    e = datestr() +":"+ str(e)[0:80]
    with open(errtxtname,'a',encoding='utf-8') as f:
        f.write(e)
        f.write('\n')




if __name__ == "__main__":
    print( 'fluid run as main' )
