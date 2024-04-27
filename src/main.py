from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException, RequestValidationError

from config import APP_TITLE, APP_VERSION
from exceptions import APIException
from logger import logger
from router import auth_router, groups_router, users_router

# FastAPI application
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

# App routes
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(groups_router)


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


@app.exception_handler(HTTPException)
async def http_exception_handler(_, exc: HTTPException):
    return APIException(
        status_code=exc.status_code,
        error_code=f'ERR-{exc.status_code}-000',
        message=exc.detail,
        headers=exc.headers,
    ).get_response()


@app.exception_handler(Exception)
async def exception_handler(_, exc: Exception):
    return APIException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        error_code='ERR-500-000',
        message=str(exc),
    ).get_response()


logger.info('Server start successful')
