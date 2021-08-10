from fastapi import HTTPException, Depends, APIRouter, status, Body
from fastapi_jwt_auth import AuthJWT

from database import get_database

from pydantic import BaseModel



router = APIRouter()


@router.get('/protected' ,operation_id="authorize")
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    # Authorize.jwt_optional()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}



