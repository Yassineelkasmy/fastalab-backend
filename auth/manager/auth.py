from models.manager import ManagerCreate, ManagerInDB
from auth.helpers import get_password_hash, pin_code_genrator, verify_expire_date, verify_password
from database.database import MongoManager
from datetime import timedelta , datetime



async def authenticate_manager(username: str, password: str ,db:MongoManager):
    manager = await db.manager_repo.get_managerDB({"email":username})
    if not manager:

        return False

    if not verify_password(password, manager.hashed_password):

        return False

    return manager.email


async def manager_exists(email:str,db:MongoManager):
    checked = await db.manager_repo.get_manager({"email":email})
    return checked

async def create_manager(manager:ManagerCreate, db:MongoManager):
    checked = await manager_exists(email=manager.email,db=db)

    if checked:
       if checked.verified:
           return None

    if checked:
        await db.manager_repo.delete_manager(checked.email)
    manager_dict = manager.dict(exclude_none=True)
    manager_dict['hashed_password'] = get_password_hash(manager.password)
    managerDB = ManagerInDB(**manager_dict)
    created = await db.manager_repo.create_manager(managerDB.dict(by_alias=True,exclude_none=True))
        
    return created


async def send_sign_up_code_verification(email:str, db:MongoManager):
    pinCode = pin_code_genrator()
    pinCodeHash = get_password_hash(pinCode)
    expire = (datetime.utcnow() + timedelta(minutes=5)).isoformat()
    verication = {'signup_verification':{'pin_code':pinCodeHash,'expires' : expire}}
    checked = await db.manager_repo.get_manager({"email":email})
    if checked:
        await db.manager_repo.update_manager(data=verication,id=checked.id)

        #TODO: Send vericiation code email

    else:
        return None


async def send_forgot_password_code_verification(email:str, db:MongoManager):
    pinCode = pin_code_genrator()
    pinCodeHash = get_password_hash(pinCode)
    expire = datetime.utcnow() + timedelta(minutes=5)
    verication = {'forgot_verification':{'pin_code':pinCodeHash,'expires' : expire}}
    checked = await manager_exists(email=email,db=db)
    if checked:
        await db.manager_repo.update_manager(data=verication,id=checked.id)

        print(pinCode)

    else:
        return None


async def verify_manager(email:str,pinCode:str,db:MongoManager):
    checked = await db.manager_repo.get_managerDB({"email":email})
    if checked:
        verification_success = verify_password(pinCode,checked.signup_verification.pin_code) and verify_expire_date(checked.signup_verification.expires)

        if verification_success:
            manager = await db.manager_repo.update_manager(data={'verified':True},id=checked.id)
            if manager:
                return True
    else:
        return None



async def update_password(email:str,pinCode:str,db:MongoManager,password:str):
    checked = await db.manager_repo.get_managerDB({"email":email})
    if checked:
        if verify_password(plain_password=pinCode,hashed_password=checked.forgot_verifcation.pin_code):
            hashed_password = get_password_hash(password)
            manager = await db.manager_repo.update_manager(data={'hashed_password':hashed_password},id=checked.id)
            if manager:
                return True
            
    else:
        return None


