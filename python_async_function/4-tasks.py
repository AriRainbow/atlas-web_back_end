#!/usr/bin/env python3
"""Run multiple asyncio tasks concurrently using task_wait_random."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times and return list delays in ascending order.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: Sorted list of completed delays.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
