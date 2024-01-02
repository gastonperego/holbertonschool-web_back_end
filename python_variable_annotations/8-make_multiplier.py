#!/usr/bin/env python3
"""make_multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a number by multiplier"""
    def func(num: float) -> float:
        return num * multiplier
    return func
