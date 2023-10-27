from abc import ABC,abstractmethod
from src.domain.models.user_entity import UserEntity as User

class UserInterface(ABC):
    
    @abstractmethod
    def get(self,user_id:User) -> User:
        pass
    
    @abstractmethod
    def create(self,user:User) -> User:
        pass
    
    @abstractmethod
    def update(self,user:User) -> User:
        pass