from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from database import db
app = FastAPI(debug=True)



origins = ["http://localhost:8081"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






app.mount("/static", StaticFiles(directory="static"), name="static")





@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this app ."}



# app.include_router(SizeRouter, tags=["Size CRUD"], prefix="/sizes")

@app.on_event("startup")
async def startup():
    await db.connect_to_database()


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()