#!/usr/bin/env python3
"""
This module contains a coroutine the defines asynchronous generator,
which yields 10 random float numbers between 0 and 10 with a 1-second delay between each.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield 10 random floats between 0 and 10 asynchronously,
    pausing 1 second between each.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
