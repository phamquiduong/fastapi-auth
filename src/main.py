from fastapi import FastAPI

from config import APP_TITLE, APP_VERSION
from exceptions import APIException
from router import auth_router, users_router

app = FastAPI(
    docs_url='/',
    title=APP_TITLE,
    version=APP_VERSION,
    contact={
        'name': 'Pham Qui Duong',
        'url': 'https://github.com/phamquiduong',
        'email': 'phamquiduong@outlook.com',
    }
)

app.include_router(auth_router)
app.include_router(users_router)


# App custom error handlers
@app.exception_handler(APIException)
async def fastapi_exception_handler(_, exc: APIException):
    return exc.get_response()
