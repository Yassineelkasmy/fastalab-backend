from models.size import Size






class SizeRepository():
    collection = None
    def __init__(self,db):
        self.collection  = db.get_collection("sizes")
    


    async def get_size(self,data:dict):
        size = await self.collection.find_one(data)
        if size:
            return Size(**size)
        
  