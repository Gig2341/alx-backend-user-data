#!/usr/bin/env python3
"""this module represents the authentication class
"""


from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """this represents the authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """defines the require_auth method
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        # Ensure that all paths in excluded_paths end with a slash
        excluded_paths = [
                p if p.endswith('/') else p + '/' for p in excluded_paths
        ]
        # Check if the path is in excluded_paths
        return path + '/' not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
