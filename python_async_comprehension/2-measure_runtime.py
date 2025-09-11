#!/usr/bin/env python3
"""
This module provides a coroutine that measures
the runtime of running async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import Callable

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times in parallel and measure total runtime.

    Returns:
        float: Total elapsed time to complete all four comprehensions.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
