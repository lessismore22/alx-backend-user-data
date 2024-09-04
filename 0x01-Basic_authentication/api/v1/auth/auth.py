import request from flask
from typing import list, TypeVar

class Auth:
    """
    Auth class template for managing authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:

        """
        Method that determines if authentication is required for a given path.
        """

        if path is None:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True

        # Ensure path ends with a slash for comparison
         for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
        path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method that retrieves the authorization header from the Flask request object.
        Currently returns None, but will be implemented later.
        """
        return None

        if request is None:
            return None

        auth_header = request.headers.get("Authorization", None)
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that retrieves the current user from the Flask request object.
        Currently returns None, but will be implemented later.
        """
        return None
