from jwt import encode,decode
from datetime import datetime,timedelta

def create_token(data:dict) -> dict:
    
    payload = __expire_token(data)
    
    token:str = encode(payload,"Mysecr3tK4y",algorithm="HS256")
    
    return token

def validate_token(token:str) -> dict :
    
    data:dict = decode(token,key="Mysecr3tK4y",algorithm="HS256")
    
    return data

def __expire_token(data:dict):
    
    to_encode = data.copy()
    
    token_expires = timedelta(minutes=30)
    
    expire = datetime.utcnow() + token_expires
    
    to_encode.update({'exp':expire})
    
    return to_encode