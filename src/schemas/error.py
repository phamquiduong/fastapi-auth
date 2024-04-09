from pydantic import BaseModel


class FieldErrorSchema(BaseModel):
    field: str
    message: str


class ErrorSchema(BaseModel):
    status_code: int
    error_code: str
    message: str
    error_fields: list[FieldErrorSchema] | None
