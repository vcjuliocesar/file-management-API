from abc import ABC,abstractmethod
from src.domain.models.user_entity import UserEntity as User

class UserInterface(ABC):
    
    @abstractmethod
    def find_by_id(self,user_id:int) -> User:
        pass
    
    @abstractmethod
    def find_one(self,crieria:dict) -> User:
        pass
    
    @abstractmethod
    def get(self) -> User:
        pass
    
    @abstractmethod
    def create(self,user:User) -> User:
        pass
    
    @abstractmethod
    def update(self,user:User) -> User:
        pass
    
    @abstractmethod
    def delete(self,user:User) -> None:
        pass