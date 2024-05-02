#!/usr/bin/env python3
"""9th Task"""


import math
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """takes a string k and an int OR float v as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v"""
    return lambda x: x * multiplier
