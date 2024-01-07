#!/usr/bin/env python3
"""OOOOOOOOOOK"""

from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ddddddddd"""

    li = []
    for i in range(4):
        task = asyncio.create_task(async_comprehension())
        li.append(task)

    start_time = time()
    await asyncio.gather(*li)
    end_time = time()
    return end_time - start_time
