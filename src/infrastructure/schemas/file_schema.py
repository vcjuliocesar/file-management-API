from pydantic import BaseModel,Field
from typing import Optional


class FilePostRequest(BaseModel):
    
    name:str = Field("namefile",title="Name")
    
    path:str = Field("/path",title="Path")
    
    description:str = Field("This is one file",title="Description")
    

class FileSchema(FilePostRequest):
    
    id:Optional[int] = Field(default=None)
    
    owner_id:int
    
    class Config:
        
        from_attributes = True