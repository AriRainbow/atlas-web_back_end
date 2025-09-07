#!/usr/bin/env python3
"""This module provides a higher-order function that returns a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The value to multiple by.

    Returns:
        Callable[[float], float]: A function tht takes a float and multiplies it by 'multiplier'.
    """
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
