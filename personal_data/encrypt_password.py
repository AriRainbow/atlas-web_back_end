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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that a provided password matches a hashed password.

    Args:
        hashed_password: The hashed password (from bcrypt).
        password: The plaintext password to validate.

    Returns:
        True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
