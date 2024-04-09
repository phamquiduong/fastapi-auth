from enum import Enum

from fastapi import status

from exceptions import APIException

AUTH_ERROR_HEADERS = {"WWW-Authenticate": "Bearer"}


class AuthError(Enum):
    AUTH_400_001 = APIException(status_code=status.HTTP_400_BAD_REQUEST,
                                error_code='AUTH-400-001', message='Email does not exist')
    AUTH_400_002 = APIException(status_code=status.HTTP_400_BAD_REQUEST,
                                error_code='AUTH-400-002', message='Password incorrect')

    AUTH_401_001 = APIException(status_code=status.HTTP_401_UNAUTHORIZED, headers=AUTH_ERROR_HEADERS,
                                error_code='AUTH-401-001', message='Expired signature')
    AUTH_401_002 = APIException(status_code=status.HTTP_401_UNAUTHORIZED, headers=AUTH_ERROR_HEADERS,
                                error_code='AUTH-401-002', message='Invalid signature')

    AUTH_403_001 = APIException(status_code=status.HTTP_403_FORBIDDEN, headers=AUTH_ERROR_HEADERS,
                                error_code='AUTH-403-001', message='You are not administrator')

    AUTH_404_001 = APIException(status_code=status.HTTP_404_NOT_FOUND, headers=AUTH_ERROR_HEADERS,
                                error_code='AUTH-404-001', message='User does not exist')

    AUTH_409_001 = APIException(status_code=status.HTTP_409_FORBIDDEN,
                                error_code='AUTH-409-001', message='User already registered')
