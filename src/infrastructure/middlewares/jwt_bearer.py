from fastapi import HTTPException,status
from fastapi.security import HTTPBearer
from starlette.requests import Request
from datetime import datetime
from src.infrastructure.exceptions.invalid_credentials_exception import InvalidCredentialsException
from src.infrastructure.exceptions.utils import get_http_exception
from src.infrastructure.utils.jwt_utils import validate_token
from src.services.user_service import UserService


class JWTBearer(HTTPBearer) :
    
    async def __call__(self, request: Request):
        
        self.user_service = UserService()
        
        try:
            
            auth = await super().__call__(request)
            
            credentials = validate_token(auth.credentials)
            
            expire = datetime.fromtimestamp(credentials['exp'])
            
            user = self.user_service.find_one({"email":credentials["email"]})
            
            if not user:
                
                raise get_http_exception(InvalidCredentialsException())
            
            if expire is None or datetime.utcnow() > expire:
                
                raise get_http_exception(InvalidCredentialsException())

            return user
    
        except Exception as error:
            
            raise get_http_exception(error)