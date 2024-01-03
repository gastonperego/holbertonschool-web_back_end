#!/usr/bin/env python3
"""waiting"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """aaaaaaaaaaaaa"""
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
