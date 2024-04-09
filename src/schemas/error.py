from pydantic import BaseModel


class FieldErrorSchema(BaseModel):
    field: str
    message: str | None = None


class ErrorSchema(BaseModel):
    status_code: int
    error_code: str | None = None
    message: str | None = None
    error_fields: list[FieldErrorSchema] | None = None
