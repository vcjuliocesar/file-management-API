from src.infrastructure.repositories.interfaces.file_interface import FileInterface
from src.domain.models.file_entity import FileEntity
from src.infrastructure.configs.database import Session

class FileRepository(FileInterface):
    
    def __init__(self) -> None:
        
        self.db = Session()
    
    def find_by_id(self,file_id:int,token) -> FileEntity:
        
        return self.db.query(FileEntity).filter((FileEntity.id == file_id) & (FileEntity.owner_id == token.id )).first()
    
    def find_by_email(self,file:FileEntity) -> FileEntity:
        
        return self.db.query(FileEntity).filter(FileEntity.email == file.email).first()
    
    def find_one(self,criteria:dict) -> FileEntity:
        
        return self.db.query(FileEntity).filter_by(**criteria).first()
    
    def get(self,owner) -> list:
        
        return self.db.query(FileEntity).filter(FileEntity.owner_id == owner).all()
    
    def create(self,file:FileEntity) -> FileEntity:
        
        self.db.add(file)
        
        self.db.commit()
        
        return file
    
    def update(self, file:FileEntity) -> FileEntity:
        
        self.db.commit()
        
        self.db.refresh(file)
        
        return file
    
    def delete(self,file:FileEntity) -> None:
        
        self.db.delete(file)
        
        self.db.commit()