#!/usr/bin/env python3
"""OOOOOOOOOOK"""

import asyncio
from random import uniform


async def async_generator():
    """KKKKKKK (risa br)"""

    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
