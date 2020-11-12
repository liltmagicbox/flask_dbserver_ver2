jar = 'jar'
static = 'static'
imgtower = 'static/imgtower'

errlist=[]
#for all log in here.
def logerr():
    with open('jarerr.txt','a',encoding='utf-8') as f:
        for i in errlist:
            f.write(i)
            f.write('\n')
    #errlist.clear()# e=[] ,, works as assign.
    #clear not each log. but a batch dude!
    #do it just end of batch!ha!

#-------------for log time.
import datetime
tzinfo=datetime.timezone(datetime.timedelta(seconds=32400))#+9
def datestr():
    now = datetime.datetime.now()
    now=now.astimezone(tzinfo)
    return now.strftime("%Y.%m.%d %H:%M:%S")
#-------------for log time.

import txt2dict
import os
import shutil#os.remove not work if filled.shutil.rmtree(tempdir)
import sys#for log

from resizer import resizeDir
import hashlib#for id10

def makedirs():
    try:
        os.mkdir( './'+static )
        print('statics created')
    except:
        pass
    try:
        os.mkdir( './'+imgtower )
        print('imgtower in statics created')
    except:
        pass
    try:
        os.mkdir( jar )
        print('jar created')
    except:
        pass
    print('jar loading..all dirs ready')

makedirs()


# O(n*2).. it prevents not add already.
def appDict(oldDict,newDict):
    for i in newDict:
        if oldDict.get(i) == None:
            oldDict[i] = newDict[i]
        else:
            errlist.append('{}dict already!! at {}'.format(datestr(),i))
            logerr()
    return oldDict


#make only if exists. not guarantee each key is.
parseKeys = ['번호','제목','작성자','날짜','태그','본문']
multiLineKey = parseKeys[-1]
titlekey = '제목'
idkey = '번호'

#load jar, read txt, if not in dict:add , copy origins,move pastebin.
#preventSet= set(adict.keys())
# a in set is O1.
def getJar(preventSet={}):
    """
    returns new dict. fail, to pastebin.
    let preventSet = oldDict ,, for live check. if getjar too slow, it may be.
    """
    errlist.clear()    
    
    #------pre check if dir in jar--------------------------
    targetDir = jar
    dirList = []
    for i in os.listdir(targetDir):
        if os.path.isdir(  targetDir+'/'+i ):
            dirList.append(i)

    if len(dirList) == 0:
        print('no jar!')
        return {} #think this will stop all func below..
    #------pre check if dir in jar--------------------------

    newDatas = {} #for data insure.

    #noFolder is not full-path, only str.
    for noFolder in dirList:
        noDir = os.path.join( jar,noFolder)
        try:
            #1. check txt in dir.
            txtfiles = []
            for f in os.listdir( noDir ):
                if '.txt' in f.lower():
                    txtfiles.append(f)
            #if empty dir.
            if len(os.listdir( noDir ))==0:
                raise Exception('empty! : ' + str(noFolder))

            # 1:load 0:dir=name,id=sha(name) , 2~:expire!
            if len(txtfiles) == 1:
                txtFile = os.path.join( noDir, txtfiles[0])
                parsedDict = txt2dict.parseTxt(txtFile,parseKeys,multiLineKey)
            elif len(txtfiles) == 0:
                parsedDict = {}
            elif len(txtfiles) > 1:
                raise Exception('txt shall be only one! : ' + str(noFolder))

            #fill dict minimum requirement.
            if parsedDict.get(titlekey) == None:
                parsedDict[titlekey] = noFolder# title become folder name.
            if parsedDict.get(idkey) == None:
                parsedDict[idkey] = '0'+hashlib.sha256( parsedDict[titlekey].encode() ).hexdigest()[:11]
                # id == dirname.. and it prevents same dir name. #if crash, change name!
                #0 for dir see good.. 10 to 11. see better.

            #if already, don't. fine.
            if parsedDict[idkey] in preventSet:
                raise Exception('in preventSet.. passing : ' + str(noFolder))            
            

            #----------------------for custom dict additional option
            #del only [번역]---.
            if parsedDict['제목'].startswith('[번역]'):
                parsedDict['제목'] = parsedDict['제목'].split('[번역]')[1].strip()
            #if '센세)', add 태그.
            if parsedDict['제목'].find('센세)') != -1 :
                if parsedDict.get('태그') == None:
                    parsedDict['태그']=''
                parsedDict['태그'] += '작가:'+parsedDict['제목'].split('센세)')[0].strip()
            #----------------------for custom dict additional option


            #2. we got dict anyway. txt done. now for img. origin created, remaining txt.
            resizedlist = resizeDir(noDir)#0 origin 1 re 2 thumb.
            parsedDict['원본'] = resizedlist[0]
            parsedDict['리사이즈'] = resizedlist[1]
            parsedDict['썸네일'] = resizedlist[2]

            #3.what? ah. move to ..the.. storage.
            #assume already was not happens..   ..maybe.rollback, it can happen

            #idkey  1113033 if crawl / hash10 if user.
            idDir = os.path.join( imgtower, parsedDict[idkey] )
            os.rename( noDir, idDir )
            tmpKey = parsedDict[idkey]
            newDatas[tmpKey] = parsedDict

        except Exception as e:
            exc_info = sys.exc_info()#below except.
            errmsg = exc_info[1],':at line',exc_info[2].tb_lineno
            print(errmsg)
            errlist.append( "{}err while getjar,{},{}".format(datestr(),noFolder,errmsg) )
            
            #os.remove( os.path.join(os.getcwd(),noDir) )#note it requires path, not dir. perm. error!
            shutil.rmtree(noDir)
            continue#what is it? im not sure..
            #pass go through, continue break,next!

    print( "newdatas:{},err:{}".format(len(newDatas),len(errlist) ) )
    logerr()
    return newDatas,errlist
