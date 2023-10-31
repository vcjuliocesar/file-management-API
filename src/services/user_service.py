from src.domain.models.user_entity import UserEntity as User
from src.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.infrastructure.repositories.user_repository import UserRepository
from src.infrastructure.schemas.user_schema import UserSchema,UserPostRequest

class UserService:
    
    def __init__(self) -> None:
        
        self.user_repository = UserRepository()
    
    def get_all(self) -> list:
        
        return self.user_repository.get()
    
    def find_by_id(self,user_id:int):
        
        return self.user_repository.find_by_id(user_id)
    
    def find_one(self,criteria:dict) -> list:
        
        return self.user_repository.find_one(criteria)
        
    def create(self,user:UserSchema) -> User:
        
        exist = self.user_repository.find_one({"email":user.email})
        
        if exist:
            
            raise UserAlreadyExistsException()
        
        return self.user_repository.create(User(**user.model_dump()))
    
    def update(self,user_id:int,user_data:UserSchema) -> User:
        
        exist = self.user_repository.find_by_id(user_id)
        
        if not exist:
            
             raise UserNotFoundException()
        
        user = self.user_repository.find_by_id(user_id)
        
        user.name = user_data.name
        
        user.email = user_data.email
        
        user.password = user_data.password
        
        user.is_active = user_data.is_active
        
        user.is_admin = user_data.is_admin
        
        return self.user_repository.update(user)
    
    def delete(self,user_id:int) -> None:
        
        exist = self.user_repository.find_by_id(user_id)
        
        if not exist:
            
            raise UserNotFoundException()
        
        user = self.find_by_id(user_id)
        
        return self.user_repository.delete(user)