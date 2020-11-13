import os

def txt2dir( targetdir ):
    txtlist = []
    errlist = []

    flist = os.listdir( targetdir)
    for i in flist:
        ipath = os.path.join( targetdir, i)

        name,ext = os.path.splitext(i)
        namedir = os.path.join( targetdir, name)
        if ext.lower() == '.txt':
            try:
                os.mkdir(namedir)
                os.rename(ipath, os.path.join(namedir,i) )
                txtlist.append(name)
            except Exception as e:
                errlist.append('txterr'+str(e)[:80] )
                #print(e)
    lastword = "in dir:{},txtdir:{}".format(len(flist),len(txtlist))
    #print( lastword )
    return txtlist,errlist
