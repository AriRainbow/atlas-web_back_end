#!/usr/bin/env python3
"""
Module for securely hashing passwords using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with automatic salt.

    Args:
        password: The plaintext password to be hashed.

    Returns:
        A salted bcrypt hashed password as bytes.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
