if 1==1: print(3)
if 2==2: print(4)

fluid={}
fluid['444']={}

key='태그'
#if fluid['444'][key]==None:fluid[no][key]=[]

import random
import time

d={}
for i in range(100000):
    d[i] = str( random.randint(0,1000000))


#4ms for 10만
k = str ( random.randint(0,100000) )
aa=time.time()
if k in d.values():
        print('haha')        
print(time.time()-aa )

#0.08294916152954102 when print.
#0.04197406768798828 for 10 check. 40ms?!

aa=time.time()
print('only prinf time',end='_')
print(time.time()-aa )

#0.0059967041015625 ... just print took 6ms..

keys = [ '태그', '댓', '추', '조' ]
dd = dict.fromkeys(keys,[])

aa=time.time()
if dd['태그'] ==[]:
    pass
print(time.time()-aa )
#fast.gotit.


#0ms for 10000.  4ms for 100000 1ms for 20000.fine.
ddd={}
for i in range(20000):
    ddd[i]= str(random.randint(0,1000000))

aa=time.time()
if '444' in ddd.values():
    fa=1
    print(3)
print(time.time()-aa ,'values')
#fast.gotit.
