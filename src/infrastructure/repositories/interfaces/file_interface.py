from abc import ABC,abstractmethod
from src.domain.models.file_entity import FileEntity as File

class FileInterface(ABC):
    
    @abstractmethod
    def find_by_id(self,file_id:int) -> File:
        pass
    
    @abstractmethod
    def find_one(self,crieria:dict) -> File:
        pass
    
    @abstractmethod
    def get(self) -> File:
        pass
    
    @abstractmethod
    def create(self,File:File) -> File:
        pass
    
    @abstractmethod
    def update(self,File:File) -> File:
        pass
    
    @abstractmethod
    def delete(self,File:File) -> None:
        pass