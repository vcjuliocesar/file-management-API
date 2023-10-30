from src.domain.models.base_entity import EntityBase
from sqlalchemy import Integer,String,Column,Boolean

class UserEntity(EntityBase):
    
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    
    name = Column(String)
    
    email = Column(String,unique=True) 
    
    password = Column(String)
    
    is_active = Column(Boolean,default=True)
    
    is_admin = Column(Boolean,default=False)