from fastapi import HTTPException,APIRouter,status,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.infrastructure.schemas.user_schema import UserPostRequest,UserSchema
from src.app.usecases.user.create_user_use_case import CreateUserUseCase
from src.app.usecases.user.update_user_use_case import UpdateUserUseCase
from src.app.usecases.user.delete_user_use_case import DeleteUserUseCase
from src.app.usecases.user.find_by_id_user_use_case import FindByIdUserUseCase
from src.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.infrastructure.exceptions.utils import get_http_exception

user_router = APIRouter(prefix="/api/v1",tags=['Users'])

@user_router.post("/users",response_model=UserSchema,status_code=status.HTTP_200_OK)
async def create(user:UserPostRequest,user_case:CreateUserUseCase = Depends()):
    
    try:
        
        user_case.execute(user)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"User created"})
    
    except UserAlreadyExistsException as error:
        
        raise get_http_exception(error)
        
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))

@user_router.get("/users/{id}",response_model=UserSchema,status_code=status.HTTP_200_OK)
async def get_by_id(id:int,user_case:FindByIdUserUseCase = Depends()):
    
    try:
        
        return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(user_case.execute(id)))
        
    except UserNotFoundException as error:
        
        raise get_http_exception(error)
    
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
    
@user_router.put("/users",response_model=UserSchema,status_code=status.HTTP_200_OK)
async def update(id:int,user:UserPostRequest,user_case:UpdateUserUseCase = Depends()):
    
    try:
        
        user_case.execute(id,user)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"User updated"})
        
    except UserNotFoundException as error:
        
        raise get_http_exception(error)
        
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
    
@user_router.delete("/users",status_code=status.HTTP_200_OK)
async def delete(id:int,user_case:DeleteUserUseCase = Depends()):
    
    try:
        
        user_case.execute(id)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"User deleted"})
        
    except UserNotFoundException as error:
        
        raise get_http_exception(error)
    
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))