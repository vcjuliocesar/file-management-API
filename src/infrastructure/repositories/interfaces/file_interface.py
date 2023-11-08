from abc import ABC,abstractmethod
from src.domain.models.file_entity import FileEntity

class FileInterface(ABC):
    
    @abstractmethod
    def find_by_id(self,file_id:int,token) -> FileEntity:
        pass
    
    @abstractmethod
    def find_one(self,crieria:dict) -> FileEntity:
        pass
    
    @abstractmethod
    def get(self) -> FileEntity:
        pass
    
    @abstractmethod
    def create(self,File:FileEntity) -> FileEntity:
        pass
    
    @abstractmethod
    def update(self,File:FileEntity) -> FileEntity:
        pass
    
    @abstractmethod
    def delete(self,File:FileEntity) -> None:
        pass