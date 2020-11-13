#created 2020-11-12. fine. target dir, check imgs, get it resized.
#note it outputs dict. with key.
#..think better list[0,1,2].. changed.
#...no. list(3) cant find what it is. dict can by key.
#...no. cant remember.. but 0,1,2 is origin, resized, thumb. too clear.
import os
from PIL import Image
#it make more general..good.
def resizeDir( targetDir, resizew=700,thumbw=300):

    origin_dir = 'origin'
    resized_dir = 'resized'
    thumb_dir = 'thumb'

    imgExt = ['jpg','jpeg','JPG','JPEG','png','PNG',
              'gif','GIF','webp','WEBP','bmp','BMP']

    files = os.listdir( targetDir )
    imgList = []
    for f in files:
        ext = os.path.splitext( f )[1][1:]     # .jpg == jpg
        if ext in imgExt:     #now, it's img.
            imgList.append(f)

    #imgList=[]..

    # break below. no img, no dirs!
    if len(imgList)==0:
        returnList=[[],[],[]]
        return returnList


    originList = []
    resizedList = []
    thumbList = []
    #make dirs in current folder.
    os.mkdir( os.path.join(targetDir, origin_dir ))
    os.mkdir( os.path.join(targetDir, resized_dir ))
    os.mkdir( os.path.join(targetDir, thumb_dir ))

    nameAlready=[]#for 1.jpg and 1.gif.
    for i in imgList:
        #get iname, if already, +=barrand.
        iname,iexp = os.path.splitext( i )
        if iname in nameAlready:
            iname = iname+barrand6()
        else:
            nameAlready.append(iname)
        #print(iexp,iname)

        isrc = os.path.join(targetDir, i) #dirname/imgfile.jpg
        idestname = os.path.join(targetDir, resized_dir ,iname)#+.jpg
        tdestname = os.path.join(targetDir, thumb_dir,iname )

        im = Image.open(isrc)
        try:
            #-----------resize----------------------
            imw = resizew
            # if gif, just save to dest.
            if iexp in ['.GIF','.gif']:
                im.save( idestname+'.gif') # its copy. origin remains.
                resizedList.append( iname+'.gif' )
            else:
                imh = int(im.size[1]/(im.size[0]/imw))
                im.resize((imw,imh),Image.LANCZOS).convert('RGB').save( idestname+'.jpg' ,quality=90)
                resizedList.append( iname+'.jpg' )
                # #if >w, resize and save.
                # if im.size[0]>imw:
                #     imh = int(im.size[1]/(im.size[0]/imw))
                #     im.resize((imw,imh),Image.LANCZOS).convert('RGB').save( idestname+'.jpg' ,quality=90)
                #     resizedList.append( iname+'.jpg' )
                # #too small, just save jpg.
                # else:
                #     im.save( idestname+'.jpg')
                #     resizedList.append( iname+'.jpg' )
            #-----------resize----------------------


            #-----------thumbnail----------------------
            #it shall be justsize, even small.
            imw = thumbw
            imh = int(im.size[1]/(im.size[0]/imw))
            if imh >=imw:
                nim = im.resize((imw,imh),Image.LANCZOS)
                imh = imw
                nim.crop( (0,0,imw,imh) ).convert('RGB').save( tdestname+'.jpg' ,quality=80)
                #im.resize((300,imh),Image.LANCZOS).convert('RGB').save( tdestname+'.jpg' ,quality=80)
            elif imh <imw:
                imh = thumbw
                imw = int( (im.size[0]/im.size[1]*imh))
                nim = im.resize((imw,imh),Image.LANCZOS)
                #imw = imh
                nim.crop( ((imw/2 -imh/2), 0, (imw/2 +imh/2), imh) ).convert('RGB').save( tdestname+'.jpg' ,quality=80)
            thumbList.append( iname+'.jpg' )
            #-----------thumbnail----------------------

            #-----------origin----------------------
            osrcimg = os.path.join(targetDir,i)
            odestimg = os.path.join(targetDir, origin_dir ,i)
            im = None# this was really problem!
            os.rename(osrcimg, odestimg)#move. we considered lot, but to zip(origin)!

            originList.append(i)
            #-----------origin----------------------
        except Exception as e:
            print(e)
            im = None
            raise Exception('err while im loop:{}'.format(iname))

    #originList# is imgList.
    #resizedList #is created.
    #thumbList #.. is  --.jpg. but if.. ..now we add it. fine.

    # imgDict = {}
    # imgDict[originkey] = originList
    # imgDict[resizedkey] = resizedList
    # imgDict[thumbkey] = thumbList
    #return imgDict

    returnList=[]
    returnList.append(originList)
    returnList.append(resizedList)
    returnList.append(thumbList)
    return returnList
