#!/usr/bin/env python3
"""measure time"""

import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """aaaaaaaaaaaaaa"""
    li = asyncio.run(wait_n(n, max_delay))
    total_time = 0
    for time in li:
        total_time += time

    return total_time / n
