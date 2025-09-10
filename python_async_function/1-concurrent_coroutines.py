#!/usr/bin/env python3
"""Run wait_random n times concurrently and return list of delays in order."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with given max_delay and return
        list of results in order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Max delay allowed for wait_random.

    Returns:
        List[float]: List of delays in ascending order of completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
