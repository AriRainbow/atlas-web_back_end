#!/usr/bin/env python3
"""
BasicAuth module for API authentication using Basic Auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class inherits from Auth - for Basic Authentication"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts Base64 part from Basic Auth header
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]
