import request from flask
from typing import list, TypeVar


class Auth:

    """
    Auth class template for managing authentication

    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:

        """
        Implementation of require_
        auth

        """
        return False

    def authorization_header(self, request=None) -> str:

        """
        Implementation of
        authorization header

        """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
