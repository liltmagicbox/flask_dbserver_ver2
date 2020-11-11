#https://yeowool0217.tistory.com/536
import hashlib
#file_hash = hashlib.sha256()
#file_hash.update('massman25')
#print (file_hash.hexdigest())
a = hashlib.sha256( 'mas'.encode() )
#print( a.hexdigest() )


def shasha(intext):
    return hashlib.sha256(intext.encode() ).hexdigest()

print("userdb loading..")

# username, sha, salt, token
user={}
def newuser(username,sha):
    if len(username)>20:
        return 'too long username'
    if user.get(username) == None:
        salt = username
        tsalt = 'nosaltfrenchfries'
        user[username] = { "sha" : shasha(sha+salt) ,"token":shasha(username+tsalt), "salt" : salt ,  "tsalt" : tsalt  }
        return 'new account!'
    else:
        return 'username already exist..'

def login(username,sha):
    if user.get(username) == None:
        return 'no'#for secure reason..
    else:
        salt = user[username]["salt"]
        if user[username]["sha"] == shasha(sha+salt):
            #return 'log in! hello {}'.format(username)
            return user[username]["token"]
        else:
            return 'no'
