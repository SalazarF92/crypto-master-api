import bcrypt

def calcHashedPassword(pwd):
    bytePwd = pwd.encode('utf-8')

    hash = bcrypt.hashpw(bytePwd, bcrypt.gensalt())
    
    return hash.decode('utf-8')

def validatePassword(pwd, hash):
    check = bcrypt.checkpw(pwd.encode('utf-8'), hash.encode('utf-8'))
    return check
