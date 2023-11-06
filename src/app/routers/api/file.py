from fastapi import HTTPException,APIRouter,status,Depends
from fastapi.responses import JSONResponse
from src.infrastructure.schemas.file_schema import FileSchema,FilePostRequest
from src.app.usecases.file.create_file_use_case import CreateFileUseCase
from src.infrastructure.middlewares.jwt_bearer import JWTBearer

file_router = APIRouter(prefix="/api/v1",tags=['Files'])

@file_router.post("/files",response_model=FileSchema,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def create(file:FilePostRequest,token:str = Depends(JWTBearer()),file_case:CreateFileUseCase = Depends()):
    
    try:
        
        file_case.execute(file,token.id)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"File created"})
        
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
