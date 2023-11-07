from fastapi import HTTPException,APIRouter,status,Depends,UploadFile
from fastapi.responses import JSONResponse
from src.infrastructure.schemas.file_schema import FileSchema,FilePostRequest
from src.app.usecases.file.create_file_use_case import CreateFileUseCase
from src.infrastructure.middlewares.jwt_bearer import JWTBearer

file_router = APIRouter(prefix="/api/v1",tags=['Files'])

@file_router.post("/file/upload",response_model=FileSchema,status_code=status.HTTP_200_OK)
async def upload_file(name:str,description:str,file:UploadFile,file_case:CreateFileUseCase = Depends()):
    
    try:
        
        # if not allowed_file(file.filename):
            
        #      return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,content={"message":"Invalid document"})
        
        # new_file_name = new_filename(name,file.filename)
        
        # file_path = os.path.join(UPLOAD_DIR,new_file_name)
        
        # with open(file_path,"wb") as uploaded_file:
            
        #     uploaded_file.write(file.file.read())
            
        file_case.execute(name,description,file)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"name":file.filename,"message":"File created"})
        
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
