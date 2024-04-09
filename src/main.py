from fastapi import FastAPI

from exceptions import APIException
from router import auth_router, users_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)


# App custom error handlers
@app.exception_handler(APIException)
async def fastapi_exception_handler(_, exc: APIException):
    return exc.get_response()
