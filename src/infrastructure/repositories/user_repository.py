from src.infrastructure.repositories.interfaces.user_interface import UserInterface
from src.domain.models.user_entity import UserEntity as User
from src.infrastructure.configs.database import Session

class UserRepository(UserInterface):
    
    def __init__(self) -> None:
        
        self.db = Session()
    
    def find_by_id(self,user_id:int) -> User:
        
        return self.db.query(User).filter(User.id == user_id).first()
        
    def get(self,user:User) -> User:
        pass
    
    def create(self,user:User) -> User:
        
        self.db.add(user)
        
        self.db.commit()
        
        return user
    
    def update(self, user:User) -> User:
        
        self.db.commit()
        
        self.db.refresh(user)
        
        return user
    
    def delete(self,user:User) -> None:
        
        self.db.delete(user)
        
        self.db.commit()