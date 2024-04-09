from fastapi.responses import JSONResponse

from schemas import ErrorSchema, FieldErrorSchema


class APIException(Exception):
    def __init__(self,
                 status_code: int = 500,
                 error_code: str | None = None,
                 message: str | None = None,
                 error_fields: dict[str, str] | None = None,
                 headers: dict[str, str] | None = None):
        self.status_code = status_code
        self.error_code = error_code
        self.message = message
        self.error_fields = error_fields
        self.headers = headers

    def dump(self):
        error_fields = [
            FieldErrorSchema(
                field=field,
                message=msg)
            for field, msg in self.error_fields.items()
        ] if self.error_fields is not None else None

        return ErrorSchema(
            status_code=self.status_code,
            error_code=self.error_code or f'ERR-{self.status_code}-000',
            message=self.message or 'Oops, there are some errors',
            error_fields=error_fields
        )

    def set(self,
            status_code: int | None = None,
            error_code: str | None = None,
            message: str | None = None,
            error_fields: dict[str, str] | None = None,
            headers: dict[str, str] | None = None):
        self.status_code = status_code if status_code is not None else self.status_code
        self.error_code = error_code if error_code is not None else self.error_code
        self.message = message if message is not None else self.message
        self.error_fields = error_fields if error_fields is not None else self.error_fields
        self.headers = headers if headers is not None else self.headers
        return self

    def get_response(self):
        return JSONResponse(content=self.dump().model_dump(exclude_none=True),
                            status_code=self.status_code,
                            headers=self.headers)
