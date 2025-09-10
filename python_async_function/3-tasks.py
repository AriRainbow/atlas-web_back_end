#!/usr/bin/env python3
"""Returns an asyncio Task that runs wait_random with the given max_delay."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that runs wait_random.

    Args:
        max_delay (int): Tha maximum delay time for the coroutine.

    Returns:
        asyncio.Task: The created task that runs wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
