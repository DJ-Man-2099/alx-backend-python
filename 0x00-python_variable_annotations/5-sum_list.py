#!/usr/bin/env python3
"""6th Task"""


import math
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """takes a list input_list of floats as argument
    and returns their sum as a float."""
    return math.fsum(input_list)
