from auth.manager.auth import authenticate_manager, create_manager
from models.manager import ManagerCreate, ManagerLogin
from auth.constants import REFRESH_TOKEN_EXPIRES_TIME, SECRET_KEY, TOKEN_EXPIRES_TIME
from fastapi import HTTPException, Depends, APIRouter, status, Body
from fastapi_jwt_auth import AuthJWT

from database import get_database

from pydantic import BaseModel

router = APIRouter()




class Settings(BaseModel):
    authjwt_secret_key:str = SECRET_KEY
    authjwt_access_token_expires = TOKEN_EXPIRES_TIME
    authjwt_refresh_token_expires = REFRESH_TOKEN_EXPIRES_TIME


@AuthJWT.load_config
def get_config():
    return Settings()





@router.post("/signup")
async def sign_up(new_manager: ManagerCreate  = Body(...), db=Depends(get_database)):
    manager  = await create_manager(db=db,manager=new_manager)

    if manager:
        return manager
    else:
        return "email_already_exists"




@router.post('/login')
async def login(creds: ManagerLogin, Authorize: AuthJWT = Depends(), db = Depends(get_database)):
    email = await authenticate_manager(creds.username, creds.password,db)
    if not email:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )

    # Use create_access_token() and create_refresh_token() to create our
    access_token = Authorize.create_access_token(subject=creds.username)
    refresh_token = Authorize.create_refresh_token(subject=creds.username)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):

    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


