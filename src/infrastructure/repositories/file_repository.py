from src.infrastructure.repositories.interfaces.file_interface import FileInterface
from src.domain.models.file_entity import FileEntity as File
from src.infrastructure.configs.database import Session

class FileRepository(FileInterface):
    
    def __init__(self) -> None:
        
        self.db = Session()
    
    def find_by_id(self,file_id:int) -> File:
        
        return self.db.query(File).filter(File.id == file_id).first()
    
    def find_by_email(self,file:File) -> File:
        
        return self.db.query(File).filter(File.email == file.email).first()
    
    def find_one(self,criteria:dict) -> File:
        
        return self.db.query(File).filter_by(**criteria).first()
    
    def get(self) -> list:
        
        return self.db.query(File).all()
    
    def create(self,file:File) -> File:
        
        self.db.add(file)
        
        self.db.commit()
        
        return File
    
    def update(self, file:File) -> File:
        
        self.db.commit()
        
        self.db.refresh(file)
        
        return File
    
    def delete(self,file:File) -> None:
        
        self.db.delete(file)
        
        self.db.commit()