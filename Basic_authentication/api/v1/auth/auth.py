#!/usr/bin/env python3
"""
Auth module for API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if a path requires authentication """

        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Ensure trailing slash for comparison
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Return the Authorization header if present """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None (to be implemented later)"""
        return None
