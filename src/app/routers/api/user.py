from fastapi import HTTPException,APIRouter,status
from fastapi.responses import JSONResponse
from src.domain.models.user_entity import UserEntity as User
from src.infrastructure.schemas.user_schema import UserPostRequest,UserSchema
from src.usecases.user.create_user_use_case import CreateUserUseCase
from src.interactor.user_interactor import UserInteractor

user_router = APIRouter()

@user_router.post("/users",tags=['Users'],response_model=UserSchema,status_code=status.HTTP_200_OK)
async def create(user:UserPostRequest) -> User:
    try:
        user_case = CreateUserUseCase()
        user_case.execute(user)
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"User created"})
        #return (CreateUserUseCase()).execute(user)
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))