'''
basic work flow:
jarList = os.listdir(jar)
newDatas = getJar(oldDatas,jarList)
resizeImg(newDatas)
datas = appendDict(datas , newDatas)
txt2dict.saveJson(datas,'datas.json')
'''

jar = 'dumpjar'

statics = 'static'
origins = 'static/origin'
resizeds = 'static/resized'
thumbs = 'static/thumb'

pastebin = 'pastebin'
txtFiledir = ''

imgExt = ['jpg','jpeg','JPG','JPEG','png','PNG',
          'gif','GIF','webp','WEBP','bmp','BMP']

parseKeys = ['번호','제목','작성자','날짜','태그','본문']
idKey = parseKeys[0]
multiLineKey = parseKeys[-1]

originKey = '원본'
#allfilesKey = 'allfiles'

##shutil.copytree(old,new,dirs_exist_ok = overWrite)
##shutil.move(old,new)
#import movefolders
import txt2dict
import os
import shutil
#get before happens.
import sys
import datetime
import random
def barrand6():
    return '_'+str( random.randint(1,1000000))
#os.rename(noFolderpath, pastebin+'/'+noFolder+barrand6() )


# a = 'dumpjar'
# b = 'static/origin'
#movefolders.copyFolders(a,b)

#txt load, get json
##glob.glob('static/origin/*')
##os.listdir('static/origin/')

#read txt, append dict.


def makedirs():
    try:
        os.mkdir( './'+statics )
        print('statics done')
    except:
        pass
    try:
        os.mkdir('./'+origins )
        print('origin done')
    except:
        pass
    try:
        os.mkdir( './'+resizeds )
        print('resizeds done')
    except:
        pass
    try:
        os.mkdir('./'+thumbs )
        print('thumbs done')
    except:
        pass
    try:
        os.mkdir( pastebin )
        print('pastebin done')
    except:
        pass
    try:
        os.mkdir( jar )
        print('jar done')
    except:
        pass
    print('minidb loading..all dirs already')

makedirs()

'notice it can move origin to origin. good for test!!'
#load jar, read txt, if not in dict:add , copy origins,move pastebin.
def getJar(oldDatas,jarList):
    """
    returns new dict, not in old dict.
    if already was, delete that no folder.
    """
    #clear pastebin here. confirmed.
    if pastebin in os.listdir():
        tempdir = barrand6()
        os.rename(pastebin,tempdir)#clever..fine..
        shutil.rmtree(tempdir)#acces deniyed     ..fixed!
        os.mkdir(pastebin)


    oldDatakeys = oldDatas.keys()
    newDatas = {} #for data insure.

    for noFolder in jarList:
        try:
            #txtFiledir = os.path.join( origins,noFolder,noFolder+'.txt')
            txtFilename = noFolder+'.txt'
            #------------------------user pre-sure.
            txtfiles = []
            for f in os.listdir( os.path.join( jar,noFolder) ):
                if '.txt' in f:
                    txtfiles.append(f)
            if len(txtfiles) == 1:
                txtFilename = txtfiles[0]
            else:
                if not '설정.txt' in txtfiles:
                    raise Exception('ERROR no txt : ' + str(noFolder))
                txtFilename = '설정.txt'
            #------------------------user pre-sure

            txtFile = os.path.join( jar,noFolder,txtFilename) #whatif dir = no.txt?
            parsedDict = txt2dict.parseTxt(txtFile,parseKeys,multiLineKey)#hope it's atleast complete...

            #----------------------for custom dict additional option
            checklist = ['번호','제목','작성자','날짜','본문']
            for c in checklist:
                if not c in parsedDict.keys():
                    raise Exception('ERROR!! not format txt : ' + str(noFolder))

            #user input, do another func.
            #'16'.isdigit()
            #if int(parsedDict['번호'])<1:
                #raise Exception('ERROR!! of : ' + str(noFolder))
            #a = parsedDict['날짜'].split('.')
            #b = str(datetime.date.today()).split('-')
            #if datetime.date(a[0],a[1],a[2]) < datetime.date.today()

            if '태그' in parsedDict.keys():
                tagList = parsedDict['태그'].split(',')
                parsedDict['유저태그'] = tagList
                del parsedDict['태그']
            else:
                parsedDict['유저태그'] = []

            if parsedDict['제목'].startswith('[번역]'):
                parsedDict['제목'] = parsedDict['제목'].split('[번역]')[1].strip()
                if parsedDict['제목'].find('센세)') != -1 :
                    parsedDict['유저태그'].append( parsedDict['제목'].split('센세)')[0].strip()+'센세' )
                    #parsedDict['태그'].append( a.split('[번역]')[1].strip().split('센세)')[0]+'센세)' )
            #----------------------for custom dict additional option


            #----------------------------- after get parsedDict.
            tmpKey = parsedDict[idKey]       #9133114
            if tmpKey in oldDatakeys:
                raise Exception('skip.. id already in parsedict ..: ' + str(noFolder))

            idFoldername = parsedDict['번호']
            noFolderpath = os.path.join( jar,noFolder )
            originPath = os.path.join( origins , idFoldername )
            shutil.copytree(noFolderpath,originPath, dirs_exist_ok = False)# was true, but to integrity....
            #it occured at test. nodict, but files.
            #shutil.move(noFolderpath,pastebin)


            #datas is dict object, appended new key,value.
            #add more value.
            #datas[tmpKey]['key'] = 'value'

            # get moved nofolder, add datas originImgs.
            originFiles = os.listdir(os.path.join( origins, idFoldername))
            originImgs = []
            for img in originFiles:
                ext = os.path.splitext( img )[1][1:]     # .jpg == jpg
                if ext in imgExt:     #now, it's img.
                    originImgs.append(img)
            if originImgs==[]:
                raise Exception('ERROR!! no img..: ' + str(noFolder))
            parsedDict[originKey] = originImgs

            newDatas[tmpKey] = parsedDict
            #datas[tmpKey][allfilesKey] = originFiles
            thisrand=barrand6()
            os.rename( os.path.join( jar,noFolder), pastebin+'/'+noFolder+thisrand )

        except Exception as e:
            exc_info = sys.exc_info()#below except.
            errmsg = exc_info[1],':at line',exc_info[2].tb_lineno
            print(errmsg)

            thisrand=barrand6()
            os.rename( os.path.join( jar,noFolder), pastebin+'/'+noFolder+thisrand )
            f = open('./'+pastebin+'/'+noFolder+thisrand+'/err.txt','w',encoding='utf-8')
            f.write(str(errmsg))
            f.close()
            print( 'ERROR occured. gone pastebin :',str(noFolder)+thisrand)
            continue

    return newDatas




def appendDict(oldDict,newDict):
    for i in newDict:
        if i not in oldDict:
            pass
        else:
            print('BUGBUG...dict appending.... already!')
            return oldDict

    for i in newDict:
        oldDict[i] = newDict[i]
    return oldDict


##datas={}
##oldDatas = datas
'note that it loads dict, usually already was datas.json.. and adds.fine.'
def jarScan(datas):

    jsonName = 'datas.json'
    #jarList = os.listdir(jar)#only get dir. fine.
    jarList=[]
    for i in os.listdir(jar):
        if os.path.isdir(  jar+'/'+i ):
            jarList.append(i)
    #print(jarList)
    #we got dir lists. fine.

    if len(jarList) != 0:
        newDatas = getJar(datas,jarList)
        print('jar List:',len(jarList),'== new datas:', len(newDatas))
        if len(newDatas)>0: #means some may be not in ,anyway done.
            newDatas_resized = resizeImg(newDatas)#and adds to newDatas.
            datas = appendDict(datas , newDatas_resized)#returns atleast datas, not {}.
            print('datas len:',len(datas) )
            #txt2dict.saveJson(datas,jsonName)           #for more bigger..
    return datas #for at least..?





import json


##filename = 'datas.json'
##datas = loadJson( filename )
def loadJson( filename = 'datas.json'):
    f=open( filename,'r',encoding='utf-8')
    a=f.read()
    f.close()
    b=json.loads(a)
    return b


'''
import minidb
#for load json get dict:
datas = minidb.loadJson( 'datas.json' )

#for get new from jar , added dict:
datas = minidb.jarScan(datas)  # in datas, get datas :added. saving json.
'''


#before we got dict, and moved to origins. now, convert phase.
#input dict, origin dir, outputs resized folder & imgs.

#maybe can go out..
    #phase3, convert img. we got imglist, dir, ..to path.
from PIL import Image
resizedKey = '리사이즈'


#newDatas = datas
def resizeImg(newDatas):
    imgnumbers=0

    newKeys = newDatas.keys()
    for no in newKeys:
        imgList = newDatas[no][originKey]#origin img list.
        resizedList = []
        thumbList = []
        os.mkdir( os.path.join(resizeds, no))
        os.mkdir( os.path.join(thumbs, no))

        onlynameList=[]
        for i in imgList:
            iname,iexp = os.path.splitext( i )
            if iname in onlynameList:
                iname = iname+barrand6()
            else:
                onlynameList.append(iname)
            #print(iexp,iname)

            isrc = os.path.join(origins, no, i)
            idest = os.path.join(resizeds, no, iname )
            thumbDest = os.path.join(thumbs, no, iname )

            im = Image.open(isrc)

            if iexp not in ['.GIF','.gif']:
                imh = int(im.size[1]/(im.size[0]/700))
                im.resize((700,imh),Image.LANCZOS).convert('RGB').save( idest+'.jpg' ,quality=90)
                resizedList.append( iname+'.jpg' )

                #for thumbnail
                imw = 300
                imh = int(im.size[1]/(im.size[0]/imw))
                if imh >=imw:
                    nim = im.resize((imw,imh),Image.LANCZOS)
                    imh = imw
                    nim.crop( (0,0,imw,imh) ).convert('RGB').save( thumbDest+'.jpg' ,quality=80)
                #im.resize((300,imh),Image.LANCZOS).convert('RGB').save( thumbDest+'.jpg' ,quality=80)
                elif imh <imw:
                    imh = 300
                    imw = int( (im.size[0]/im.size[1]*imh))
                    nim = im.resize((imw,imh),Image.LANCZOS)
                    #imw = imh

                    nim.crop( ((imw/2 -imh/2), 0, (imw/2 +imh/2), imh) ).convert('RGB').save( thumbDest+'.jpg' ,quality=80)


                thumbList.append( iname+'.jpg' )
            else:
                im.save( idest+'.gif')
                resizedList.append( iname+'.gif' )

                #tumb
                #im.save( thumbDest+'.gif')
                #thumbList.append( iname+'.gif' )
                #add for jpg not GIF
                imw = 300
                imh = int(im.size[1]/(im.size[0]/imw))
                if imh >=imw:
                    nim = im.resize((imw,imh),Image.LANCZOS)
                    imh = imw
                    nim.crop( (0,0,imw,imh) ).convert('RGB').save( thumbDest+'.jpg' ,quality=80)
                elif imh <imw:
                    imh = 300
                    imw = int( (im.size[0]/im.size[1]*imh))
                    nim = im.resize((imw,imh),Image.LANCZOS)
                    nim.crop( ((imw/2 -imh/2), 0, (imw/2 +imh/2), imh) ).convert('RGB').save( thumbDest+'.jpg' ,quality=80)
                #add for jpg not GIF
                thumbList.append( iname+'.jpg' )
            imgnumbers+=1
        newDatas[no][resizedKey] = resizedList
    print( "converted imgs:",str(imgnumbers) )
    return newDatas

#so we got datas, fine dataset. as dict.

#after functioning, we do next,, make bodys ,heads.
    #body is , each id .txt file.fine. containing only '본문'
    #heads is .. else.containging.. exported as js file. a big file.
