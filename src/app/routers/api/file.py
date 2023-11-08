from fastapi import HTTPException,APIRouter,status,Depends,UploadFile
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.infrastructure.exceptions.utils import get_http_exception
from src.infrastructure.schemas.file_schema import FileSchema,FilePostRequest
from src.infrastructure.middlewares.jwt_bearer import JWTBearer
from src.domain.exceptions.file_not_found_exception import FileNotFoundException
from src.app.usecases.file.create_file_use_case import CreateFileUseCase
from src.app.usecases.file.find_file_by_id_use_case import FindFileByIdUseCase
from src.app.usecases.file.get_all_files_use_case import GetAllFilesUseCase
from src.app.usecases.file.delete_file_use_case import DeleteFileUseCase

file_router = APIRouter(prefix="/api/v1",tags=['Files'])

@file_router.post("/file/upload",response_model=FileSchema,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def upload_file(name:str,description:str,file:UploadFile,token:str = Depends(JWTBearer()),file_case:CreateFileUseCase = Depends()):
    
    try:
         
        file_case.execute(name,description,file,token)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"name":file.filename,"message":"File created"})
        
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))

@file_router.get("/file/{id}",response_model=FileSchema,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def get_by_id(id:int,token:str = Depends(JWTBearer()),file_case:FindFileByIdUseCase = Depends()):
    
    try:
        
        return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(file_case.execute(id,token)))
    
    except FileNotFoundException as error:
        
        raise get_http_exception(error)
    
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
    
@file_router.get("/files",response_model=FileSchema,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def get(token:str = Depends(JWTBearer()),file_case:GetAllFilesUseCase = Depends()):
    
    try:
        
        return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(file_case.execute(token.id)))
    
    except FileNotFoundException as error:
        
        raise get_http_exception(error)
    
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
    
@file_router.delete("/files",status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def delete(id:int,token:str = Depends(JWTBearer()),file_case:DeleteFileUseCase = Depends()):
    
    try:
        
        file_case.execute(id,token)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"File deleted"})
    
    except FileNotFoundException as error:
        
        raise get_http_exception(error)
    
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))