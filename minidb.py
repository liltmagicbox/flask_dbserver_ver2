jar = 'dumpjar'
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


# a = 'dumpjar'
# b = 'static/origin'
#movefolders.copyFolders(a,b)

#txt load, get json
##glob.glob('static/origin/*')
##os.listdir('static/origin/')

#read txt, append dict.


def makedirs():
    try:
        os.mkdir( os.getcwd()+'/'+origins )        
    except:
        pass
    try:
        os.mkdir( os.getcwd()+'/'+resizeds )
    except:
        pass
    try:
        os.mkdir( os.getcwd()+'/'+thumbs )
    except:
        pass
    try:
        os.mkdir( os.getcwd()+'/'+thumbs )
    except:
        pass
    try:
        os.mkdir( pastebin )
    except:
        pass
    try:
        os.mkdir( jar )
    except:
        pass
    print('all allready.')

'notice it can move origin to origin. good for test!!'
#load jar, read txt, if not in dict:add , copy origins,move pastebin.
def getJar(oldDatas,jarList):
    makedirs()
    """
    returns new dict, not in old dict.
    if already was, delete that no folder.
    """
    oldDatakeys = oldDatas.keys()
    newDatas = {} #for data insure.

    for noFolder in jarList:
        #txtFiledir = os.path.join( origins,noFolder,noFolder+'.txt')
        txtFile = os.path.join( jar,noFolder,noFolder+'.txt')
        parsedDict = txt2dict.parseTxt(txtFile,parseKeys,multiLineKey)
        if '태그' in parsedDict.keys():
            tagList = parsedDict['태그'].split(',')
            parsedDict['유저태그'] = tagList
            del parsedDict['태그']
        else:
            parsedDict['유저태그'] = []
        

        if '제목' in parsedDict.keys():
            if parsedDict['제목'].startswith('[번역]'):
                parsedDict['제목'] = parsedDict['제목'].split('[번역]')[1].strip()
                if parsedDict['제목'].find('센세)') != -1 :
                    parsedDict['유저태그'].append( parsedDict['제목'].split('센세)')[0].strip()+'센세' )
                    #parsedDict['태그'].append( a.split('[번역]')[1].strip().split('센세)')[0]+'센세)' )




        tmpKey = parsedDict[idKey]       #9133114

        noFolderpath = os.path.join( jar,noFolder )
        originPath = os.path.join( origins , noFolder )
        if tmpKey not in oldDatakeys:   #means new one.
            newDatas[tmpKey] = parsedDict

            #if os.listdir( os.path.join( jar,noFolder) )
            try:
                #movefolders.copyAinB( noFolderdir, origins)#inside to inside of.
                shutil.copytree(noFolderpath,originPath, dirs_exist_ok = True)
                #print(str(tmpKey),'copy success, files to origins')

            except:
                del newDatas[tmpKey]
                #print('error.. delete this no. dict.')
            #movefolders.moveAinB( noFolderdir, pastebin ) # A moved in B
            shutil.move(noFolderpath,pastebin)


            #datas is dict object, appended new key,value.
            #add more value.
            #datas[tmpKey]['key'] = 'value'

            # get moved nofolder, add datas originImgs.
            originFiles = os.listdir(os.path.join( origins,noFolder))
            originImgs = []
            for img in originFiles:
                ext = os.path.splitext( img )[1][1:]     # .jpg == jpg
                if ext in imgExt:     #now, it's img.
                    originImgs.append(img)
            #print(originImgs)
            newDatas[tmpKey][originKey] = originImgs
            #datas[tmpKey][allfilesKey] = originFiles
        else:
            #print('key already dicted..')
            shutil.move(noFolderpath,pastebin)

    return newDatas




def appendDict(oldDict,newDict):
    for i in newDict:
        if i not in oldDict:
            pass
        else:
            print('bad dict!')
            return {}

    for i in newDict:
        oldDict[i] = newDict[i]
    print('good, dict appended')
    return oldDict


##datas={}
##oldDatas = datas

def jarScan(datas):
    jsonName = 'datas.json'
    jarList = os.listdir(jar)
    if not len(jarList) == 0:
        print('jar List length of: ',len(jarList))
        newDatas = getJar(datas,jarList)
        print('jar List appended: ',len(newDatas))
        resizedlen = resizeImg(newDatas)
        print('imgs resized: ', str(resizedlen) )

        if len(newDatas)>0:
            datas = appendDict(datas , newDatas)
            print('new Dict appended: ',len(newDatas),'finally :',len(datas) )
            txt2dict.saveJson(datas,jsonName)
            print('json saved:'+str(jsonName),'length of: ',len(datas))
    else:
        print('error jarScan')
    return datas #for at least..?


##jarList = os.listdir(jar)
##newDatas = getJar(oldDatas)
##resizeImg(newDatas)
##datas = appendDict(datas , newDatas)
##txt2dict.saveJson(datas,'datas.json')


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


        resizedList = []
        try:
            os.mkdir( os.path.join(resizeds, no))
        except:
            print('no resizeds dir already!! ')
            
        thumbList = []
        try:
            os.mkdir( os.path.join(thumbs, no))
        except:
            print('no thumb dir already!! ')

        imgList = newDatas[no][originKey]#origin img list.
        for i in imgList:

            iname,iexp = os.path.splitext( i )
            #print(iexp,iname)
            imgnumbers+=1

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
                    imw = imh
                    nim.crop( (0,0,imw,imh) ).convert('RGB').save( thumbDest+'.jpg' ,quality=80)


                thumbList.append( iname+'.jpg' )
            else:
                im.save( idest+'.gif')
                resizedList.append( iname+'.gif' )

                #tumb
                im.save( thumbDest+'.gif')
                thumbList.append( iname+'.gif' )

        newDatas[no][resizedKey] = resizedList

    return str(imgnumbers) #do we need it? now, err if err.


#so we got datas, fine dataset. as dict.

#after functioning, we do next,, make bodys ,heads.
    #body is , each id .txt file.fine. containing only '본문'
    #heads is .. else.containging.. exported as js file. a big file.
