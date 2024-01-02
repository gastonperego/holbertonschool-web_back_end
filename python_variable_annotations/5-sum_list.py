#!/usr/bin/env python3
"""fsum_list function"""


def sum_list(input_list: list[float]) -> float:
    "returns the sum of a list of floats"
    i: float = 0.0
    for num in input_list:
        i += num
    return i
