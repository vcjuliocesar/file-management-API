from pydantic import BaseModel,Field
from typing import Optional

class UserPostRequest(BaseModel):
    
    name:str = Field(title="Name")
    
    email:str = Field(title="Email")
    
    password:str = Field(title="Password")

class UserSchema(UserPostRequest):
    
    id:Optional[int] = Field(default=None)
    
    is_active:bool
    
    is_admin:bool
    
    class Config:
        
        from_attributes = True