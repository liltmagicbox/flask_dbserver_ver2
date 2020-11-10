user={}

def newuser(username,sha):
    if user.get(username) == None:
        user[username] = sha
        return 'new account!'
    else:
        return 'username already exist..'

def login(username,sha):
    if user.get(username) == None:
        return 'no username.'
    else:
        if user[username] == sha:
            return 'log in! hello {}'.format(username)
        else:
            return 'not log in.. '
