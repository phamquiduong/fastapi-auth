from fastapi import FastAPI

from router import auth_router, users_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
