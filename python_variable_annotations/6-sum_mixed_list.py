#!/usr/bin/env python3
"""sum_mixed_list function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    "returns the sum of a list of ints and floats"
    return sum(mxd_lst)
