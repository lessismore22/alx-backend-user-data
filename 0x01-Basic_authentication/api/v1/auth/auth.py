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

        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True
         # Ensure path ends with a slash for comparison
        path_with_slash = path if path.endswith('/') else path + '/'

        # Check if the path matches any of the excluded paths
        for excluded_path in excluded_paths:
            if excluded_path == path_with_slash:
                return False


    def authorization_header(self, request=None) -> str:

        """
        Implementation of
        authorization header

        """
        if request is None:
            return None
        
        if request.headers.get("Authorization", None)


    def current_user(self, request=None) -> TypeVar('User'):

        """
        Retrieves the current user
        from the flask object
        """

        return None
