from enum import Enum

from fastapi import status

from exceptions import APIException


class UsersError(Enum):
    USERS_403_001 = APIException(status_code=status.HTTP_403_FORBIDDEN, error_code='AUTH-403-001',
                                 message='You cannot get other user information when you are not an admin.')

    USERS_404_001 = APIException(status_code=status.HTTP_404_NOT_FOUND, error_code='AUTH-404-001',
                                 message='User with this id does not exist')
