errlist=[]
#for all log in here.
def logerr():
    with open('jarerr.txt','a',encoding='utf-8') as f:
        for i in errlist:
            f.write(i)
            f.write('\n')
