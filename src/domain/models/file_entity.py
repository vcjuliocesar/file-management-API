from src.domain.models.base_entity import EntityBase
from sqlalchemy import Integer,String,Column,ForeignKey
from sqlalchemy.orm import relationship

class FileEntity(EntityBase):
    
    __tablename__ = "files"
    
    id:int = Column(Integer,primary_key=True)
    
    name:str = Column(String)
    
    path:str = Column(String)
    
    description:str = Column(String,default=None)
    
    owner_id:int = Column(Integer,ForeignKey("users.id"))
    
    owner = relationship("UserEntity",back_populates="files")
