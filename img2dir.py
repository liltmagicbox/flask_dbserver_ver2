import os

imgExt = {'.jpg','.jpeg','.png','.gif','.webp','.bmp',}

def img2dir( targetdir ):
    imglist = []
    errlist = []

    flist = os.listdir( targetdir)
    for i in flist:
        ipath = os.path.join( targetdir, i)

        name,ext = os.path.splitext(i)
        namedir = os.path.join( targetdir, name+ext[1:])#just i cuts ext.
        #note if dirname == 1.jpg , split works.
        if ext.lower() in imgExt:
            try:
                os.mkdir(namedir)
                os.rename(ipath, os.path.join(namedir,i) )
                imglist.append(name)
            except Exception as e:
                errlist.append('img2dir:'+str(e)[:180] )
                #print(e)
    #lastword = "in dir:{},imgdir:{}".format(len(flist),len(imglist))
    #print( lastword )
    return imglist,errlist
