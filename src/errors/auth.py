from enum import Enum

from fastapi import status

from exceptions import APIException

AUTH_ERROR_HEADERS = {"WWW-Authenticate": "Bearer"}


class AuthError(Enum):
    AUTH_401_001 = APIException(status_code=status.HTTP_401_UNAUTHORIZED, headers=AUTH_ERROR_HEADERS,
                                error_code='AUTH-401-001', message='Expired signature')
    AUTH_401_002 = APIException(status_code=status.HTTP_401_UNAUTHORIZED, headers=AUTH_ERROR_HEADERS,
                                error_code='AUTH-401-001', message='Invalid signature')

    AUTH_403_001 = APIException(status_code=status.HTTP_403_FORBIDDEN, headers=AUTH_ERROR_HEADERS,
                                error_code='AUTH-401-001', message='You are not administrator')

    AUTH_404_001 = APIException(status_code=status.HTTP_404_NOT_FOUND, headers=AUTH_ERROR_HEADERS,
                                error_code='AUTH-401-001', message='User does not exist')
