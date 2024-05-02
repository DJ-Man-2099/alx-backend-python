#!/usr/bin/env python3
"""7th Task"""


import math
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats as argument
    and returns their sum as a float."""
    return math.fsum(mxd_lst)
