#!/usr/bin/env python3
"""EEEEEEEEOOOOOOOOO"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    "OOOOOOOAAAAAA"
    li = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        li.append(task)

    times = []
    for task in asyncio.as_completed(li):
        time = await task
        times.append(time)

    return times
