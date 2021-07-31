from repositories.manager import ManagerRepository
from repositories.size import SizeRepository
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase 
from decouple import config


MONGO_DETAILS = config('MONGO_DETAILS')

# client = AsyncIOMotorClient(MONGO_DETAILS)

# database = client.fastalab




class MongoManager():
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None
    size_repo: SizeRepository = None
    manager_repo: ManagerRepository = None

    async def connect_to_database(self):
        print("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(
            MONGO_DETAILS,
            maxPoolSize=10,
            minPoolSize=10)
        self.db = self.client.fastalab
        self.size_repo = SizeRepository(self.db)
        self.manager_repo = ManagerRepository(self.db)
        print("Connected to MongoDB.")

    async def close_database_connection(self):
        print("Closing connection with MongoDB.")
        self.client.close()
        print("Closed connection with MongoDB.")








