#!/usr/bin/env python3
"""
BasicAuth module for API authentication using Basic Auth
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class inherits from Auth - for Basic Authentication"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts Base64 part from Basic Auth header
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str)):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64-encoded authorization header
        """
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None
