#!/usr/bin/env python3
"""
This module provides a coroutine that gathers
random numbers using async comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random floats asynchonously using an async comprehension
    over the async_generator coroutine, and return the values as a list.
    """
    return [i async for i in async_generator()]
