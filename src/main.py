from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError

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


@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(_, exc: RequestValidationError):
    error_fields = {}
    for pydantic_error in exc.errors():
        loc, msg = pydantic_error["loc"], pydantic_error["msg"]
        loc = loc[1:] if len(loc) > 1 and loc[0] in ("body", "query", "path") else ['__all__']
        for field in loc:
            if not isinstance(field, str):
                field = '__all__'
            error_fields[field] = msg
    return APIException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        error_code='ERR-422-000',
        message='Request validation error',
        error_fields=error_fields
    ).get_response()
