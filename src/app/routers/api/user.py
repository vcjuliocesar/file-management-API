from fastapi import HTTPException,APIRouter,status
from fastapi.responses import JSONResponse
from src.infrastructure.schemas.user_schema import UserPostRequest,UserSchema
from src.app.usecases.user.create_user_use_case import CreateUserUseCase

user_router = APIRouter(prefix="/api/v1",tags=['Users'])

@user_router.post("/users",response_model=UserSchema,status_code=status.HTTP_200_OK)
async def create(user:UserPostRequest):
    try:
        
        user_case = CreateUserUseCase()
        
        user_case.execute(user)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"User created"})
    
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))