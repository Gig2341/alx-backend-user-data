#!/usr/bin/env python3
"""this module represents the authentication class
"""


from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """this represents the authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' public method that checks which path requires auth '''
        if path is not None and excluded_paths:
            if not path.endswith('/'):
                path += '/'
            for excluded_path in excluded_paths:
                if excluded_path.endswith('*') \
                        and path.startswith(excluded_path[:-1]):
                    return False
                elif path == excluded_path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """defines the authorization hrader method
        """
        if request is None:
            return None
        # get header from the request
        header = request.headers.get('Authorization')
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
