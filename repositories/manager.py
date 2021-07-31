from models.manager import Manager, ManagerInDB
from bson import ObjectId





class ManagerRepository():
    collection = None
    def __init__(self,db):
        self.collection  = db.get_collection("managers")
    

    async def create_manager(self,data:dict):
        manager = await self.collection.insert_one(data)
        new_manager = await self.collection.find_one({"_id":manager.inserted_id})
        return Manager(**new_manager)


    async def get_managerDB(self,data:dict):
        manager = await self.collection.find_one(data)
        return ManagerInDB(**manager)


    async def get_manager(self,data:dict):
        manager = await self.collection.find_one(data)
        return Manager(**manager)


    async def get_managers(self):
        managers = []
        async for manager in self.collection.find():
            managers.append(Manager(**manager))


    async def get_managersDB(self):
        managers = []
        async for manager in self.collection.find():
            managers.append(ManagerInDB(**manager))


    async def update_manager(self,data:dict, id:str):
        manager = await self.collection.find_one({"_id":ObjectId(id)})
        if manager:
            await self.collection.update_one({"_id":ObjectId(id)},{"$set":data})
            return True
        return False