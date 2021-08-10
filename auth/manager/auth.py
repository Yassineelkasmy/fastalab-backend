from models.manager import ManagerCreate, ManagerInDB
from auth.helpers import get_password_hash, verify_password
from database.database import MongoManager


async def authenticate_manager(username: str, password: str ,db:MongoManager):

    manager = await db.manager_repo.get_managerDB({"email":username})

    if not manager:

        return False

    if not verify_password(password, manager.hashed_password):

        return False

    return manager.email



async def create_manager(manager:ManagerCreate, db:MongoManager):
    checked = await db.manager_repo.get_manager({"email":manager.email})

    if checked:
        return None
    else:
        manager_dict = manager.dict()
        manager_dict['hashed_password'] = get_password_hash(manager.password)
        managerDB = ManagerInDB(**manager_dict)
        created = await db.manager_repo.create_manager(managerDB.dict())
        return created