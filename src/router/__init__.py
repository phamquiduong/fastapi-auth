from router.auth import router as auth_router
from router.groups import router as groups_router
from router.users import router as users_router

__all__ = [
    'auth_router',
    'users_router',
    'groups_router',
]
