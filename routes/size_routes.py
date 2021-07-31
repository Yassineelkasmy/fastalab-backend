from database import get_database
from fastapi.param_functions import Depends

from fastapi import APIRouter

from models.size import * 



router = APIRouter()



@router.get("/size")
async def get_all_sizes(size:str,db=Depends(get_database)):
    sizes = await db.size_repo.get_size({"size":size})
    return sizes