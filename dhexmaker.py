#std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#mybase64chars  = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

base64chars  = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

#encode

def dhex3(i):
    b,c = divmod(i, 64)
    a,b = divmod(b, 64)
    return base64chars[a]+base64chars[b]+base64chars[c]


def dhexstr(ilist):
    return "".join( list(map(dhex3,ilist)) )

#decode

def dhexstrrev(s):
    #for i,ss in enumerate(s):
    return list(map( dhex3rev, [ s[i:i+3] for i in range(0,len(s),3) ]  ))

def dhex3rev(s):
    #a=s[0]
    a = base64chars.find(s[0])*64*64
    b = base64chars.find(s[1])*64
    c = base64chars.find(s[2])    
    return a+b+c
#>>> s='00000100A00B00/01001101/020100///'
#>>> dhexstrrev(s)
#[0, 1, 10, 11, 63, 64, 65, 127, 128, 4096, 262143]



#js has slice.
#https://stackoverflow.com/questions/5711452/how-do-i-slice-a-string-every-3-indices
#[str(i) for i in s]
#list(range(0,10,2)) 0,2,,

def dhex3decode(s):
    #for i,ss in enumerate(s):
    return [ s[i:i+3] for i in range(0,len(s),3) ]
#>>> s='00000100A00B00/01001101/020100///'
#>>> dhex3decode(s)
#['000', '001', '00A', '00B', '00/', '010', '011', '01/', '020', '100', '///']


#ilist=[0,1,10,11,63,64,65,127,128,4096,262143]
#"".join( list(map(dhex3,ilist)) )
#'00000100A00B00/01001101/020100///'

#created 2020-11-18.
##def dhexmaker(i):
##    diver = 64
##    b,c = divmod(i, diver)
##    a,b = divmod(b, diver)
##    aa= base64chars[a]
##    bb= base64chars[b]
##    cc= base64chars[c]
##    return aa+bb+cc

##def decmaker(i):
##    diver = 10
##    a,b = divmod(i, diver)
##    return a*diver+b
