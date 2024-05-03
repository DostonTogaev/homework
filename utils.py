import bcrypt


def hash_password(raw_password):
    encoded = raw_password.encode('utf-8')
    salt = bcrypt.gensalt(4)
    return bcrypt.hashpw(encoded, salt)

def check_password(password, hash):
    print(hash)
    print(password)
    # hashd = bcrypt.checkpw(raw_password, hash)
    if bcrypt.checkpw(password, hash):
        print('Password match!')
    else:
        print('Password incorrect!')


