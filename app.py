from custom_openapi import custom_openapi
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from database import db
from auth.manager.router import router as ManagerAuthRouter
from manager.router import router as ManagerRouter
from fastapi_jwt_auth.exceptions import AuthJWTException

app = FastAPI(debug=True)



origins = ["http://localhost:8081"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


#Mounting Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

#Mounting Routers
app.include_router(ManagerAuthRouter,tags=['Manager Authentication'],prefix='/manager/auth')
app.include_router(ManagerRouter,tags=['Manager Routes'],prefix='/manager')





@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this app ."}




@app.on_event("startup")
async def startup():
    await db.connect_to_database()


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()

# app.openapi = custom_openapi(app)