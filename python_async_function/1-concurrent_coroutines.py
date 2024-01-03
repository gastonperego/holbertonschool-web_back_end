#!/usr/bin/env python3
"""EEEEEEEEOOOOOOOOO"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    "OOOOOOOAAAAAA"
    li = []
    for i in range(n):
        num = await wait_random(max_delay)
        li.append(num)
    return sorted(li)
