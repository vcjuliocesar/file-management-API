from src.infrastructure.repositories.interfaces.user_interface import UserInterface
from src.domain.models.user_entity import UserEntity as User
from src.infrastructure.configs.database import Session

class UserRepository(UserInterface):
    
    def __init__(self) -> None:
        
        self.db = Session()
    
    def get(self,user:User) -> User:
        pass
    
    def create(self,user:User) -> User:
        
        self.db.add(user)
        
        self.db.commit()
        
        return user
    
    def update(self, user:User) -> User:
        pass