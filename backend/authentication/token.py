import jwt, datetime

def create_access_token(id):
    return jwt.encode(
        {
            'user_id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 15),
            'iat': datetime.datetime.utcnow()
        },
        key='access_secret',
        algorithm = 'HS256'
    )

def create_refresh_token(id):
    return jwt.encode(
        {
            'user_id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days = 7),
            'iat': datetime.datetime.utcnow()
        },
        key='refresh_secret',
        algorithm = 'HS256'
    )

def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')
        return payload['user_id']
    except Exception as e:
        raise str(e)
    
def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        return payload['user_id']
    except Exception as e:
        raise str(e)


