# from models.restaurant import Restaurant, RestaurnatInDB
# from bson import ObjectId
# class RestaurantRepository():
#     collection = None
#     def __init__(self,db):
#         self.collection  = db.get_collection("restaurants")
    

#     async def create_restaurant(self,data:dict):
#         restaurant = await self.collection.insert_one(data)
#         new_restaurant = await self.collection.find_one({"_id":restaurant.inserted_id})
#         return Restaurant(**new_restaurant)


#     async def get_restaurantDB(self,data:dict):
#         restaurant = await self.collection.find_one(data)
#         if restaurant:
#             return RestaurantInDB(**restaurant)
#         else:
#             return None


#     async def get_restaurant(self,data:dict):
#         restaurant = await self.collection.find_one(data)
#         if restaurant:
#             return Restaurant(**restaurant)
#         else:
#             return None


#     async def get_restaurants(self):
#         restaurants = []
#         async for restaurant in self.collection.find():
#             restaurants.append(Restaurant(**restaurant))
#         return restaurants


#     async def get_restaurantsDB(self):
#         restaurants = []
#         async for restaurant in self.collection.find():
#             restaurants.append(RestaurantInDB(**restaurant))
#         return restaurants
        


#     async def update_restaurant(self,data:dict, id:str):
#         restaurant = await self.collection.find_one({"_id":ObjectId(id)})
#         if restaurant:
#             await self.collection.update_one({"_id":ObjectId(id)},{"$set":data})
#             return True
#         return False