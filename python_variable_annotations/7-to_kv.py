#!/usr/bin/env python3
"""
This module defines a function that returns a tuple with a string and
the square of a number as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.

    Args:
        k (str): A string key.
        v (Union[int,float]): A number to be squared.
    
    Returns:
        Tuple[str, float]: A tuple with the original string and the square of the number as a float.
    """
    return (k, float(v * v))
