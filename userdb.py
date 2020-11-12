#https://yeowool0217.tistory.com/536
import hashlib
#file_hash = hashlib.sha256()
#file_hash.update('massman25')
#print (file_hash.hexdigest())
a = hashlib.sha256( 'mas'.encode() )
#print( a.hexdigest() )
#a = hashlib.sha256( '언젠가는말하고싶언s'.encode() ).hexdigest()[:10] easy 10 id.


def shasha(intext):
    return hashlib.sha256(intext.encode() ).hexdigest()

print("userdb loading..")

# username, sha, salt, token
tokens={}
user={}
def newuser(username,sha):
    if len(username)>20:
        return 'too long username'
    if len(username)==0:
        return 'too short username'
    if user.get(username) == None:
        salt = username
        tsalt = 'nosaltfrenchfries'
        user[username] = { "sha" : shasha(sha+salt) ,"token":shasha(username+tsalt), "salt" : salt ,  "tsalt" : tsalt  }
        tokens[ user[username]["token"] ] = username
        return 'new account!'
    else:
        return 'username already exist..'

def login(username,sha):
    if user.get(username) == None:
        return 'no'#for secure reason..
    salt = user[username]["salt"]
    if user[username]["sha"] == shasha(sha+salt):
        #return 'log in! hello {}'.format(username)
        return user[username]["token"]
    else:
        return 'no'#see function fetchlogin() in userfunc.js ...it's used for key..

# def tokencheck(username,token):
#     if user.get(username) == None:
#         return False
#     if token == user[username]["token"]:
#         return True
#     else:
#         return False
def tokencheck(token):
    if token in tokens:
        return tokens[token]#username
    else:
        return 'no'
