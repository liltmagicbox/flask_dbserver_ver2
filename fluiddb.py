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
maxidx ="maxidx"
postbox[maxidx]=0
pastebin[maxidx]=0

box={} # means it's for box.
print('fluiddb loading..')

#------------------ variable names!!
#from jar.
from jar import parseKeys , imgKeys
#parseKeys = ['번호','제목','작성자','날짜','본문']# all or not.
id_key,title_key,writer_key,date_key,body_key = parseKeys#used for headdict
originkey,resizedkey,thumbkey = imgKeys

#gifs_key = "gifs"
img_key = "imgs"
thumb_key = "thumbs"

#fluid inner keys
fluidKeys = [ "조회", "좋아", "주연", "태그", "댓글", ]
view_key, like_key, hero_key, tag_key, comm_key, = fluidKeys

#for tag, text...and post.
user_key, text_key, time_key, see_key = ["유저","내용","시간","보기"]

#for see state of tag,text
seestate = ["all","hidden"]
see_default = seestate[0]

#post setting
idof_key = "원글"
poststate = ["new","done","alert"]
post_default = poststate[0]
#------------------ variable names!!


nlist = [view_key,like_key]
taglist = [hero_key,tag_key]
textlist = [comm_key]
def setbox(id):
    id = str(id)# insure str. for jsonsave.
    box[id]={}
    for i in parseKeys:
        box[id][i]=""
    for i in imgKeys:
        box[id][i]=[]

    for i in nlist:
        box[id][i] = 0
    for i in taglist:
        box[id][i] = {}
    for i in textlist:
        box[id][i] = {}
    scanrawids()
    scanidxs()#since list(range(10000000)took 1s.
    return True

#fluid.box.addtag(no,user,key,text)
def settag(user,no,text):
    try:
        key = tag_key
        text=str(text)#insure new key-val is str.for jsonsave
        time = millisec()
        box[no][key][text] = {user_key:user, text_key:text, time_key:time, see_key:see_default}
        return True
    except Exception as e:
        errlog(e)
        return False
def setherotag(user,no,text):
    try:
        key = hero_key
        text=str(text)#insure new key-val is str.for jsonsave
        time = millisec()
        box[no][key][text] = {user_key:user, text_key:text, time_key:time, see_key:see_default}
        return True
    except Exception as e:
        errlog(e)
        return False

def setcomm(user,no,text):
    try:
        key = comm_key
        if len( box[no][key] ) ==0:
            idx = '001'
        else:
            stridx = str( int(max( box[no][key] )) +1 )
            buff = 3-len( stridx )#'999' max idx.
            idx = '0'*buff + stridx
        time = millisec()
        box[no][key][idx] = {user_key:user, text_key:text, time_key:time, see_key:see_default}
        return True
    except Exception as e:
        errlog(e)
        return False


#--------------------misc storage.
def postmsg(user,no,text):
    try:
        time = millisec()
        postbox[maxidx]+=1
        stridx = str( postbox[maxidx] )#for jsonsave
        postbox[stridx] = {
        time_key:time,
        user_key:user,
        idof_key:no,
        text_key:text,
        state_key:state_default}

        return True
    except Exception as e:
        errlog(e)
        return False

def paste(no,key,idx):#note pastebinis vari.
    try:
        time = millisec()
        pastebin[maxidx]+=1
        stridx = str( pastebin[maxidx] )#for jsonsave
        #pastebin[stridx] = {"time":time,"no":no,"key":key,"idx":idx,"val":box[no][key][idx] }
        pastebin[stridx] = [ time,no,key,idx,box[no][key][idx] ]
        del box[no][key][idx]#hope pasbin remained. atleast 1,'1'can. or deepcopy.
        return True
    except Exception as e:
        errlog(e)
        return False
def unpaste(stridx):
    try:
        time,no,key,idx,val = pastebin[stridx]
        box[no][key][idx] = val
        return True
    except Exception as e:
        errlog(e)
        return False

#for value in data.
import time
def millisec():
    return str(int(time.time()*1000))

#-------------------------------------

#view_key, like_key, hero_key, tag_key, comm_key, = fluidKeys
#fluidKeys = [ "조회", "좋아", "주연", "태그", "댓글", ]
#user_key, text_key, time_key, see_key = ["유저","내용","시간","보기"]#for tag, text.

#----------------memory list
rawids = []
def scanrawids():
    global rawids
    rawids = list(box.keys())
idxs = []
def scanidxs():
    global idxs
    idxs = list(range(len(rawids)))

#tagdict : { tname, tname2, tanema, taneme,,,}   / tname = [ 1124,1151 ,15135135,235,,,,]
tagdict={}
def tagscan():
    global tagdict
    tagdict = {}
    for id in box:
        for tname in box[id][tag_key]:
            if tagdict.get(tname) == None:
                tagdict[tname] = []#hope same id in tname not happen
            tagdict[tname].append(id)

herotagdict={}
def herotagscan():
    global herotagdict
    tagdict = {}
    for id in box:
        for tname in box[id][hero_key]:
            if tagdict.get(tname) == None:
                tagdict[tname] = []#hope same id in tname not happen
            tagdict[tname].append(id)
#----------------memory list


#----------------export headdata
# 번호: _2332302200,
# 제목: 어쩌구저쩌구최대20자는넘겠나,
# 날짜: 20202033,
# imgs=6,
# thumbs=6,
# gifs=[3,4]
def getheaddict():
    headlist = []
    for idx,j in enumerate(rawids):
        rawid = rawids[idx]
        idx=str(idx)#forjsonsave
        tmpdict = {}

        tmpdict[id_key] = idx #note not id.
        tmpdict[title_key] = box[rawid][title_key]
        #no need writer
        tmpdict[date_key] = box[rawid][date_key]
        #no need bodytext.

        #more relable!
        tmpdict[img_key] =[]

        if box[rawid].get(resizedkey) !=[]:
            for i in box[rawid][resizedkey]:
                tmpdict[img_key].append( i.split(rawid)[-1:] )

        #thums?

        #herotag made. for general rule.
        #tmpdict[hero_key] = box[rawid][hero_key]

        headlist.append(tmpdict)

        #hope id---_1.jpg kinds.
        # giflist = []
        # counter = 1
        # for i in box[rawid][resizedkey]:
        #     if i[-3:].lower() == "gif":
        #         giflist.append(counter)
        #     counter+=1
        # headdict[idx][gifs_key] = giflist
        # headdict[idx][maximg_key] = len(box[rawid][resizedkey])
        # headdict[idx][maxthumb_key] = len(box[rawid][thumbkey])
    return headlist

def headexport():
    try:
        filename = "headdata.json"
        filepath = os.path.join(staticdir,filename)

        herotagscan()

        #mega = [rawids,getheaddict()]
        #varnamelist = ['rawids','heads']
        #saveVarJsonlist(mega,varnamelist,filepath)

        mega = [rawids,herotagdict,getheaddict()]
        varNames=['rawids',"herotag",'headlist']
        saveVarJsonlist(mega,varNames,filepath)

        #saveVarjson(mega,filepath,varName='headdatas')
        return True
    except Exception as e:
        errlog(e)
        return False
#----------------export headdata




#--------------------SORT! returns key list.
#headdict already can make: ..but should we...? -- 300kb, 6= 1.8MB. or 2.4MB.
#def newsort():
#def namesort():

#rawids, idxs
def viewsort():
    kname = view_key
    sortedidxs = sorted( idxs , key= lambda k:box[rawids[k]][kname] ,reverse = True)#higher first
    return sortedidxs
def likesort():
    kname = like_key
    sortedidxs = sorted( idxs , key= lambda k:box[rawids[k]][kname] ,reverse = True)
    return sortedidxs

#k:box[rawids[k]][kname][time_key]
def tagsort():
    kname = tag_key
    sortedidxs = sorted( idxs , key= lambda k: len(box[rawids[k]][kname]) ,reverse = True)
    return sortedidxs
def commsort():
    kname = comm_key
    sortedidxs = sorted( idxs , key= lambda k: len(box[rawids[k]][kname]) ,reverse = True)
    return sortedidxs

#k:box[rawids[k]][kname][time_key]
def newtagsort():
    kname = tag_key
    sortedidxs = sorted( idxs , key= lambda k: box[rawids[k]][kname].get(time_key,"") ,reverse = True)
    return sortedidxs
def newcommsort():
    kname = comm_key
    sortedidxs = sorted( idxs , key= lambda k:box[rawids[k]][kname].get(time_key,"") ,reverse = True)
    return sortedidxs


#sortedidxs to rawbytes! 300KB for 100,000 of item.
from dhexmaker import dhexstr
#dhexstr(list) -> str


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
backuppath = os.path.join(staticdir,backupdir)
try:
    os.mkdir( backuppath )
    print('backupdir created')
except:
    pass

def backup():
    try:
        filename = "{}.{}".format(datestr(),"txt")
        filepath = os.path.join(backuppath,filename)
        mega=[box,postbox,pastebin]
        saveJson(mega,filepath)
        return True
    except Exception as e:
        errlog(e)
        return False

def backdown():
    global box
    global postbox
    global pastebin
    #or, it regardes assign new inner variable
    try:
        flist = os.listdir(backuppath)
        filename = max(flist)
        filepath = os.path.join(backuppath,filename)
        box,postbox,pastebin = loadJson(filepath)
        return True
    except Exception as e:
        errlog(e)
        return False

#-------------errlog
import sys

errtxtname = "./{}/{}.{}".format(staticdir,'err_fluid',"txt")
def errlog(e):
    #e = datestr() +":"+ str(e)[0:80]

    exc_info = sys.exc_info()#below except.
    errmsg = exc_info[1],':at line',exc_info[2].tb_lineno
    e = str(errmsg)[0:80]
    print(e)
    with open(errtxtname,'a',encoding='utf-8') as f:
        f.write(e)
        f.write('\n')




if __name__ == "__main__":
    print( 'fluid run as main' )
