#!/usr/bin/env python3
"""OOOOOOOOOOK"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """FFFFFFFFF"""
    return [i async for i in async_generator()]
