from os import XATTR_SIZE_MAX
from models.restaurant import Restaurant
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
        if manager:
            return ManagerInDB(**manager)
        else:
            return None


    async def get_manager(self,data:dict):
        manager = await self.collection.find_one(data)
        if manager:
            return Manager(**manager)
        else:
            return None


    async def get_managers(self):
        managers = []
        async for manager in self.collection.find():
            managers.append(Manager(**manager))
        return managers


    async def get_managersDB(self):
        managers = []
        async for manager in self.collection.find():
            managers.append(ManagerInDB(**manager))
        return managers
        


    async def update_manager(self,data:dict, id:str):
        manager = await self.collection.find_one({"_id":ObjectId(id)})
        if manager:
            await self.collection.update_one({"_id":ObjectId(id)},{"$set":data})
            return Manager(**manager)
        return False

    async def delete_manager(self,email:str):
        manager = await self.collection.delete_one({"email":email})
        if manager:
            return True
        else:
            return False
        
    
    #Restaurants Managing Routes

    async def create_restaurant(self,restaurantData:dict,managerEmail:str):
        manager = await self.collection.find_one({"email":managerEmail})
        if manager:         
            restaurants = await self.collection.update_one({"email":managerEmail},{"$push":{"restaurants":restaurantData}})
            return restaurants
        else:
            return False 

    async def update_restaurant(self,restaurantData:dict,managerEmail:str,restaurantID:str):
        updateQuery = dict()
        
        for k in restaurantData.keys():
            updateQuery.update({f"restaurants.$.{k}":restaurantData[k]})

        restaurant = await self.collection.update_one({"email":managerEmail,"restaurants.id":restaurantID},{"$set":updateQuery})
        if restaurant:
            return Restaurant(**restaurant)
        else:
            return False

    


